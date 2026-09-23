# QA Test Report

## Test Summary

- **Run ID:** `20260922-mergeNumberUpTo5-normal-one-board-1457`
- **Target:** `mergeNumberUpTo5` (normal; not the LO variant)
- **Scope:** Complete exactly one board.
- **Environment:** Godot 4.6.1, Linux/X11 Xvfb `:1059`, 1280×720, Mesa llvmpipe.
- **Overall result:** **PASS — 1 board completed**

## Level Details

- **Title:** Add 1 to Get Numbers Up to 5
- **Type:** `icmV2`
- **Variants:** `numberTile` → `numberSlot`
- **Configured boards:** 10; only Board 1 was tested.
- **Authoritative source:** `/home/abs-bot-01/dev/gd-math-config/data/yamlFiles/levels.yaml:12196`
- **Runtime source:** `/home/abs-bot-01/dev/gd-math-godot/assets/config.json`

## Action-by-Action Testing

1. **Launch and render — VERIFIED**
   - Board 1 rendered with three arithmetic rows and three matching slots.
   - Evidence: `../runs/20260922-mergeNumberUpTo5-normal-one-board-1457/artifacts/board_initial.png`

2. **Merge results — VERIFIED**
   - `1+1=2`, `2+1=3`, and `4+1=5` all produced stable result tiles.
   - Evidence: `after_merge_top_wait5.png`, `after_merge_middle.png`, `after_all_merges.png`.

3. **Place results — VERIFIED**
   - `2` accepted by the middle `2` slot.
   - `3` accepted by the bottom `3` slot.
   - `5` accepted by the top `5` slot.
   - Evidence: `after_place_2.png`, `after_place_3.png`, `after_place_5.png`.

4. **Board completion — VERIFIED**
   - Completion feedback appeared; after settling, a new board was visible, confirming Board 1 completion.
   - Evidence: `after_place_5.png` and `final_wait.png`.

## Final State

- **Board 1:** Completed, 3/3 result placements accepted.
- **Board 2:** Not tested; it appeared only as the automatic post-completion transition.

## Issues Found

- None during the requested normal-level one-board run.

## Overall Conclusion

`mergeNumberUpTo5` normal Board 1 rendered, all three merges succeeded, all three results were accepted by their matching slots, and the game advanced to the next board. The requested one-board scope is complete.

## Missing Evidence / Untested Coverage

- Boards 2–10 were not tested by request scope.
- Audio, invalid interactions, hints, and performance were not separately tested.
