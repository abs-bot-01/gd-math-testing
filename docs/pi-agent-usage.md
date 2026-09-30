# Using this setup from Pi-agent

Pi-agent should treat `testing-setup` as the working project and read local skills from its `skills/` directory. No global plugin, skill, or profile installation is required.

## Start of a test

```text
Read:
- AGENTS.md if present; otherwise pi-agent/TESTING_INSTRUCTIONS.md
- skills/gd-math-godot-testing/SKILL.md
- skills/native-x11-input/SKILL.md
- skills/evidence-qa-reporting/SKILL.md
- docs/deterministic-level-testing.md
- docs/architecture.md
```

This setup intentionally has no global `AGENTS.md`; use `pi-agent/TESTING_INSTRUCTIONS.md` in this isolated project.

## Agent/tool division

- Pi-agent reasons about the current board and writes the live plan.
- `scripts/deterministic_level_runner.py` owns mechanical timing, Xvfb lifecycle, native input, screenshots, event writing, and bounded retry enforcement.
- Pi-agent or a human reviews screenshots and decides approve/retry/stop.
- `scripts/validate_run.py` checks the final artifact contract.

Do not hide a visual acceptance decision inside an unconditional script. Do not claim that a runner status is a semantic PASS without reviewing the visible terminal state.

## Long runs

Split long multi-board tests into resumable board batches. Checkpoint the plan, event stream, flow, and partial report after each batch. If the agent turn ends, leave a readable `PARTIAL / INCOMPLETE` report rather than restarting with stale coordinates.
