"""Read-only, explainable business-language routing; not a semantic model or installer."""
import json
from pathlib import Path
import re
import argparse
import importlib.util

_spec = importlib.util.spec_from_file_location('hub_requirements', Path(__file__).with_name('requirements.py'))
requirements = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(requirements)

NEGATION = re.compile(r'(?:不需要|不要|不用|无需|不想|不做|排除|without\s+|no\s+|not\s+)(?:做|用|使用|任何|一个|一套|复杂的|的|\s)*$', re.I)
NEGATIVE_CLAUSE = re.compile(r'^(?:我|我们|暂时|现在|目前|这次|也|并|先|完全|明确|请|都|还)*(?:不需要|不要|不用|无需|不想|不做|排除|without\s|no\s|not\s)', re.I)
FUNCTIONAL_NEGATION = re.compile(r'^(?:我|我们|希望|要求|页面|系统|最好)*(?:不用刷新|不刷新|不用联网|不需要联网|不能撞|不能重叠|不冲突|不会丢失|不丢)', re.I)
SPLIT = re.compile(r'[，,。；;！？!?\n]|但是|而是|但|只要')
PACKAGE_HINTS = {
    'tech-react-flow': ['@xyflow/react', 'reactflow'], 'tech-react': ['react'],
    'tech-vue': ['vue'], 'tech-echarts': ['echarts'], 'tech-d3': ['d3'],
    'tech-g2': ['@antv/g2'], 'tech-tiptap': ['@tiptap/core', '@tiptap/react'],
    'tech-yjs': ['yjs'], 'tech-threejs': ['three'], 'tech-babylonjs': ['@babylonjs/core'],
    'tech-antd': ['antd'], 'tech-ag-grid': ['ag-grid-community', 'ag-grid-react'],
    'tech-tanstack-table': ['@tanstack/react-table'], 'tech-tanstack-query': ['@tanstack/react-query'],
    'tech-monaco': ['monaco-editor'], 'tech-codemirror': ['@codemirror/view', 'codemirror'],
    'tech-fastapi': ['fastapi'], 'tech-django': ['django'], 'tech-nestjs': ['@nestjs/core'],
    'tech-langgraph': ['langgraph'], 'tech-llamaindex': ['llama-index'],
    'tech-pandas': ['pandas'], 'tech-duckdb': ['duckdb'], 'tech-polars': ['polars'],
    'tech-ortools': ['ortools'], 'tech-supabase': ['@supabase/supabase-js'],
    'tech-remotion': ['remotion'], 'tech-playwright': ['@playwright/test', 'playwright'],
    'tech-vitest': ['vitest'], 'tech-react-native': ['react-native'], 'tech-electron': ['electron'],
}


def positive_hits(text, terms):
    """Return auditable positive phrases, excluding direct negative clauses."""
    hits = []
    for clause in SPLIT.split(text.casefold()):
        if NEGATIVE_CLAUSE.match(clause.strip()) and not FUNCTIONAL_NEGATION.match(clause.strip()):
            continue
        for term in terms:
            needle = term.casefold()
            for match in re.finditer(re.escape(needle), clause):
                if NEGATION.search(clause[:match.start()]):
                    continue
                if term not in hits:
                    hits.append(term)
    return hits


def profile_matches(text, profiles):
    output = []
    for profile in profiles:
        alternatives = [profile['match_groups']] + profile.get('alternative_match_groups', [])
        matched = [[positive_hits(text, terms) for terms in groups] for groups in alternatives]
        complete = [groups for groups in matched if groups and all(groups)]
        if not complete:
            continue
        groups = max(complete, key=lambda groups: sum(len(g) for g in groups))
        # Scores are rule evidence, never a calibrated probability.
        score = 10 * len(groups) + sum(min(len(g), 3) * 2 for g in groups)
        output.append((score, profile, groups))
    return sorted(output, key=lambda r: (-r[0], r[1]['id']))


def project_context(project):
    if project is None:
        return {'provided': False, 'declared_dependencies': {}, 'lockfiles': [], 'warnings': []}
    root = Path(project).expanduser().resolve()
    if not root.is_dir():
        raise ValueError('项目路径不存在或不是目录')
    dependencies, warnings = {}, []
    package = root / 'package.json'
    if package.exists():
        if not package.resolve().is_relative_to(root) or package.stat().st_size > 1_048_576:
            warnings.append('package.json 越界或超过读取上限，未读取')
        else:
            try:
                data = json.loads(package.read_text(encoding='utf-8'))
                for section in ('dependencies', 'devDependencies', 'peerDependencies'):
                    if isinstance(data.get(section), dict):
                        dependencies.update({k: str(v) for k, v in data[section].items()})
            except (OSError, ValueError, TypeError):
                warnings.append('package.json 无法解析；不能据此认定没有现有依赖')
    # Never execute project files or follow a symlink to an unrelated location.
    for name in ('requirements.txt', 'pyproject.toml'):
        path = root / name
        if not path.is_file():
            continue
        if not path.resolve().is_relative_to(root) or path.stat().st_size > 1_048_576:
            warnings.append(name + ' 越界或超过读取上限，未读取')
            continue
        content = path.read_text(encoding='utf-8')
        for aliases in PACKAGE_HINTS.values():
            for alias in aliases:
                if re.search(r'(?<![\w-])' + re.escape(alias) + r'(?=\s|[<>=!~\[\]"\x27,;]|$)', content):
                    dependencies.setdefault(alias, '文件中发现名称；版本与实际使用待核')
    locks = [name for name in ('package-lock.json', 'pnpm-lock.yaml', 'yarn.lock', 'bun.lock',
                               'bun.lockb', 'uv.lock', 'poetry.lock') if (root / name).is_file()]
    return {'provided': True, 'path': str(root), 'declared_dependencies': dependencies,
            'lockfiles': locks, 'warnings': warnings,
            'boundary': '只读取指定项目根目录中的相关清单；依赖声明不证明已安装或已运行'}


def public_record(root, record, sources):
    return {k: record.get(k) for k in ('id', 'title', 'summary', 'path', 'review_status',
                                      'outcome', 'validations', 'adoption_note')} | {
        'absolute_path': str((root / record['path']).resolve()),
        'evidence_kinds': sorted({sources[s]['kind'] for s in record.get('source_refs', []) if s in sources}),
        'source_refs': record.get('source_refs', []),
    }


def named_technologies(text, records):
    found = []
    for record in records.values():
        if record['kind'] != 'technology':
            continue
        terms = [record['id'].removeprefix('tech-'), record['title']]
        # Only explicit tool names enter this fallback, not generic type/capability aliases.
        for term in terms:
            if len(term) < 3:
                continue
            if positive_hits(text, [term]):
                found.append(record['id'])
                break
    return found


def discover(root, data, request, args, search_fn):
    request = request.strip()
    if not request:
        raise ValueError('需求描述不可为空')
    profiles_path = (root / data.get('discovery_profiles_path', 'data/discovery-profiles.json')).resolve()
    if not profiles_path.is_relative_to(root.resolve()):
        raise ValueError('需求场景路径越界')
    if not profiles_path.is_file():
        raise ValueError('业务场景映射缺失；请继续按能力词 search，不能声称已完成需求匹配')
    profiles = json.loads(profiles_path.read_text(encoding='utf-8'))['profiles']
    records = {r['id']: r for r in data['records']}
    sources = {s['id']: s for s in data['sources']}
    context = project_context(getattr(args, 'project_path', None))
    matches = profile_matches(request, profiles)
    interpretation = {'mode': 'phrase_hints', 'assumptions_to_confirm': [],
                      'boundary': '规则只是发现线索；未命中时由Codex解释意图，不要求用户提供技术名称。'}
    intent = getattr(args, 'intent', None)
    inline_intent = getattr(args, 'intent_json', None)
    if intent or inline_intent is not None:
        if inline_intent is not None and len(inline_intent.encode('utf-8')) > 65536:
            raise ValueError('需求解释超过64KiB上限')
        payload = json.loads(inline_intent) if inline_intent is not None else requirements.read_json(intent)
        interpretation = requirements.interpret(request, payload, profiles)
        by_id = {p['id']: p for p in profiles}
        matches = [(0, by_id[g['scenario_id']], [[g['source_quote']]]) for g in interpretation['goals']]
    selected = matches[:3]
    explicit = named_technologies(request, records)
    status = 'matched_scenarios' if selected else 'named_tools_only' if explicit else 'needs_clarification'
    scenarios, capability_ids, template_ids, technology_ids = [], [], [], list(explicit)
    options, acceptance, steps = [], [], []
    for score, profile, matched in selected:
        scenarios.append({'id': profile['id'], 'title': profile['title'], 'rule_score': score,
                          'matched_phrases': matched, 'path': records[profile['id']]['path']})
        capability_ids += profile['capabilities']
        template_ids += profile['template_ids']
        technology_ids += profile['technologies']
        acceptance += profile['acceptance']
        steps.append({'scenario': profile['title'], 'modules_and_dataflow': profile['dataflow']})
        choices = []
        for tid in profile['technologies']:
            record = public_record(root, records[tid], sources)
            declared = {p: context['declared_dependencies'][p] for p in PACKAGE_HINTS.get(tid, [])
                        if p in context['declared_dependencies']}
            choices.append(record | {'role': profile.get('technology_roles', {}).get(tid, record['summary']), 'declared_project_packages': declared,
                                     'reuse_hint': '先检查是否可复用' if declared else '尚无已检查的项目复用证据'})
        choices.sort(key=lambda c: not bool(c['declared_project_packages']))
        options.append({'business_need': profile['title'], 'decision': 'conditional_candidates',
                        'reuse_first': profile['reuse_first'], 'decision_boundary': profile['decision_boundary'], 'composition_rule': profile['composition_rule'],
                        'candidates': choices})
    def unique(ids):
        return list(dict.fromkeys(ids))
    capability_ids, template_ids = unique(capability_ids), unique(template_ids)
    if not selected and explicit:
        for tid in explicit:
            capability_ids += records[tid].get('capabilities', [])
        capability_ids = unique(capability_ids)
        template_ids = ['template-selection-brief', 'template-requirements']
    query = ' '.join([request] + [records[c]['title'] for c in capability_ids if c in records])
    def relevant(kind):
        if status == 'needs_clarification':
            return []
        filters = argparse.Namespace(kind=kind, project=None, capability=None, outcome=None,
                                     review_status=None, scope=None, result=None, evidence_kind=None, limit=3)
        return [public_record(root, r, sources) for r in search_fn(root, data, query, filters)['results']]
    questions = list(interpretation.get('open_questions', []))
    if selected:
        # Domain questions take priority over a technical project-path request.
        for _, profile, _ in selected:
            questions.extend(profile['questions'])
    elif explicit:
        questions.append('使用这些工具想完成什么用户任务，什么结果算成功？')
    elif positive_hits(request, ['3d', '三维']):
        questions += ['你希望在哪个软件或网页里完成什么操作：制作模型、查看产品，还是做仿真？',
                      '有没有现成模型或效果参考？可以直接描述希望看到和操作的样子。']
    else:
        questions += ['谁要完成什么操作，输入和期望结果分别是什么？',
                      '在哪种设备使用，是否需要多人、离线或外部数据？']
    questions = unique(questions)[:2]
    inventory = requirements.environment_inventory() if getattr(args, 'check_environment', False) else None
    paths = requirements.implementation_paths(root, data, [p['id'] for _, p, _ in selected], context, inventory)
    return {
        'request': request, 'status': status,
        'method': 'auditable phrase-group routing + catalog relations; not general semantic understanding',
        'scenarios': scenarios, 'matched_scenario_count': len(matches),
        'understanding': interpretation,
        'implementation_paths': paths,
        'environment_inventory': inventory,
        'agent_next_step': ('clarify_business_goal' if not selected else
                            'confirm_inferences_and_constraints' if interpretation.get('assumptions_to_confirm') else
                            'review_path_and_project_then_implement_if_authorized'),
        'additional_matches_not_expanded': [{'id': p['id'], 'title': p['title']} for _, p, _ in matches[3:]],
        'capabilities': [public_record(root, records[c], sources) for c in capability_ids],
        'candidate_paths': options,
        'explicitly_named_technologies': [public_record(root, records[t], sources) for t in explicit],
        'project_context': context, 'questions_that_may_change_direction': questions,
        'related_knowledge': {kind: relevant(kind) for kind in ('project', 'decision', 'experience')},
        'templates': [public_record(root, records[t], sources) for t in template_ids],
        'coding_handoff': {
            'status': 'needs_project_and_candidate_review' if status != 'needs_clarification' else 'insufficient_requirements',
            'business_request': request, 'modules': steps, 'acceptance_observations': unique(acceptance),
            'implementation_order': ['核实项目、用户改动和相关规则', '复用现有方案并查相关项目与失败经验',
                                     '针对缺口核查目标版本、许可、部署与费用', '只验证会改变选择的关键风险',
                                     '在已授权范围内实现并验收真实用户流程'],
            'execution_boundary': 'discover 只读，不安装、执行外部动作或自动生成项目；Codex 读取候选证据后完成选型和 Coding。',
        },
        'limits': ['规则未覆盖的表述应由 Codex 继续拆解并检索，不能当成没有成熟方案。',
                   '匹配分数不是采用概率；候选的维护、许可、PoC、项目集成与运行状态仍分别有效。',
                   '不同职责的候选可能需要组合，列表不是要求全部安装的技术栈。'],
    }


def format_discovery(result):
    lines = ['需求：' + result['request']]
    if result['status'] == 'needs_clarification':
        lines.append('暂未匹配到已编制场景。请补充用户任务；不据此生成技术栈。')
    else:
        lines.append('能力场景：' + '；'.join(s['title'] for s in result['scenarios']))
        for option in result['candidate_paths']:
            lines.append('\n' + option['business_need'] + '：')
            lines.append('  ' + option['reuse_first'])
            lines.append('  ' + option['composition_rule'])
            for c in option['candidates']:
                note = '；' + c['adoption_note'] if c.get('adoption_note') else ''
                lines.append('  候选：' + c['title'] + ' — ' + c['role'] + note)
        if result['explicitly_named_technologies']:
            lines.append('明确提及工具：' + '、'.join(r['title'] for r in result['explicitly_named_technologies']))
        if result['templates']:
            lines.append('\n可用模板：' + '、'.join(t['title'] for t in result['templates']))
        for path in result.get('implementation_paths', []):
            lines.append('\n实现路径：' + path['title'] + '；' + path['readiness'])
            for stage in path['stages']:
                lines.append('  ' + stage['name'] + ' → ' + stage['deliverable'])
        if result.get('understanding', {}).get('assumptions_to_confirm'):
            lines.append('待确认的理解：' + '；'.join(result['understanding']['assumptions_to_confirm']))
    lines.append('\n会改变方向的问题：')
    lines += ['- ' + q for q in result['questions_that_may_change_direction']]
    lines.append('\n' + result['coding_handoff']['execution_boundary'])
    return '\n'.join(lines)


def validate_profiles(root, data):
    errors = []
    location = data.get('discovery_profiles_path')
    if not location:
        return errors
    file = (root / location).resolve()
    if not file.is_relative_to(root.resolve()):
        return ['需求场景路径越界']
    try:
        payload = json.loads(file.read_text(encoding='utf-8'))
        if payload.get('schema_version') != 1:
            return ['需求场景 schema_version 无效']
        profiles = payload['profiles']
        records = {r['id']: r for r in data['records']}
        seen = set()
        for profile in profiles:
            pid = profile['id']
            if pid in seen:
                errors.append(pid + ': 场景 ID 重复')
            seen.add(pid)
            if records.get(pid, {}).get('kind') != 'scenario':
                errors.append(pid + ': 场景未在目录登记')
            groups = profile.get('match_groups')
            if not isinstance(groups, list) or not groups or any(
                not isinstance(g, list) or not g or any(not isinstance(t, str) or not t.strip() for t in g)
                for g in groups
            ):
                errors.append(pid + ': 匹配词组为空或类型无效')
            for alternative in profile.get('alternative_match_groups', []):
                if not isinstance(alternative, list) or not alternative or any(
                    not isinstance(group, list) or not group or any(not isinstance(t, str) or not t.strip() for t in group)
                    for group in alternative
                ):
                    errors.append(pid + ': 替代表述词组无效')
            for field, kind in [('capabilities', 'capability'), ('technologies', 'technology'),
                                ('template_ids', 'template')]:
                for rid in profile.get(field, []):
                    if records.get(rid, {}).get('kind') != kind:
                        errors.append(pid + ': ' + field + ' 关联无效 ' + rid)
            for field in ('questions', 'dataflow', 'acceptance'):
                if not profile.get(field):
                    errors.append(pid + ': 缺少 ' + field)
        registered = {r['id'] for r in data['records'] if r['kind'] == 'scenario'}
        for rid in sorted(registered - seen):
            errors.append(rid + ': 场景正文没有对应运行映射')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('需求场景文件无效: ' + str(exc))
    return errors + requirements.validate_paths(root, data)
