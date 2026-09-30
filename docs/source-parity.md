# Workflow parity

This setup preserves the behavior used by the prior GD Math Godot runs while making the paths local to this project.

| Behavior | Local implementation |
|---|---|
| Exact source/runtime identity check | `scripts/preflight.py` |
| Fresh Xvfb display and bounded rendered-board probe | `scripts/deterministic_level_runner.py` |
| Native drag input | runner `drag()` using `xdotool` |
| X11 screenshot capture | runner `capture()` using ImageMagick `import` |
| Current-board mapping checkpoint | plan `initial_screenshot_sha256` and `live_mapping_verified` |
| One-action visual gate | `--one-action`, `--approve-action`, `--retry-action` |
| One bounded recovery | runner plan retry and `max_retries: 1` |
| Board-boundary and cleanup events | runner `events.jsonl` and `flow.md` |
| Backend provenance | plan and every runner event |
| Report/evidence validation | `scripts/validate_run.py` |
| No global skill installation | local `skills/` only |

The project intentionally does not copy the GD Math application, source configuration, BLC data, or historical run evidence. Those remain read-only external inputs selected in `config/target.json`; the test process, skills, templates, and durable evidence locations are isolated here.
