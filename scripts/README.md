# Local scripts

- `preflight.py` — verify target paths, exact source/runtime level identity, commands, display state, and backend metadata without launching.
- `new_run.py` — create `tester-data/runs/<run-id>/plan.json`, `events.jsonl`, `flow.md`, `context-packet.md`, and evidence directories.
- `deterministic_level_runner.py` — run the two-phase Godot/Xvfb flow with native `xdotool` input and screenshots.
- `validate_run.py` — validate JSONL, report links, screenshots, cleanup, backend fields, and scope markers.

All scripts are stdlib-only at runtime. Optional Pillow/PyYAML support is listed in `requirements.txt`.
