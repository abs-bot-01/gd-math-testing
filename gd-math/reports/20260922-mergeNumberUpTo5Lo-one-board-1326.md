# QA Test Report

## Test Summary

- **Run ID:** `20260922-mergeNumberUpTo5Lo-one-board-1326`
- **Target:** `mergeNumberUpTo5Lo`
- **Scope:** Complete one board only.
- **Environment:** Godot 4.6.1, Linux/X11 Xvfb `:1052`, 1280×720, Mesa llvmpipe.
- **Overall result:** **BLOCKED / NOT COMPLETED**
- **Configured boards:** 10
- **Boards requested for this run:** 1
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

### Board 1 — blocked before completion

1. **Launch and render — VERIFIED**
   - The requested level launched and rendered the expected LO board title.
   - Evidence: [initial board](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_initial.png)

2. **Top-row merge `4 + 1 = 5` — VERIFIED**
   - The source tile was dragged onto the addend tile.
   - The source was consumed and a result `5` appeared.
   - Evidence: [before](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_before_merge_top_retry2.png), [after](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_merge_top_retry2.png)

3. **Middle-row merge `4 + 1 = 5` — VERIFIED**
   - The source was consumed and a second result `5` appeared.
   - Evidence: [before](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_before_merge_middle.png), [after](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_merge_middle.png)

4. **Bottom-row merge `1 + 1 = 2` — VERIFIED**
   - The source was consumed and a result `2` appeared.
   - Evidence: [before](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_before_merge_bottom.png), [after](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_merge_bottom.png)

5. **Place result `2` into top `2` slot — BLOCKED**
   - The result was dragged with intermediate waypoints around the visible brick platform.
   - The result did not settle inside the top slot; it rendered as a large rotated/oversized white tile near the right side of the board.
   - Evidence: [before placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_before_place_2.png), [after placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_place_2.png)

6. **Wait for recovery — VERIFIED NOT RECOVERED**
   - After four seconds, the malformed tile remained and the top `2` slot remained unresolved.
   - The board did not advance.
   - Evidence: [after four-second wait](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_place_2_wait4s.png)

## Finding

### F-1 — Known high-severity placement/rendering defect

- **Finding ID:** `mergeNumberUpTo5Lo-top-slot-placement-misrendered`
- **Status:** `known`
- **Expected:** A correctly constructed `2` dragged into the clear top `2` destination should settle in the slot and resolve it.
- **Actual:** The result disappeared from its work area but rendered as an oversized/rotated white tile outside the destination. The top slot stayed unresolved after four seconds, preventing board completion.
- **LO observation:** The animated brick platform occupied or crossed the destination area during the placement attempt.
- **Current-run evidence:**
  - `../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_before_place_2.png`
  - `../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_place_2.png`
  - `../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/board01_after_place_2_wait4s.png`

## Level Result Summary

- **Board 1:** Rendered; all three merges completed; destination placement blocked.
- **Board 1 completion:** Not verified.
- **Boards 2–10:** Not tested by request scope.
- **Full level:** Not tested.
- **Result:** **BLOCKED / NOT COMPLETED**.

## Additional Runtime Observation

Godot logged invalid external-resource UIDs for `tracingOutline.ttf` and fell back to text paths. The target board still rendered. See [Godot log](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/godot.log).

## Missing Evidence / Untested Coverage

- Successful completion of Board 1.
- Boards 2–10.
- Full-level completion.
- Audio/TTS, invalid-interaction coverage, Android/device behavior, and formal performance measurement.

## Artifacts

- [Run flow](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/flow.md)
- [Raw events](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/events.json)
- [Artifact directory](../runs/20260922-mergeNumberUpTo5Lo-one-board-1326/artifacts/)
