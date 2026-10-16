"""Business requests exercise routing, evidence and safe project inspection end to end."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('discovery_kb', ROOT/'scripts/kb.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


def run_request(query, *args):
    command = [sys.executable, str(ROOT/'scripts/kb.py'), 'discover', query, *args, '--json']
    result = subprocess.run(command, capture_output=True, text=True)
    return result, json.loads(result.stdout)


def tools(result):
    return {r['id'] for option in result['candidate_paths'] for r in option['candidates']}


class BusinessDiscoveryTests(unittest.TestCase):
    def test_plain_requests_without_framework_names(self):
        cases = [
            ('像搭积木一样拖来拖去，把几个处理步骤连起来', 'tech-react-flow'),
            ('几个人同时改一份文档，断网后还能接着写', 'tech-yjs'),
            ('把一段产品介绍批量变成短视频', 'tech-remotion'),
            ('自动安排机器和工人的工作，不能撞时间', 'tech-ortools'),
            ('我把文档放进去，能问它问题，并告诉我根据哪段话', 'tech-llamaindex'),
            ('图片统一加上中文水印并缩放到指定宽度', 'tech-pillow'),
            ('做一个可以拖动旋转的产品展示', 'tech-threejs'),
            ('不同公司各自只能看到自己的资料', 'tech-supabase'),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                process, result = run_request(query)
                self.assertEqual(process.returncode, 0, process.stderr)
                self.assertIn(expected, tools(result))
                self.assertTrue(result['coding_handoff']['acceptance_observations'])

    def test_negated_3d_does_not_select_scene_engine(self):
        _, result = run_request('不要三维场景，只要折线图展示经营趋势')
        self.assertIn('tech-echarts', tools(result))
        self.assertNotIn('tech-threejs', tools(result))
        self.assertNotIn('tech-godot', tools(result))

    def test_unknown_request_does_not_invent_a_stack(self):
        _, result = run_request('我想做一个很好的应用')
        self.assertEqual(result['status'], 'needs_clarification')
        self.assertEqual(result['candidate_paths'], [])
        self.assertEqual(result['related_knowledge']['project'], [])
        self.assertTrue(result['questions_that_may_change_direction'])

    def test_explicit_tools_keep_requirements_open(self):
        _, result = run_request('我想用 React Flow')
        self.assertEqual(result['status'], 'named_tools_only')
        self.assertIn('tech-react-flow', {r['id'] for r in result['explicitly_named_technologies']})
        self.assertEqual(result['coding_handoff']['modules'], [])

    def test_project_dependency_is_declared_not_verified(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'package.json').write_text(json.dumps({'dependencies': {'@xyflow/react': '^12.0.0'}}))
            (root/'pnpm-lock.yaml').write_text('lockfileVersion: 9\n')
            _, result = run_request('拖动节点，把几个步骤连起来', '--project', folder)
            self.assertEqual(result['project_context']['lockfiles'], ['pnpm-lock.yaml'])
            candidate = next(r for option in result['candidate_paths'] for r in option['candidates']
                             if r['id'] == 'tech-react-flow')
            self.assertIn('@xyflow/react', candidate['declared_project_packages'])
            self.assertEqual(candidate['reuse_hint'], '先检查是否可复用')
            self.assertNotIn('installed', result['project_context'])

    def test_manifest_symlink_does_not_escape_project(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder);root = base/'project';root.mkdir()
            external = base/'external.json';external.write_text('{"dependencies":{"secret-package":"value"}}')
            (root/'package.json').symlink_to(external)
            _, result = run_request('给一个节点连线流程', '--project', str(root))
            self.assertEqual(result['project_context']['declared_dependencies'], {})
            self.assertTrue(result['project_context']['warnings'])

    def test_candidates_preserve_restrictions_and_evidence(self):
        _, result = run_request('上传文件，授权下载自己的附件')
        candidates = [r for option in result['candidate_paths'] for r in option['candidates']]
        minio = next(r for r in candidates if r['id'] == 'tech-minio')
        self.assertIn('限制使用', minio['adoption_note'])
        for r in candidates:
            self.assertTrue(r['source_refs'])
            self.assertTrue(r['validations'])
        self.assertIn('不安装', result['coding_handoff']['execution_boundary'])

    def test_bad_request_or_path_fails_without_mutation(self):
        result, payload = run_request(' ')
        self.assertEqual(result.returncode, 2)
        self.assertFalse(payload['ok'])
        result, payload = run_request('文件上传', '--project', '/not/a/real/project')
        self.assertEqual(result.returncode, 2)
        self.assertFalse(payload['ok'])

    def test_mapping_broken_reference_is_detected(self):
        data = kb.load(ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            p = root/'profiles.json'
            payload = {'schema_version': 1, 'profiles': [{'id': 'missing-scenario', 'match_groups': [['图表']],
                       'technologies': ['tech-nonexistent'], 'capabilities': [], 'template_ids': [],
                       'questions': ['什么需求？'], 'dataflow': ['输入'], 'acceptance': ['结果']}]}
            p.write_text(json.dumps(payload))
            data['discovery_profiles_path'] = 'profiles.json'
            errors = kb.discovery_module().validate_profiles(root, data)
            self.assertTrue(any('关联无效' in e for e in errors))
            self.assertTrue(any('未在目录登记' in e for e in errors))


if __name__ == '__main__':
    unittest.main(verbosity=2)
