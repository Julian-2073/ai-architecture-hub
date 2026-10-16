"""Grounded Codex interpretations and implementation recipes; no model or installer."""
import json
from pathlib import Path
import shutil


def read_json(path, max_bytes=65536):
    path = Path(path)
    if path.stat().st_size > max_bytes:
        raise ValueError('需求解释文件超过64KiB上限')
    payload = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(payload, dict):
        raise ValueError('需求解释必须是JSON对象')
    return payload


def interpret(request, payload, profiles):
    """Validate provenance, not semantic truth. The Codex caller supplies understanding."""
    if not isinstance(payload, dict) or payload.get('schema_version') != 1:
        raise ValueError('需求解释 schema_version 必须为1')
    known = {p['id']: p for p in profiles}
    goals = payload.get('goals', [])
    excluded = payload.get('excluded_scenarios', [])
    if not isinstance(goals, list) or not isinstance(excluded, list) or len(goals) > 10 or len(excluded) > 10:
        raise ValueError('goals/excluded_scenarios 必须为不超过10项的数组')
    def grounded(item):
        if not isinstance(item, dict) or item.get('scenario_id') not in known:
            raise ValueError('需求解释引用了未知场景')
        quote = item.get('source_quote')
        if not isinstance(quote, str) or not quote.strip() or quote not in request:
            raise ValueError('需求解释必须引用本次原话中的非空片段')
        return item['scenario_id']
    goal_ids, excluded_ids = [], []
    for item in goals:
        goal_ids.append(grounded(item))
        if item.get('certainty') not in {'explicit', 'inferred'}:
            raise ValueError('需求解释必须区分 explicit 与 inferred')
    for item in excluded:
        excluded_ids.append(grounded(item))
    if len(set(goal_ids)) != len(goal_ids) or len(set(excluded_ids)) != len(excluded_ids):
        raise ValueError('需求解释包含重复场景')
    if set(goal_ids) & set(excluded_ids):
        raise ValueError('同一场景不能同时要求和排除')
    constraints = payload.get('known_constraints', [])
    if not isinstance(constraints, list) or len(constraints) > 12:
        raise ValueError('known_constraints 必须为不超过12项的数组')
    names = {'platform', 'assets', 'data_source', 'interaction', 'deployment', 'budget',
             'scale', 'privacy', 'persistence'}
    seen = set()
    for item in constraints:
        if not isinstance(item, dict) or item.get('name') not in names:
            raise ValueError('未知约束名称')
        if item['name'] in seen:
            raise ValueError('同一约束重复；冲突应作为待确认问题')
        seen.add(item['name'])
        if not isinstance(item.get('value'), str) or not item['value'].strip():
            raise ValueError('约束值必须为非空字符串')
        quote = item.get('source_quote')
        if not isinstance(quote, str) or not quote.strip() or quote not in request:
            raise ValueError('已知约束必须引用本次原话，不能将推测登记为已知')
    questions = payload.get('open_questions', [])
    if not isinstance(questions, list) or len(questions) > 2 or any(
        not isinstance(q, str) or not q.strip() for q in questions
    ):
        raise ValueError('open_questions 最多两个非空问题')
    return {
        'mode': 'codex_grounded_interpretation', 'goals': goals,
        'excluded_scenarios': excluded, 'known_constraints': constraints,
        'assumptions_to_confirm': [known[g['scenario_id']]['title'] for g in goals if g['certainty'] == 'inferred'],
        'open_questions': questions,
        'boundary': '解释由当前Codex提供；工具仅校验引用、枚举与冲突，不证明语义判断正确，也不调用额外模型。',
    }


def environment_inventory():
    """Only inspect executable paths; do not launch software or inspect user data."""
    tools = {}
    for name in ('python3', 'node', 'blender'):
        executable = shutil.which(name)
        if name == 'blender' and not executable:
            app = Path('/Applications/Blender.app/Contents/MacOS/Blender')
            executable = str(app) if app.is_file() else None
        tools[name] = {'executable_path': executable,
                       'status': 'executable_found_not_run' if executable else 'not_found_in_checked_locations'}
    return {'tools': tools, 'boundary': '仅检查PATH与标准应用位置；未启动软件、核验版本、插件、授权或实际可调用性。'}


def load_paths(root, data):
    location = data.get('implementation_paths_path')
    if not location:
        return []
    path = (root / location).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('实现路径文件越界')
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('schema_version') != 1 or not isinstance(payload.get('paths'), list):
        raise ValueError('实现路径格式无效')
    return payload['paths']


def implementation_paths(root, data, scenario_ids, context, inventory=None):
    records = {r['id']: r for r in data['records']}
    result = []
    for path in load_paths(root, data):
        if not set(path['scenario_ids']) & set(scenario_ids):
            continue
        # A verified reference is scoped to its own project/version/data, not this request.
        references = []
        for rid in path.get('verified_reference_ids', []):
            record = records[rid]
            validations = [v for v in record.get('validations', [])
                           if v['scope'] == 'project_integration' and v['result'] == 'passed']
            if validations:
                references.append({'id': rid, 'title': record['title'], 'validations': validations,
                                   'path': record['path'], 'boundary': path['reference_boundary']})
        result.append({**path, 'verified_references': references,
                       'readiness': 'reference_available_new_project_not_verified' if references else 'recipe_only_not_project_verified',
                       'project_path_checked': context.get('path'),
                       'environment_checked': inventory is not None,
                       'execution_status': 'not_executed',
                       'next_action': '先确认输入、项目环境和关键未知项，再由Codex按路径实施；命中不代表可以跳过这些检查。'})
    return result


def validate_paths(root, data):
    errors = []
    try:
        records = {r['id']: r for r in data['records']}
        sources = {s['id'] for s in data['sources']}
        seen = set()
        for path in load_paths(root, data):
            pid = path['id']
            if pid in seen:
                errors.append(pid + ': 实现路径重复')
            seen.add(pid)
            if records.get(pid, {}).get('kind') != 'template':
                errors.append(pid + ': 实现路径未登记为模板')
            for field in ('scenario_ids', 'source_refs', 'input_gates', 'stages', 'acceptance', 'fallback', 'reference_boundary'):
                if not path.get(field):
                    errors.append(pid + ': 实现路径缺少 ' + field)
            for rid in path.get('scenario_ids', []):
                if records.get(rid, {}).get('kind') != 'scenario':
                    errors.append(pid + ': 未知场景 ' + rid)
            for sid in path.get('source_refs', []):
                if sid not in sources:
                    errors.append(pid + ': 来源缺失 ' + sid)
            for rid in path.get('verified_reference_ids', []):
                if rid not in records or not any(v['scope'] == 'project_integration' and v['result'] == 'passed'
                                                for v in records[rid].get('validations', [])):
                    errors.append(pid + ': 所称已验证参考缺少项目集成通过证据 ' + rid)
            for stage in path.get('stages', []):
                if not isinstance(stage, dict) or not all(stage.get(f) for f in ('name', 'agent_action', 'deliverable', 'check')):
                    errors.append(pid + ': 阶段缺少动作、交付物或检查')
                for tid in stage.get('technology_options', []):
                    if records.get(tid, {}).get('kind') != 'technology':
                        errors.append(pid + ': 阶段引用未知技术 ' + tid)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('实现路径无效: ' + str(exc))
    return errors
