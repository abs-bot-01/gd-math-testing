# QA Test Report

## Test Summary

- **Run ID:** `20260922-mergeNumberUpTo5Lo-one-board-1442`
- **Target:** `mergeNumberUpTo5Lo`
- **Scope:** Complete exactly one board.
- **Environment:** Godot 4.6.1, Linux/X11 Xvfb `:1058`, 1280×720, Mesa llvmpipe.
- **Overall result:** **BLOCKED / NOT COMPLETED**
- **Configured boards:** 10
- **Boards requested:** 1
- **Boards completed:** 0

## Level Details

- **Title:** Add 1 to Get Numbers Up to 5 - LO
- **Skill age:** 5
- **Branch:** Arithmetic
- **Type:** `icmV2`
- **Variants:** `numberTile` → `numberSlot`
- **Extensions:** `mergeAndFillBase`, `mergeNumberUpTo5`, `alternatingStrikersBars`, `age5Drops`
- **Authoritative source:** `/home/abs-bot-01/dev/gd-math-config/data/yamlFiles/levels.yaml:12234`
- **Runtime source:** `/home/abs-bot-01/dev/gd-math-godot/assets/config.json`

## Action-by-Action Testing

### Board 1 — rendered, merged, then blocked

1. **Launch and render — VERIFIED**
   - The requested level title and playable board rendered.
   - ![Initial board](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/initial.png)
   - **Expected:** The requested LO board renders.
   - **Actual:** Board 1 rendered with three source tiles, three `+1` addends, three target slots, and moving brick obstacles.
   - **Result:** PASS.

2. **Three merges — VERIFIED**
   - `4 + 1 = 5` (top), `1 + 1 = 2` (middle), and `4 + 1 = 5` (bottom) all completed.
   - Before/after evidence: [top before](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/before_merge_top.png), [top after](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_merge_top.png), [middle after settling](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_merge_middle_wait5.png), [all results](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_all_merges.png).
   - **Expected:** Each merge consumes the source/addend pair and exposes the calculated result.
   - **Actual:** All three result values appeared after animation settled.
   - **Result:** PASS.

3. **Place result `5` into top `5` slot — VERIFIED**
   - ![Before top placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/before_place_top5.png)
   - ![After top placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_place_top5.png)
   - **Expected:** The result is consumed and the top slot resolves.
   - **Actual:** The top slot visibly resolved with the accepted green `5`; no malformed tile remained for this placement.
   - **Result:** PASS.

4. **Place result `2` into bottom `2` slot — FIRST ATTEMPT BLOCKED**
   - ![Before bottom placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/before_place_bottom2.png)
   - ![After wait](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_place_bottom2_wait6.png)
   - **Expected:** The result centers in the bottom slot and resolves it.
   - **Actual:** The result became displaced/malformed and the bottom slot remained unresolved after six seconds.
   - **Result:** BLOCKED.

5. **Bounded recovery for result `2` — VERIFIED**
   - ![Recovery result](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_recovery_2_wait7.png)
   - **Expected:** A bounded recovery drag may resolve a path/timing-sensitive placement.
   - **Actual:** The malformed result cleared and the bottom target visibly resolved as a green `2`.
   - **Result:** PASS for this placement.

6. **Place final result `5` into middle `5` slot — BLOCKED**
   - ![Before final placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/before_final_place_5.png)
   - ![After wait](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_final_place_5_wait7.png)
   - **Expected:** The final result centers in the middle slot and resolves it.
   - **Actual:** The result became a displaced/malformed white tile; the middle slot remained unresolved after seven seconds.
   - **Result:** BLOCKED.

7. **Bounded recovery for final result `5` — FAILED**
   - ![Final recovery state](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_recovery_final5.png)
   - **Expected:** The recovery resolves the remaining middle target or advances the board.
   - **Actual:** The middle `5` slot remained unresolved and no board transition occurred.
   - **Result:** FAIL/BLOCKED.

## Finding

### F-1 — Known result-placement/rendering defect reproduced

- **Finding ID:** `mergeNumberUpTo5Lo-top-slot-placement-misrendered`
- **Status:** known/recurring
- **Severity:** high
- **Expected:** A valid result released into a clear matching destination settles in the slot and resolves it.
- **Actual:** Two placements produced displaced/malformed result tiles. The bottom `2` required a recovery drag; the final middle `5` remained malformed after the normal attempt and one bounded recovery. The middle slot stayed unresolved.
- **Evidence:** [bottom failure](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_place_bottom2_wait6.png), [final failure](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/after_recovery_final5.png).

## Screenshot Evidence and Movement Evidence

- Initial board: `../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/initial.png`
- Merge before/after evidence: listed in step 2.
- Successful top placement: `before_place_top5.png` → `after_place_top5.png`.
- Failed bottom placement and recovery: `before_place_bottom2.png` → `after_place_bottom2_wait6.png` → `after_recovery_2_wait7.png`.
- Failed final placement and recovery: `before_final_place_5.png` → `after_final_place_5_wait7.png` → `after_recovery_final5.png`.
- Godot runtime log: `../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/godot.log`.

## Final State

- Board 1 remained on screen with the top `5` and bottom `2` accepted, the middle `5` target unresolved, and a malformed/displaced final result.
- **Board 1 completion:** Not verified.
- **Full-level completion:** Not tested.

## Issues Found

- Reproduced high-severity result-placement/rendering defect; see F-1.
- Godot logged invalid external-resource UIDs for `tracingOutline.ttf` and fell back to text paths; the board still rendered.

## Level Result Summary

- **Board 1:** Rendered; all three merges completed; two placement paths needed recovery, and the final placement remained blocked.
- **Board 1 completion:** 0/1 verified.
- **Boards 2–10:** Not tested by request scope.
- **Overall:** **BLOCKED / NOT COMPLETED**.

## Overall Conclusion

The requested single-board execution was carried out. The board rendered and all three arithmetic merges worked, but the board could not be completed because the final result placement repeatedly became malformed and left its matching slot unresolved.

## Missing Evidence / Untested Coverage

- Successful completion of Board 1.
- Boards 2–10 and full-level completion.
- Audio/TTS, invalid-interaction coverage, Android/device behavior, and formal performance measurement.
- No final-completion screenshot is claimed because completion was not observed.

## Artifacts

- [Run flow](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/flow.md)
- [Raw events](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/events.json)
- [Artifact directory](../runs/20260922-mergeNumberUpTo5Lo-one-board-1442/artifacts/)
