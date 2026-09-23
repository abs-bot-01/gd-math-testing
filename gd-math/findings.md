# Findings — gd-math

## mergeNumberUpTo5Lo-top-slot-placement-misrendered

- **Run:** `20260921-mergeNumberUpTo5Lo-devtest-185535`
- **Status:** new
- **Severity:** high
- **Confidence:** high
- **Expected:** A constructed `3` placed in the top `3` slot is consumed and satisfies the slot.
- **Actual:** The result disappeared from the work area but rendered as a large rotated/oversized white tile over the top slot; the slot remained unresolved after four seconds. An animated brick platform overlapped the target area.
- **Evidence:** `runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_place_3.png`; `runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/mergeNumberUpTo5Lo_board_01_04_after_wait.png`
- **Report:** `reports/20260921-mergeNumberUpTo5Lo-devtest-185535.md`

## Runtime warning observed

- **Run:** `20260921-mergeNumberUpTo5Lo-devtest-185535`
- **Status:** known/observed
- **Severity:** low
- **Actual:** Godot logged invalid `ext_resource` UIDs for `tracingOutline.ttf` in three scenes and fell back to text paths; the board rendered.
- **Evidence:** `runs/20260921-mergeNumberUpTo5Lo-devtest-185535/artifacts/godot.log`

## Recurrence — mergeNumberUpTo5Lo retest

- **Run:** `20260921-mergeNumberUpTo5Lo-retest10-093837`
- **Status:** known/recurring
- **Severity:** high
- **Actual:** A result `4` placed into the bottom `4` slot again became a large rotated/oversized tile; the slot remained unresolved after four seconds.
- **Evidence:** `runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_place_4.png`; `runs/20260921-mergeNumberUpTo5Lo-retest10-093837/artifacts/mergeNumberUpTo5Lo_board_01_02_after_wait.png`
- **Report:** `reports/20260921-mergeNumberUpTo5Lo-retest10-093837.md`
