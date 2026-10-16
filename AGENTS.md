# Architecture Hub repository instructions

- Read `docs/novice-workflow.md` when first using this hub. Understand the user's goal, operations, inputs and desired effect without requiring technology names.
- Locate this repository root, then invoke `python3 scripts/kb.py discover 'the original request' --json` from that root, or use the script's absolute path from any other working directory.
- Inspect only relevant returned cards, current project manifests and applicable experience. Reuse existing components first.
- Rule misses are not proof that no mature solution exists. Interpret the user's wording, search capabilities or scenarios, and provide a grounded `--intent-json` explanation when useful. Separate confirmed constraints and inferences.
- Ask only questions that materially change the direction. Explain why this architecture fits, alternatives' cost and conditions for reconsideration.
- Candidates and recipes are unverified until checked for the target version, license, environment and project. Use current primary sources for material technology decisions; run only decisive PoCs.
- `discover` is read-only. Continue implementation only within the user's authorization; review, test and retain evidence. A discussion or read-only task must not write knowledge back.
- Never commit credentials, personal paths, proprietary evidence or third-party webpage bodies. Keep source kinds and verification scopes separate; do not turn official descriptions into project success evidence.
- Before submitting repository changes run `python3 scripts/kb.py validate --strict` and relevant tests. Use `python3 -m unittest discover -s tests -v` for behavior or schema changes.
