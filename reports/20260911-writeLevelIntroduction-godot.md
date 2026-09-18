# Direct Godot Retest Report — `writeLevelIntroduction`

- Run ID: `20260911-writeLevelIntroduction-godot`
- Date: 2026-09-11
- Level ID: `writeLevelIntroduction`
- Title: **Introducing Line Tracing**
- Target: Godot 4.6.1 desktop via Xvfb `:99`
- Renderer: Mesa llvmpipe
- Selector: `GDM_LEVEL_ID=writeLevelIntroduction`

## Level metadata

- Skill age: 3
- Branch: Geometry
- Status: `deviceTested`
- Tags: `intro|write|master|concept`
- Type: `icmV2`
- Variants: `characterTrace` → `numberTile`
- Configured board count: 1
- Configured board time: 14 seconds

## Result

**PASS — direct Godot desktop run**

The single configured board loaded, both vertical trace paths were completed, and the app transitioned to a visible completion/home state.

## Tested flow

1. **Initial board** — verified
   - Two vertical trace paths were visible.
   - Both prompts displayed `Standing Line`.
   - Evidence: `00_initial.png`

2. **Left trace** — accepted
   - Dragged from the top to the bottom of the left vertical path.
   - Evidence: `01_before_trace_left.png`, `02_after_trace_left.png`

3. **Right trace** — accepted
   - Dragged from the top to the bottom of the right vertical path.
   - Runtime output included `Well done! Keep going!`.
   - Evidence: `03_before_trace_right.png`, `04_after_trace_right.png`

4. **Completion** — verified
   - The trace board was replaced by the completion/home state.
   - Visible state included 40 coins and home, retry, next, and dice/navigation controls.
   - Because the configured board count is 1, this verifies full completion of the configured level in the direct Godot run.
   - Evidence: `05_final.png`, `06_final_wait.png`

## Checks

| Check | Result |
|---|---|
| Level ID/title | PASS |
| Board rendered | PASS |
| Trace paths visible | PASS |
| Left trace acceptance | PASS |
| Right trace acceptance | PASS |
| Completion transition | PASS |
| Full configured level completion | PASS — 1 of 1 board |
| Android rendering/touch | BLOCKED / not tested in this run |
| Invalid trace path | Not tested |
| Rapid/repeated trace | Not tested |
| Performance timing | Not tested |
| Audio heard directly | Not tested |

## Scope boundary

This is verified desktop Godot evidence only. It does not override the earlier Android result, where the APK rendered a black screen with `QueuePresentKHR failed with error: 5`.

## Evidence

Directory:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/writeLevelIntroduction-godot-20260911/`

- `00_initial.png`
- `01_before_trace_left.png`
- `02_after_trace_left.png`
- `03_before_trace_right.png`
- `04_after_trace_right.png`
- `05_final.png`
- `06_final_wait.png`

Journal:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/20260911-writeLevelIntroduction-godot.jsonl`
