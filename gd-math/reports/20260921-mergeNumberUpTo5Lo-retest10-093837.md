# QA Test Report

## Test Summary

**Status: FAIL — reproduced gameplay defect; 10-board completion blocked**

Target: `mergeNumberUpTo5Lo`  
Run: `20260921-mergeNumberUpTo5Lo-retest10-093837`  
Execution: Godot desktop under Xvfb `:1042`  
Scope requested: complete all 10 configured boards

## Level Details

- Title: `Add 1 to Get Numbers Up to 5 - LO`
- Type/parser: `icmV2`
- Variants: `numberTile` → `numberSlot`
- Configured board count: 10
- Board time: 27 seconds
- Mechanic: merge each number with `1`, then place the result in the matching slot

## Coverage Summary

Board 1 was reached. One merge was accepted; the first result placement reproduced the prior malformed-tile defect. Board 1 was not completed, so Boards 2–10 were not tested.

## Action-by-Action Testing

1. **Launch and board render — verified.** Board 1 displayed live rows `3+1=4`, `4+1=5`, and `4+1=5`, with animated brick platforms near target rows. Evidence: `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_00_initial.png`.
2. **Merge `3 + 1` — verified.** The top-row source and addend merged successfully and produced result `4`. Before/after evidence: `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_01_before_merge_3_1.png`, `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_01_after_merge_3_1.png`.
3. **Place result `4` — failed/reproduced.** The result was dragged to the bottom `4` slot through a clear route. It rendered as a large rotated/oversized tile over the target instead of satisfying the slot. The malformed state persisted after four seconds. Evidence: `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_before_place_4.png`, `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_place_4.png`, `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_wait.png`.

## Final State

Board 1 remained unresolved. The bottom `4` slot was not satisfied and the result tile remained malformed. No board-completed or full-level-completed state was reached.

## Issue Found

### `mergeNumberUpTo5Lo-top-slot-placement-misrendered` — HIGH — REPRODUCED

**Expected:** A constructed result placed into its matching slot is consumed and satisfies the slot.  
**Actual:** The result tile became a large rotated/oversized white tile over the destination; the slot remained unresolved after four seconds. This retest reproduced the prior defect using result `4` and the bottom `4` slot, not the prior result `3`/top-slot case.  
**Evidence:** `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_place_4.png`, `../runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_wait.png`.

## Level Result Summary

- Board 1: **FAIL / incomplete**
- Boards 2–10: **NOT TESTED** because Board 1 was blocked by the reproduced defect
- Full level: **NOT COMPLETED**

## Overall Conclusion

I attempted the requested 10-board run, but the level cannot progress past Board 1 because a valid result placement consistently creates a malformed unresolved tile. Continuing would require blind retries and would not provide truthful completion evidence.

## Missing Evidence / Not Tested

- Board completion and full-level completion
- Boards 2–10
- Invalid interactions and monkey testing after the blocker
- Audio/TTS, Android/device behavior, and mobile performance
