# QA Test Report

## Test Summary

- **Run ID:** `20260922-mergeNumberUpTo5Lo-retest-one-board-1342`
- **Target:** `mergeNumberUpTo5Lo`
- **Scope:** Retest one board using LO timing.
- **Environment:** Godot 4.6.1, Linux/X11 Xvfb `:1054`, 1280×720, Mesa llvmpipe.
- **Overall result:** **BLOCKED / NOT COMPLETED**
- **Configured boards:** 10
- **Boards requested:** 1
- **Boards completed:** 0

## Level Details

- **Title:** Add 1 to Get Numbers Up to 5 - LO
- **Type:** `icmV2`
- **Variants:** `numberTile` → `numberSlot`
- **Extensions:** `mergeAndFillBase`, `mergeNumberUpTo5`, `alternatingStrikersBars`, `age5Drops`
- **Authoritative source:** `/home/abs-bot-01/dev/gd-math-config/data/yamlFiles/levels.yaml:12234`
- **Runtime source:** `/home/abs-bot-01/dev/gd-math-godot/assets/config.json`

## Action-by-Action Testing

### Board 1

1. **Launch and render — VERIFIED**
   - The requested level rendered with the expected LO title.
   - Evidence: [initial board](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_initial_board.png)

2. **Merge operations — VERIFIED**
   - `2 + 1 = 3`
   - `1 + 1 = 2`
   - `4 + 1 = 5`
   - The final merge was confirmed after waiting for the merge animation to settle.
   - Evidence: [top merge](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_merge_top.png), [middle merge](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_merge_middle.png), [bottom merge after settling](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_merge_bottom_wait2.png)

3. **Timed placement of result `3` — BLOCKED**
   - The target platform was observed near the edge of the top destination before the drop.
   - The result was dragged directly into the top `3` slot.
   - The result rendered as an oversized/rotated white tile over the destination instead of settling correctly.
   - Evidence: [before placement](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_before_place_3.png), [after placement](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_place_3.png)

4. **Recovery wait — VERIFIED NOT RECOVERED**
   - After four seconds, the malformed tile remained and the top slot was unresolved.
   - The board did not advance.
   - Evidence: [after four-second wait](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_place_3_wait4s.png)

## Finding

### F-1 — Known placement/rendering defect reproduced

- **Finding ID:** `mergeNumberUpTo5Lo-top-slot-placement-misrendered`
- **Status:** `known`
- **Severity:** high
- **Expected:** A valid result placed into a clear matching destination should settle in the slot and resolve it.
- **Actual:** The valid result `3` became an oversized/rotated tile over the top destination; the slot remained unresolved after four seconds.
- **Retest significance:** The same failure reproduced with a different board mapping and result value than the previous run. This retest still does not prove that every possible timing window is unavailable, but the attempted timed placement was not accepted.
- **Evidence:**
  - `../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_before_place_3.png`
  - `../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_place_3.png`
  - `../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/board01_after_place_3_wait4s.png`

## Level Result Summary

- **Board 1:** Rendered; all three merges completed; first timed placement failed.
- **Board 1 completion:** Not verified.
- **Boards 2–10:** Not tested.
- **Result:** **BLOCKED / NOT COMPLETED**.

## Missing Evidence / Untested Coverage

- Successful completion of Board 1.
- Boards 2–10 and full-level completion.
- Audio/TTS, invalid interactions, Android/device behavior, and formal performance measurement.

## Artifacts

- [Run flow](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/flow.md)
- [Raw events](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/events.json)
- [Artifact directory](../runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/artifacts/)
