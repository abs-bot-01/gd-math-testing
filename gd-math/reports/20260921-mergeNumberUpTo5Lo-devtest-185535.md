# QA Test Report

## Test Summary

**Status: FAIL — reproducible gameplay defect**

Target: `mergeNumberUpTo5Lo`  
Execution: Godot desktop under Xvfb `:1042`  
Run ID: `20260921-mergeNumberUpTo5Lo-devtest-185535`  
Build: `./buildMaker.sh devTesting main`, exit code `0`  
Godot: `4.6.1.stable.official.14d19694e`  
Project revision: `ec440927c38e6df093f03bc95e784125856911a8`  
Config revision: `4b95266f28f9c6b7412332195c23c19f71b43c51`

## Level Details

Source and runtime both contain the exact ID `mergeNumberUpTo5Lo`.

- Title: `Add 1 to Get Numbers Up to 5 - LO`
- Skill age: 5
- Branch: Arithmetic
- Type/parser: `icmV2`
- Variants: `numberTile` → `numberSlot`
- Configured boards: 10
- Board time: 27 seconds
- Mechanic: merge number tiles to construct `+1` results, then place each result into the matching number slot

## Coverage Summary

One desktop board was reached. Three merge/placement sequences were exercised on Board 1; two placements were accepted and one exposed the defect below. Full-level completion was not verified.

## Action-by-Action Testing

1. **Launch and render — verified.** The level title and a playable three-row board rendered after loader initialization. The board showed three animated brick platforms crossing parts of the destination rows. Evidence: `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_00_initial.png`.
2. **Merge `1 + 1` — verified.** The top-left `1` was dragged onto the top-middle `1`; both were consumed and a result `2` appeared. Before/after evidence: `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_01_before_merge_top.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_01_after_merge_top.png`.
3. **Place result `2` — verified.** The result `2` was paced around the animated obstacle and accepted by the bottom `2` slot; the tile was consumed and visible water-ripple feedback appeared. Before/after evidence: `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_02b_before_place_2_bottom.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_02b_after_place_2_bottom.png`.
4. **Merge `2 + 1` — verified.** The middle-left `2` was dragged onto a middle `1`; a result `3` appeared. Before/after evidence: `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_03_before_merge_2_1.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_03_after_merge_2_1.png`.
5. **Place result `3` — failed.** After dragging the result `3` to the top `3` slot, the source disappeared and a large rotated/oversized white tile rendered across the target. The slot remained unresolved; after a bounded four-second wait the malformed tile persisted. Before/after/wait evidence: `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_before_place_3.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_place_3.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_wait.png`.

## Screenshot Evidence

The retained screenshots above show the untouched Board 1 state, accepted merge/placement transitions, and the malformed top-slot result. All cited files are PNGs at 1280×720 and were verified non-empty.

## Final State

Board 1 remained unresolved: the top `3` slot was not visibly satisfied and loose `1` tiles remained. No board-completed or full-level-completed state was reached.

## Issues Found

### `mergeNumberUpTo5Lo-top-slot-placement-misrendered` — HIGH — NEW

**Expected:** Placing the constructed `3` into the top `3` slot should consume the result tile, satisfy the slot, and leave the board in a solvable state.  
**Actual:** The result disappeared from the work area but rendered as a large rotated/oversized white tile over the top slot; the slot stayed unresolved after four seconds. The top animated brick platform overlapped the destination area during the attempt.  
**Reproduction:** Launch with `DISPLAY=:1042 GDM_LEVEL_ID=mergeNumberUpTo5Lo godot --path /home/abs-bot-01/dev/gd-math-godot`; on Board 1 merge `2 + 1` to create `3`; drag the result to the top `3` slot using a paced path around the platform; wait four seconds.  
**Evidence:** `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_place_3.png`, `../runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_wait.png`.

### Runtime warning — LOW — KNOWN/OBSERVED

Godot logged invalid `ext_resource` UIDs for `tracingOutline.ttf` in `character.tscn`, `tile.tscn`, and `slot.tscn`, then fell back to text paths. The board still rendered. This is logged as a recurring runtime warning, not the gameplay failure.

## Level Result Summary

- Board 1: **FAIL / incomplete** — playable, but the top `3` placement produced a persistent malformed state.
- Boards 2–10: **NOT TESTED** — stopped after the reproducible Board 1 defect.
- Full level: **FAIL** — required 10-board completion was not achieved and a reproducible gameplay/rendering violation was observed.

## Overall Conclusion

The dev build and exact runtime level configuration passed preflight, and the target rendered as a playable desktop board. Core merge behavior and one result placement worked. The level cannot be marked dev-tested/pass because the next valid result placement consistently left the top slot unresolved with an oversized, rotated tile. The defect is linked to `mergeNumberUpTo5Lo-top-slot-placement-misrendered`; animated platform overlap is a plausible contributing condition but was not isolated.

## Missing Evidence / Not Tested

- Boards 2–10 and full-level completion.
- Safe invalid-placement coverage after the blocker.
- Monkey/repeated-interaction coverage after the blocker.
- Audio/TTS pronunciation and SFX verification.
- Android/device/touch behavior and mobile performance.
- Figma comparison and source status updates; no project YAML/status files were changed.
