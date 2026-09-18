# DevTesting Rerun Report — `mergeNumberUpTo7`

- Run ID: `20260910-devTesting-mergeNumberUpTo7-rerun`
- Date: 2026-09-10
- Target: `/home/abs-bot-01/dev/gd-math-godot`
- Requested level: `mergeNumberUpTo7`
- Scope: repeat build/readiness plus direct Godot live interaction testing

## Result

**PARTIALLY TESTED — gameplay board reached and interacted with; full level completion not verified.**

## Readiness and build

- Android readiness remains blocked: `adb devices -l` returned no devices, and the effective session lacks `kvm` membership.
- `./buildMaker.sh devTesting main` generated config and completed Godot reimport, but exited `128` when the config update attempted SSH `git pull --rebase` and failed host-key verification.
- The direct Godot run used the existing project/runtime assets with `GDM_LEVEL_ID=mergeNumberUpTo7` on Xvfb display `:99`.

## Level metadata — verified

- ID: `mergeNumberUpTo7`
- Title: **Add 1 to Get Numbers Up to 7**
- Skill age: 5
- Branch: Arithmetic
- Tags: `match|v1|representative`
- Type: `icmV2`
- Variants: `numberTile` → `numberSlot`
- Configured board count: 10
- Configured board time: 27 seconds

## Gameplay observations

### Board 1 — partially verified

- The requested title and a playable three-row board were visibly rendered.
- The board rule was exercised: merge a blue number tile with a red `1`, then place the generated result into the matching gray target slot.
- A correct merge visibly produced a result tile, and placement into a matching target was visibly accepted.
- The remaining rows were solved through live drags; after the effects settled, a new board was visible in `13_after_board_wait.png`.
- This verifies transition from the first board, not completion of the ten-board level.

### Board 2 — partially verified

- A second playable board was reached and remained visible.
- Multiple merge and placement actions were attempted with changing/generated tiles.
- The board continued to show unresolved target slots and no completion screen appeared during the run.
- The exact full solution for board 2 was not completed before stopping; no full-level completion claim is made.

## Checks

| Check | Result |
|---|---|
| App/project launch | **Verified** — Godot launched on Xvfb with llvmpipe |
| Requested level selected | **Verified** — runtime output and visible title showed `mergeNumberUpTo7` / Add 1 to Get Numbers Up to 7 |
| Board rendered | **Verified** |
| Merge interaction | **Verified for exercised rows** |
| Correct result placement | **Verified for exercised rows** |
| First-board transition | **Verified** |
| Full 10-board level completion | **Not tested / not completed** |
| Android installation/touch behavior | **Not tested — no authorized target** |
| Negative interaction matrix | **Not tested** |
| TTS/audio | **Not tested** |
| Performance/timing | **Not tested** |

## Evidence

Evidence directory:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/devTesting-mergeNumberUpTo7-20260910-rerun/`

Key files:

- `00_initial.png` — playable initial board
- `01_before_move.png`, `02_after_move.png` — first merge
- `04_before_result_placement.png`, `05_after_result_placement.png` — result placement
- `13_after_board_wait.png` — subsequent board after first-board interaction
- `14_board2_before_merge1.png` through `22_board2_after_final_placement.png` — board 2 interaction evidence
- `23_board2_before_merge4.png` through `31_stabilized.png` — additional board 2 interaction evidence

Journal:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/20260910-devTesting-mergeNumberUpTo7-rerun.jsonl`
