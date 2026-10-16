#!/usr/bin/env python3
"""Local, read-only knowledge search, business discovery and provenance validation. Python >=3.10."""
import argparse
from collections import Counter
from datetime import date, datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

KINDS = {'capability', 'technology', 'project', 'decision', 'experience', 'template', 'scenario'}
SOURCE_KINDS = {'official_statement', 'code_inspection', 'historical_test', 'current_test', 'inference'}
SCOPES = {'materials', 'version_license', 'poc', 'project_integration', 'runtime'}
RESULTS = {'passed', 'failed', 'partial', 'not_executed'}
REVIEWS = {'active', 'needs_review', 'superseded'}
ROOT = Path(__file__).resolve().parents[1]



_DISCOVERY = None


def discovery_module():
    global _DISCOVERY
    if _DISCOVERY is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location('hub_discovery', ROOT / 'scripts/discovery.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _DISCOVERY = module
    return _DISCOVERY


def load(root):
    data = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('catalog.json 必须使用 schema_version=1')
    if not isinstance(data.get('records'), list) or not isinstance(data.get('sources'), list):
        raise ValueError('records 和 sources 必须为数组')
    return data


def inside(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'知识文件路径越界: {value}')
    return path


def tokens(text):
    text = text.casefold()
    output = set(re.findall(r'[a-z0-9]+(?:[.+_-][a-z0-9]+)*', text))
    for segment in re.findall(r'[\u3400-\u9fff]+', text):
        output.update(segment[i:i+2] for i in range(len(segment)-1))
        if len(segment) == 1:
            output.add(segment)
    return output - {'我要', '想要', '一个', '需要', '系统', '可以', '怎么', '如何', '进行', '能够'}


def search(root, data, query, args):
    qt = tokens(query)
    capability_hits = set()
    for cid, aliases in data.get('capability_aliases', {}).items():
        if any(alias.casefold() in query.casefold() for alias in aliases):
            capability_hits.add(cid)
    sources = {s['id']: s for s in data['sources']}
    results = []
    for record in data['records']:
        if args.kind and record['kind'] != args.kind:
            continue
        if args.project and args.project not in record.get('projects', []) and args.project != record['id']:
            continue
        if args.capability and args.capability not in record.get('capabilities', []):
            continue
        if args.outcome and record.get('outcome') != args.outcome:
            continue
        if args.review_status and record.get('review_status') != args.review_status:
            continue
        validations = record.get('validations', [])
        if (args.scope or args.result) and not any(
            (not args.scope or v['scope'] == args.scope) and
            (not args.result or v['result'] == args.result) for v in validations
        ):
            continue
        evidence = [sources[s] for s in record.get('source_refs', []) if s in sources]
        if args.evidence_kind and not any(s['kind'] == args.evidence_kind for s in evidence):
            continue
        title = ' '.join([record['title'], record['id'], *record.get('aliases', [])]).casefold()
        summary = record.get('summary', '').casefold()
        body = inside(root, record['path']).read_text(encoding='utf-8').casefold()
        score = 0.0
        matched = []
        for token in sorted(qt):
            weight = 6 if token in title else 3 if token in summary else 0.45 if token in body else 0
            if weight:
                score += weight
                matched.append(token)
        caps = sorted(set(record.get('capabilities', [])) & capability_hits)
        score += len(caps) * 8
        if query.casefold() in title:
            score += 20
        if score <= 0:
            continue
        results.append({**record, 'score': round(score, 2), 'matched_terms': matched,
                        'matched_capabilities': caps, 'absolute_path': str(inside(root, record['path'])),
                        'evidence_kinds': sorted({s['kind'] for s in evidence})})
    results.sort(key=lambda r: (-r['score'], r['id']))
    return {'query': query, 'method': 'weighted lexical + capability aliases; not semantic search',
            'total_matches': len(results), 'results': results[:args.limit]}


def catalog_today(data, now=None):
    """Compare date-only records using their declared recording offset, not host TZ."""
    offset = data.get('date_utc_offset')
    if offset is None:
        return date.today()
    match = re.fullmatch(r'([+-])(\d{2}):(\d{2})', offset) if isinstance(offset, str) else None
    if not match or int(match[2]) > 23 or int(match[3]) > 59:
        raise ValueError('date_utc_offset 必须是有效的 ±HH:MM')
    minutes = (int(match[2]) * 60 + int(match[3])) * (1 if match[1] == '+' else -1)
    zone = timezone(timedelta(minutes=minutes))
    current = now if now is not None else datetime.now(timezone.utc)
    if current.tzinfo is None:
        raise ValueError('用于日期校验的时间必须包含时区')
    return current.astimezone(zone).date()


def validate(root, data, check_origins=False):
    errors, warnings = [], []
    records, sources = data['records'], data['sources']
    if not all(isinstance(x, dict) for x in records + sources):
        return {'ok': False, 'errors': ['records/sources 条目必须为对象'], 'warnings': [], 'counts': {}}
    ids = [r.get('id') for r in records]
    sids = [s.get('id') for s in sources]
    for label, values in [('记录', ids), ('来源', sids)]:
        for key, n in Counter(values).items():
            if not isinstance(key, str) or not re.fullmatch(r'[a-z][a-z0-9-]*', key):
                errors.append(f'{label} ID 非法: {key}')
            if n > 1:
                errors.append(f'{label} ID 重复: {key}')
    record_map = {r.get('id'): r for r in records}
    source_map = {s.get('id'): s for s in sources}
    today = catalog_today(data)

    def valid_date(value, context):
        try:
            parsed = date.fromisoformat(value)
            if parsed > today:
                warnings.append(f'{context}: 日期晚于目录时区的当前日期 {value}')
        except (ValueError, TypeError):
            errors.append(f'{context}: 日期无效 {value}')

    for source in sources:
        sid = source.get('id')
        if source.get('kind') not in SOURCE_KINDS:
            errors.append(f'{sid}: 来源类型非法')
        for field in ('captured_at', 'version', 'note'):
            if not source.get(field):
                errors.append(f'{sid}: 缺少 {field}')
        valid_date(source.get('captured_at'), sid)
        if source.get('source_date') is not None:
            valid_date(source.get('source_date'), sid)
        elif not source.get('date_note'):
            errors.append(f'{sid}: 来源日期未知时必须填写 date_note')
        if not source.get('origin_path') and not source.get('origin_url'):
            errors.append(f'{sid}: 缺少原始位置')
        try:
            snapshot = inside(root, source['snapshot'])
            if not snapshot.is_file():
                errors.append(f'{sid}: 快照文件缺失')
            elif hashlib.sha256(snapshot.read_bytes()).hexdigest() != source.get('snapshot_sha256'):
                errors.append(f'{sid}: 快照 SHA256 不匹配')
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f'{sid}: 快照路径非法 {exc}')
        if source.get('kind') == 'current_test':
            if not source.get('command') or not isinstance(source.get('exit_code'), int):
                errors.append(f'{sid}: 本次实测必须记录 command 和 exit_code')
        if check_origins and source.get('origin_path'):
            origin = Path(source['origin_path'])
            if not origin.is_absolute():
                origin = inside(root, str(origin))
            if not origin.is_file():
                warnings.append(f'{sid}: 原文件不可访问，已保留本地快照')
            elif hashlib.sha256(origin.read_bytes()).hexdigest() != source.get('origin_sha256'):
                warnings.append(f'{sid}: 原文件已变化，复用前需复核')

    paths = []
    for record in records:
        rid = record.get('id')
        for field in ('title', 'summary', 'path', 'reviewed_at', 'review_status'):
            if not record.get(field):
                errors.append(f'{rid}: 缺少 {field}')
        if record.get('kind') not in KINDS:
            errors.append(f'{rid}: 记录类型非法')
        if record.get('review_status') not in REVIEWS:
            errors.append(f'{rid}: 复核状态非法')
        valid_date(record.get('reviewed_at'), rid)
        refs = record.get('source_refs', [])
        if not refs:
            errors.append(f'{rid}: 必须关联来源，建议和推断也需要来源记录')
        for sid in refs:
            if sid not in source_map:
                errors.append(f'{rid}: 来源不存在 {sid}')
        for field, kind in [('capabilities', 'capability'), ('technologies', 'technology'), ('projects', 'project')]:
            for target in record.get(field, []):
                if target not in record_map or record_map[target].get('kind') != kind:
                    errors.append(f'{rid}: {field} 关联不存在或类型错误 {target}')
        for field in ('related', 'supersedes', 'conflicts_with'):
            for target in record.get(field, []):
                if target not in record_map:
                    errors.append(f'{rid}: {field} 关联不存在 {target}')
                if target == rid:
                    errors.append(f'{rid}: {field} 不允许自引用')
        for v in record.get('validations', []):
            scope, result = v.get('scope'), v.get('result')
            if scope not in SCOPES or result not in RESULTS:
                errors.append(f'{rid}: 验证范围或结果非法')
            if v.get('as_of') is not None:
                valid_date(v.get('as_of'), f'{rid}/{scope}')
            elif not v.get('date_note'):
                errors.append(f'{rid}/{scope}: 验证日期未知时必须填写 date_note')
            evs = v.get('source_refs', [])
            if result != 'not_executed' and not evs:
                errors.append(f'{rid}/{scope}: 已执行结果缺少证据')
            if not set(evs).issubset(refs):
                errors.append(f'{rid}/{scope}: 验证证据未纳入记录来源')
            if scope in {'poc', 'project_integration', 'runtime'} and result != 'not_executed':
                tests = [source_map.get(s, {}) for s in evs
                         if source_map.get(s, {}).get('kind') in {'historical_test', 'current_test'}]
                if not tests:
                    errors.append(f'{rid}/{scope}: 执行验证不能仅由官方说明、代码检查或推断支持')
                if not v.get('data_nature') or not v.get('version'):
                    errors.append(f'{rid}/{scope}: 缺少 data_nature 或 version')
                if v.get('recency') not in {'historical', 'current'}:
                    errors.append(f'{rid}/{scope}: 缺少历史/本次标记')
                if v.get('recency') == 'current' and not any(s.get('kind') == 'current_test' for s in tests):
                    errors.append(f'{rid}/{scope}: 历史证据不能标为本次实测')
                if result == 'passed' and v.get('recency') == 'current' and not any(
                    s.get('kind') == 'current_test' and s.get('exit_code') == 0 for s in tests
                ):
                    errors.append(f'{rid}/{scope}: 本次通过缺少退出码为 0 的实测')
        try:
            path = inside(root, record['path'])
            paths.append(str(path))
            if not path.is_file():
                errors.append(f'{rid}: 正文文件缺失')
                continue
            content = path.read_text(encoding='utf-8')
            if not content.strip():
                errors.append(f'{rid}: 正文为空')
            for link in re.findall(r'\]\(([^\n)]+)\)', content):
                target = unquote(link.strip('<>').split('#', 1)[0])
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                target = re.sub(r':\d+$', '', target)
                if not (path.parent / target).exists():
                    errors.append(f'{rid}: 本地正文链接失效 {link}')
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f'{rid}: 正文路径非法 {exc}')
    for value, n in Counter(paths).items():
        if n > 1:
            errors.append(f'正文路径重复: {value}')
    for path in (root / 'knowledge').rglob('*.md'):
        if str(path.resolve()) not in paths:
            errors.append(f'正文未登记: {path.relative_to(root)}')
    expected = data.get('seed_expectations', {})
    for rid in expected.get('required_ids', []):
        if rid not in record_map:
            errors.append(f'首批记录缺失: {rid}')
    for kind, count in expected.get('minimum_counts', {}).items():
        if sum(r.get('kind') == kind for r in records) < count:
            errors.append(f'{kind}: 少于首批要求 {count}')
    for capability in data.get('capability_aliases', {}):
        if capability not in record_map or record_map[capability].get('kind') != 'capability':
            errors.append(f'能力别名指向无效能力: {capability}')
    errors.extend(discovery_module().validate_profiles(root, data))
    return {'ok': not errors, 'counts': dict(Counter(r.get('kind') for r in records)),
            'sources': len(sources), 'errors': errors, 'warnings': warnings,
            'boundary': '结构、文件完整性与证据类型校验；不证明文字真实、外部网页可用、许可有效或历史测试已复验'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='知识库目录，默认脚本所在知识库')
    commands = parser.add_subparsers(dest='command', required=True)
    query = commands.add_parser('search', help='按自然语言关键词、能力别名和正文检索')
    query.add_argument('query')
    query.add_argument('--kind', choices=sorted(KINDS))
    query.add_argument('--project', help='项目稳定 ID')
    query.add_argument('--capability', help='能力稳定 ID')
    query.add_argument('--outcome', choices=['success', 'failed', 'partial', 'not_executed'])
    query.add_argument('--review-status', choices=sorted(REVIEWS))
    query.add_argument('--evidence-kind', choices=sorted(SOURCE_KINDS))
    query.add_argument('--scope', choices=sorted(SCOPES))
    query.add_argument('--result', choices=sorted(RESULTS))
    query.add_argument('--limit', type=int, default=8)
    query.add_argument('--json', action='store_true')
    discover_cmd = commands.add_parser('discover', help='把业务口语映射到能力、技术候选与 Coding 交接')
    discover_cmd.add_argument('query')
    discover_cmd.add_argument('--project', dest='project_path', type=Path, help='只读检查指定项目根目录相关依赖清单')
    intent_group = discover_cmd.add_mutually_exclusive_group()
    intent_group.add_argument('--intent', type=Path, help='Codex从用户原话提炼的有引用JSON文件；不要求用户填写')
    intent_group.add_argument('--intent-json', help='直接传入有引用的JSON解释，无需写文件；只读讨论也可用')
    discover_cmd.add_argument('--check-environment', action='store_true', help='只检查本地工具路径，不启动或安装软件')
    discover_cmd.add_argument('--json', action='store_true')
    check = commands.add_parser('validate', help='校验目录、引用、快照与证据类型边界')
    check.add_argument('--check-origins', action='store_true', help='检查原文件是否缺失或变化，不访问网络')
    check.add_argument('--strict', action='store_true', help='将来源变化等警告计为失败')
    check.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    try:
        data = load(args.root)
        if args.command == 'search':
            if not args.query.strip() or not 1 <= args.limit <= 100:
                raise ValueError('query 不可为空，limit 必须为 1–100')
            output = search(args.root, data, args.query, args)
        elif args.command == 'discover':
            output = discovery_module().discover(args.root, data, args.query, args, search)
        else:
            output = validate(args.root, data, args.check_origins)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        if args.json:
            print(json.dumps({'ok': False, 'error': str(exc)}, ensure_ascii=False))
        else:
            print(f'错误: {exc}', file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    elif args.command == 'search':
        print(f'匹配 {output["total_matches"]} 条，显示 {len(output["results"])} 条。关键词与能力别名检索。')
        for r in output['results']:
            print(f'\n[{r["id"]}] {r["title"]} | {r["kind"]} | {r["score"]}')
            print(r['summary'])
            print('证据: ' + ', '.join(r['evidence_kinds']) + '；复核: ' + r['review_status'])
            for v in r.get('validations', []):
                print(f'  {v["scope"]}: {v["result"]} / {v.get("recency", "资料层面")} / {v["as_of"]}')
            print(r['absolute_path'])
    elif args.command == 'discover':
        print(discovery_module().format_discovery(output))
    else:
        print(('通过' if output['ok'] else '失败') + ': ' + json.dumps(output['counts'], ensure_ascii=False))
        for label in ('errors', 'warnings'):
            for message in output[label]:
                print(f'{label}: {message}')
        print(output['boundary'])
    if args.command == 'validate':
        return 0 if output['ok'] and not (args.strict and output['warnings']) else 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
