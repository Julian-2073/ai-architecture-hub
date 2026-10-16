"""Public retrieval and evidence boundaries; private projects are not test fixtures."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('kb', ROOT / 'scripts/kb.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


def options(**kw):
    values = dict(kind=None, project=None, capability=None, outcome=None,
                  review_status=None, scope=None, result=None, evidence_kind=None, limit=8)
    values.update(kw)
    return argparse.Namespace(**values)


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = kb.load(ROOT)

    def test_cross_domain_scenarios(self):
        for query, expected in [('表格 合并 汇总', 'scenario-spreadsheet-analysis'),
                                ('机器 工人 安排 不冲突', 'scenario-resource-scheduling'),
                                ('公司 文档 回答 出处', 'scenario-rag-answers')]:
            with self.subTest(query=query):
                results = kb.search(ROOT, self.data, query, options(kind='scenario', limit=10))['results']
                self.assertIn(expected, {r['id'] for r in results})

    def test_scope_filter_does_not_inherit_material_status(self):
        data = copy.deepcopy(self.data)
        rec = next(r for r in data['records'] if r['id'] == 'tech-threejs')
        rec['validations'][0]['result'] = 'partial'
        result = kb.search(ROOT, data, 'Three.js 三维', options(kind='technology', scope='poc', result='partial'))
        self.assertEqual(result['results'], [])

    def test_no_match_is_empty(self):
        self.assertEqual(kb.search(ROOT, self.data, 'zxqv987654321', options())['total_matches'], 0)

    def test_stable_result_order(self):
        self.assertEqual(kb.search(ROOT, self.data, '预测 模型', options()),
                         kb.search(ROOT, self.data, '预测 模型', options()))

    def test_capability_filter(self):
        results = kb.search(ROOT, self.data, '多人协同 离线冲突',
                            options(kind='technology', capability='cap-domain-editors-collaboration'))['results']
        self.assertEqual(results[0]['id'], 'tech-yjs')

    def test_template_cli(self):
        for query, expected in [('成本估算 预算', 'template-cost-model'), ('迁移 回退', 'template-migration')]:
            process = subprocess.run([sys.executable, str(ROOT/'scripts/kb.py'), 'search', query,
                                      '--kind', 'template', '--json'],capture_output=True,text=True,check=True)
            self.assertEqual(json.loads(process.stdout)['results'][0]['id'], expected)

    def test_public_catalog_claims_no_execution_success(self):
        for r in self.data['records']:
            self.assertTrue(all(v['result'] == 'not_executed' for v in r['validations']))
        self.assertEqual(kb.search(ROOT,self.data,'三维',options(scope='poc',result='passed'))['results'],[])

    def test_failure_writeback_is_retrievable(self):
        # A synthetic metadata fixture tests retrieval only; it is not a published project result.
        data = copy.deepcopy(self.data)
        fixture = copy.deepcopy(next(r for r in data['records'] if r['id'] == 'tech-ortools'))
        fixture.update(id='exp-fixture-failed',kind='experience',title='合成测试夹具：排程约束失败',
                       summary='演示失败经验如何影响检索；不是实际工程结论',outcome='failed')
        data['records'].append(fixture)
        result = kb.search(ROOT,data,'排程 约束',options(kind='experience',outcome='failed'))
        self.assertEqual(result['results'][0]['id'],'exp-fixture-failed')
        self.assertEqual(kb.search(ROOT,self.data,'排程',options(kind='experience'))['results'],[])

    def test_cli_invalid_input(self):
        proc=subprocess.run([sys.executable,str(ROOT/'scripts/kb.py'),'search','','--json'],capture_output=True,text=True)
        self.assertEqual(proc.returncode,2)
        self.assertFalse(json.loads(proc.stdout)['ok'])


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data=kb.load(ROOT)

    def find(self,rid='tech-threejs'):
        return next(r for r in self.data['records'] if r['id']==rid)

    def assert_error(self,fragment):
        report=kb.validate(ROOT,self.data)
        self.assertFalse(report['ok'])
        self.assertTrue(any(fragment in e for e in report['errors']),report)

    def test_complete_public_catalog(self):
        report=kb.validate(ROOT,self.data,True)
        self.assertTrue(report['ok'],report)
        self.assertEqual(report['warnings'],[])
        self.assertEqual(report['counts']['technology'],180)
        self.assertEqual(report['counts']['capability'],52)
        self.assertEqual(report['counts']['scenario'],45)
        self.assertNotIn('project',report['counts'])

    def test_official_description_cannot_prove_runtime(self):
        r=self.find();sid=r['source_refs'][0]
        next(s for s in self.data['sources'] if s['id']==sid)['kind']='official_statement'
        r['validations'].append({'scope':'runtime','result':'passed','source_refs':[sid],
                                'as_of':'2026-10-17','recency':'current','version':'fixture','data_nature':'synthetic'})
        self.assert_error('执行验证不能仅由官方说明')

    def test_historical_result_cannot_be_current(self):
        r=self.find();sid=r['source_refs'][0]
        next(s for s in self.data['sources'] if s['id']==sid)['kind']='historical_test'
        r['validations'].append({'scope':'poc','result':'passed','source_refs':[sid],
                                'as_of':'2026-10-17','recency':'current','version':'fixture','data_nature':'synthetic'})
        self.assert_error('历史证据不能标为本次实测')

    def test_missing_source(self):
        self.find()['source_refs'].append('src-missing')
        self.assert_error('来源不存在')

    def test_tampered_snapshot(self):
        self.data['sources'][0]['snapshot_sha256']='0'*64
        self.assert_error('快照 SHA256 不匹配')

    def test_duplicate_record(self):
        self.data['records'].append(copy.deepcopy(self.data['records'][0]))
        self.assert_error('ID 重复')

    def test_wrong_relation_type(self):
        self.find()['technologies'].append('cap-ui')
        self.assert_error('类型错误')

    def test_path_escape_rejected(self):
        self.find()['path']='../outside.md'
        self.assert_error('路径越界')

    def test_origin_missing_is_explicit_warning(self):
        self.data['sources'][0]['origin_path']='evidence/nonexistent.md'
        report=kb.validate(ROOT,self.data,True)
        self.assertTrue(report['ok'],report)
        self.assertTrue(any('原文件不可访问' in w for w in report['warnings']))

    def test_origin_changed_is_explicit_warning(self):
        self.data['sources'][0]['origin_sha256']='0'*64
        report=kb.validate(ROOT,self.data,True)
        self.assertTrue(report['ok'],report)
        self.assertTrue(any('原文件已变化' in w for w in report['warnings']))

    def test_moved_library_works_from_another_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            dest=Path(folder)/'copied hub'
            shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','__pycache__'))
            cmd=[sys.executable,str(dest/'scripts/kb.py')]
            result=subprocess.run(cmd+['validate','--check-origins','--strict','--json'],
                                  cwd=folder,capture_output=True,text=True,check=True)
            self.assertTrue(json.loads(result.stdout)['ok'])
            result=subprocess.run(cmd+['search','离线 表格','--json'],cwd=folder,capture_output=True,text=True,check=True)
            record=json.loads(result.stdout)['results'][0]
            self.assertTrue(Path(record['absolute_path']).is_relative_to(dest.resolve()))


if __name__=='__main__':unittest.main(verbosity=2)
