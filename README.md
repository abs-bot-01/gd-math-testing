# GD Math Godot Testing Setup for Pi-agent

This directory is a self-contained, project-local test harness for reproducing the GD Math Godot testing workflow used by the previous tester.

It deliberately does **not** install or modify system-level skills, Hermes profiles, Pi-agent configuration, application source, scenes, assets, or level data. Pi-agent should load the local skill files from `skills/` and keep all test state under this project.

## What is included

- `skills/gd-math-godot-testing/` — the complete level-testing procedure and references.
- `skills/native-x11-input/` — the input and screenshot backend contract.
- `skills/evidence-qa-reporting/` — journal, findings, report, and verification rules.
- `scripts/deterministic_level_runner.py` — plan-driven Godot runner using Xvfb, `xdotool`, and ImageMagick `import`.
- `scripts/preflight.py` — target/configuration/prerequisite checks.
- `scripts/new_run.py` — creates an isolated run directory and starter plan.
- `scripts/validate_run.py` — validates JSONL, report links, screenshots, and scope metadata.
- `docs/` — local evidence architecture, runbook, context retrieval, and Pi-agent instructions.
- `templates/` — plan, flow, report, and context-packet templates.
- `tester-data/` — isolated runs, reports, findings, issues, bugs, and knowledge state.

## Input policy

Gameplay input is native X11 input through `xdotool`. `computer_use` is not part of the default path. The agent maps the current board from a fresh screenshot, sends paced mouse events, captures the settled state, and visually verifies the result. A successful command exit is never treated as gameplay acceptance.

The channels are kept separate:

- input: `xdotool`;
- display and screenshots: Xvfb, `xdpyinfo`, ImageMagick `import`;
- visual review: Pi-agent vision or an explicit human review gate;
- orchestration: the local Python runner.

If an alternate backend is ever used, record it explicitly in the run metadata. Do not infer backend provenance from a tool catalog or an available-tool list.

## External prerequisites

The harness itself is local to this project. The machine still needs the actual runtime binaries:

- Python 3.11 or newer;
- Godot 4.x;
- `Xvfb`;
- `xdpyinfo`;
- `xdotool`;
- ImageMagick `import`.

Pillow and PyYAML are optional. The runner can perform its basic render probe without Pillow, while `preflight.py` uses a standard-library fallback when PyYAML is unavailable.

## Quick start

```bash
cd ~/dev/testing-setup
python3 scripts/preflight.py --config config/target.json --level-id <level-id>
python3 scripts/new_run.py --config config/target.json --level-id <level-id> --board-count <N>
```

The second command prints the created plan and run directory. Edit that plan only after inspecting the retained live screenshot and deriving the current source-to-target mapping.

Validate a plan without launching Godot:

```bash
python3 scripts/deterministic_level_runner.py \
  --plan tester-data/runs/<run-id>/plan.json \
  --dry-run
```

Prepare a live session:

```bash
python3 scripts/deterministic_level_runner.py \
  --plan tester-data/runs/<run-id>/plan.json \
  --run-dir tester-data/runs/<run-id> \
  --start-xvfb --prepare --retain-action-screenshots
```

Then inspect the current screenshot, fill the plan with live actions, add `initial_screenshot_sha256`, and set `live_mapping_verified: true`. Execute one action at a time when evidence review is required:

```bash
python3 scripts/deterministic_level_runner.py \
  --plan tester-data/runs/<run-id>/plan.json \
  --run-dir tester-data/runs/<run-id> \
  --execute --one-action --retain-action-screenshots
```

Approve only after visual review:

```bash
python3 scripts/deterministic_level_runner.py \
  --plan tester-data/runs/<run-id>/plan.json \
  --run-dir tester-data/runs/<run-id> \
  --execute --one-action --retain-action-screenshots \
  --approve-action <N>
```

Use `--retry-action <N>` once for a visibly rejected move. Do not use blind retries.

Validate the completed run:

```bash
python3 scripts/validate_run.py \
  --run-dir tester-data/runs/<run-id> \
  --report tester-data/reports/<run-id>.md
```

## Isolation guarantee

Persistent setup files belong below `~/dev/testing-setup`. The harness does not write to `~/.hermes/skills`, global Pi-agent directories, `/shared`, or the GD Math source/configuration repositories. Runtime evidence must use `tester-data/` inside this project. External application and configuration paths are read-only inputs supplied through `config/target.json`.

## Result discipline

Use these result classes:

- `PASS` — all requested boards/actions and final completion were visually verified;
- `FAIL` — the flow was playable but exposed a reproducible violation;
- `PARTIAL / INCOMPLETE` — some coverage exists but configured scope or completion is unfinished;
- `BLOCKED` — the requested gameplay was unreachable because of a prerequisite, launch, renderer, or target blocker;
- `NOT TESTED` — no claim is made for an unattempted scope.

A rendered board is not a completed level. A completed board is not a completed multi-board level. Android behavior is not claimed from a desktop run.
