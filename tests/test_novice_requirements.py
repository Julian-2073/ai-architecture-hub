"""Novice phrasing, grounded Codex interpretation and recipe evidence boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('novice_kb', ROOT/'scripts/kb.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


def call(request, intent=None, extra=()):
    with tempfile.TemporaryDirectory() as folder:
        args = [sys.executable,str(ROOT/'scripts/kb.py'),'discover',request,'--json',*extra]
        if intent is not None:
            file = Path(folder)/'intent.json';file.write_text(json.dumps(intent,ensure_ascii=False))
            args.extend(['--intent',str(file)])
        process = subprocess.run(args,capture_output=True,text=True)
        return process, json.loads(process.stdout)


def intent_for(request, scenario='scenario-interactive-3d', certainty='inferred'):
    return {'schema_version':1,'goals':[{'scenario_id':scenario,'source_quote':request,'certainty':certainty}],
            'known_constraints':[],'excluded_scenarios':[],'open_questions':[]}


class NoviceRequirementsTests(unittest.TestCase):
    def test_observed_equipment_request_discovers_space_and_state(self):
        _, result = call('想把厂里的设备都放到一个能走进去看的画面里，点一台机器就知道它现在有没有故障')
        ids = {s['id'] for s in result['scenarios']}
        self.assertTrue({'scenario-interactive-3d','scenario-business-twin'} <= ids)
        self.assertEqual({p['id'] for p in result['implementation_paths']},
                         {'template-path-product-3d','template-path-device-twin'})
        self.assertIn('来源', ' '.join(q for p in result['implementation_paths'] for q in p['acceptance']))

    def test_digital_twin_name_does_not_force_3d(self):
        _, result = call('我要做一套可交互的企业数字孪生系统')
        self.assertIn('scenario-business-twin',{s['id'] for s in result['scenarios']})
        tools = {c['id'] for p in result['candidate_paths'] for c in p['candidates']}
        self.assertNotIn('tech-blender', tools)
        self.assertNotIn('tech-threejs', tools)
        self.assertTrue(any('业务' in q or '状态来自' in q for q in result['questions_that_may_change_direction']))

    def test_vague_plugin_gets_domain_questions_not_forced_stack(self):
        _, result = call('帮我生成一个3D插件')
        self.assertEqual(result['status'],'needs_clarification')
        self.assertEqual(result['candidate_paths'],[])
        self.assertTrue(any('哪个软件或网页' in q for q in result['questions_that_may_change_direction']))

    def test_new_wording_uses_grounded_codex_interpretation(self):
        request='让买家绕着商品瞧瞧，看看背后和底下的样子'
        _, raw = call(request)
        self.assertEqual(raw['status'],'needs_clarification')
        _, understood = call(request,intent_for(request))
        self.assertEqual(understood['understanding']['mode'],'codex_grounded_interpretation')
        self.assertTrue(understood['understanding']['assumptions_to_confirm'])
        self.assertEqual(understood['implementation_paths'][0]['id'],'template-path-product-3d')
        self.assertEqual(understood['agent_next_step'],'confirm_inferences_and_constraints')

    def test_quoted_constraints_remain_separate_from_inference(self):
        request='在手机浏览器让买家绕着商品瞧瞧'
        intent=intent_for(request)
        intent['known_constraints']=[{'name':'platform','value':'mobile browser','source_quote':'手机浏览器'}]
        _, result=call(request,intent)
        self.assertEqual(result['understanding']['known_constraints'],intent['known_constraints'])
        self.assertTrue(result['understanding']['assumptions_to_confirm'])

    def test_inline_interpretation_supports_readonly_discussion(self):
        request='让买家绕着商品瞧瞧'
        process,result=call(request,extra=('--intent-json',json.dumps(intent_for(request))))
        self.assertEqual(process.returncode,0)
        self.assertEqual(result['understanding']['mode'],'codex_grounded_interpretation')
        self.assertTrue(result['implementation_paths'])

    def test_invalid_inline_shape_is_controlled_error(self):
        process,result=call('产品展示',extra=('--intent-json','[]'))
        self.assertEqual(process.returncode,2)
        self.assertFalse(result['ok'])

    def test_oversized_inline_interpretation_is_rejected(self):
        process,result=call('产品展示',extra=('--intent-json',json.dumps({'padding':'x'*65537})))
        self.assertEqual(process.returncode,2)
        self.assertIn('64KiB',result['error'])

    def test_false_quote_unknown_scenario_and_conflict_are_rejected(self):
        request='让买家绕着商品瞧瞧'
        cases=[]
        bad=intent_for(request);bad['goals'][0]['source_quote']='用户没有说过这句话';cases.append(bad)
        bad=intent_for(request,scenario='scenario-nonexistent');cases.append(bad)
        bad=intent_for(request);bad['excluded_scenarios']=[{'scenario_id':'scenario-interactive-3d','source_quote':request}];cases.append(bad)
        bad=intent_for(request);bad['known_constraints']=[{'name':'platform','value':'web','source_quote':'浏览器'}];cases.append(bad)
        for bad in cases:
            with self.subTest(bad=bad):
                process,result=call(request,bad)
                self.assertEqual(process.returncode,2)
                self.assertFalse(result['ok'])

    def test_explicit_exclusion_prevents_lexical_engine_route(self):
        request='不要三维，只看设备故障'
        intent=intent_for(request,scenario='scenario-business-twin',certainty='explicit')
        intent['excluded_scenarios']=[{'scenario_id':'scenario-interactive-3d','source_quote':'不要三维'}]
        _, result=call(request,intent)
        self.assertNotIn('scenario-interactive-3d',{s['id'] for s in result['scenarios']})

    def test_understanding_recovers_workflow_without_canvas_words(self):
        request='把几个处理步骤像积木一样连起来'
        _, result=call(request,intent_for(request,scenario='scenario-node-workflow'))
        self.assertIn('template-path-workflow',{p['id'] for p in result['implementation_paths']})

    def test_understanding_corrects_partial_file_upload_match(self):
        request='上传公司资料后问问题，还要告诉我答案依据哪段话'
        _, result=call(request,intent_for(request,scenario='scenario-rag-answers'))
        self.assertEqual({s['id'] for s in result['scenarios']},{'scenario-rag-answers'})
        self.assertIn('template-path-document-qa',{p['id'] for p in result['implementation_paths']})

    def test_runtime_recipe_never_claims_this_project_is_verified(self):
        _, result=call('像搭积木一样拖来拖去，把几个处理步骤连起来')
        path=next(p for p in result['implementation_paths'] if p['id']=='template-path-workflow')
        self.assertEqual(path['verified_references'],[])
        self.assertEqual(path['execution_status'],'not_executed')
        self.assertIn('未执行验证',path['reference_boundary'])
        self.assertEqual(path['readiness'],'recipe_only_not_project_verified')

    def test_environment_inventory_does_not_invoke_software(self):
        from unittest.mock import patch
        module=kb.discovery_module().requirements
        with patch.object(module.shutil,'which',return_value=None), patch.object(module.Path,'is_file',return_value=False):
            result=module.environment_inventory()
        self.assertTrue(all(v['status']=='not_found_in_checked_locations' for v in result['tools'].values()))

    def test_functional_negation_is_a_requirement(self):
        _, result=call('不用刷新就能看到设备状态实时更新')
        self.assertIn('scenario-realtime-status',{s['id'] for s in result['scenarios']})
        _, result=call('不要三维场景，只要折线图展示经营趋势')
        self.assertNotIn('scenario-interactive-3d',{s['id'] for s in result['scenarios']})

    def test_recipe_reference_and_stage_validation(self):
        data=kb.load(ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            payload=json.loads((ROOT/'data/implementation-paths.json').read_text())
            payload['paths'][0]['verified_reference_ids']=['tech-blender']
            payload['paths'][0]['stages'][0].pop('check')
            (root/'paths.json').write_text(json.dumps(payload))
            data['implementation_paths_path']='paths.json'
            errors=kb.discovery_module().requirements.validate_paths(root,data)
            self.assertTrue(any('缺少项目集成通过证据' in e for e in errors))
            self.assertTrue(any('阶段缺少' in e for e in errors))


if __name__=='__main__':unittest.main(verbosity=2)
