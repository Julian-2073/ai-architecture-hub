#!/usr/bin/env python3
"""Install only the optional local Skill, refusing existing destinations."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', required=True, type=Path,
                        help='Explicit Codex skills directory; writes architecture-hub underneath')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    target = args.skills_dir.expanduser().resolve() / 'architecture-hub'
    if target.exists() or target.is_symlink():
        print('Refusing to overwrite existing Skill: ' + str(target), file=sys.stderr)
        return 1
    template = ROOT / 'skills/architecture-hub/SKILL.md'
    if not (ROOT / 'catalog.json').is_file() or not template.is_file():
        print('Hub or Skill template is missing', file=sys.stderr)
        return 1
    print(json.dumps({'hub_root': str(ROOT), 'destination': str(target),
                      'dry_run': args.dry_run, 'files': ['SKILL.md', 'hub-location.json']}, ensure_ascii=False))
    if args.dry_run:
        return 0
    # An atomic directory claim also refuses a destination created after the check.
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        target.mkdir()
    except FileExistsError:
        print('Destination appeared; no files were overwritten', file=sys.stderr)
        return 1
    (target / 'SKILL.md').write_text(template.read_text(encoding='utf-8'), encoding='utf-8')
    (target / 'hub-location.json').write_text(json.dumps({'root': str(ROOT)}, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Installed. Open a new Codex chat and verify actual invocation separately.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
