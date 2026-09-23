# QA Test Report

## Test Summary

- **Run ID:** `20260922-mergeNumberUpTo5Lo-one-board-1355`
- **Target:** `mergeNumberUpTo5Lo`
- **Scope:** Complete one board using the specified LO timing rule.
- **Environment:** Godot 4.6.1, Linux/X11 Xvfb `:1057`, 1280×720.
- **Result:** **BLOCKED / NOT COMPLETED**
- **Configured boards:** 10
- **Board requested:** 1
- **Boards completed:** 0

## Board 1 Testing

- **Rendered:** VERIFIED. The expected LO board appeared.
- **Merges:** VERIFIED. Results were `2`, `5`, and `5`; targets were `5`, `5`, and `2`.
- **LO timing:** VERIFIED for the attempted drop. The bottom brick was fully to the right of the bottom `2` slot and moving away before the drag/release.
- **Drag route:** VERIFIED. The tile was routed along the left side of the board rather than through the brick.
- **Placement:** BLOCKED. The `2` did not settle into the target. After two seconds it became an oversized/rotated white tile at the right side, and the slot remained unresolved.

Evidence:

- [Initial board](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/artifacts/initial.png)
- [Merged board](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/artifacts/after_bottom_merge_wait.png)
- [Before timed placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/artifacts/before_place_2_clear_right_moving_away.png)
- [After placement](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/artifacts/after_place_2_clear_right_moving_away.png)
- [After two-second wait](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/artifacts/after_place_2_wait2.png)

## Finding

- **ID:** `mergeNumberUpTo5Lo-top-slot-placement-misrendered`
- **Status:** `known`
- **Severity:** high
- **Expected:** A valid result released while the LO is fully away and moving away from the destination should settle in the matching slot.
- **Actual:** The `2` still became oversized/rotated and the bottom target remained unresolved, even under the specified timing and routing method.

## Result Summary

- **Board 1:** Rendered and merged; placement failed under the specified LO timing method.
- **Board 1 completion:** Not verified.
- **Boards 2–10:** Not tested.
- **Overall:** **BLOCKED / NOT COMPLETED**.

## Missing Evidence

- Successful completion of Board 1.
- Boards 2–10 and full-level completion.
- Audio/TTS, invalid interactions, device behavior, and formal performance measurement.

- [Run flow](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/flow.md)
- [Events](../runs/20260922-mergeNumberUpTo5Lo-one-board-1355/events.json)
