# QA Test Report

## Test Summary

- **Target:** `/shared/hermes/gd-math-godot`
- **Run ID:** `gd-math-regression-20260911`
- **Mode:** Read-only desktop regression run; no project files changed
- **Runtime:** Godot 4.6.1, `gl_compatibility`, Mesa llvmpipe, Xvfb `:1042`, 1280×720
- **Android:** Blocked; `adb devices -l` reported no authorized device/emulator
- **Levels requested:** 5
- **Levels with a verified rendered initial board:** 5
- **Full-level passes:** 0
- **Overall result:** **FAIL / INCOMPLETE**

## Coverage and Results

### `stackVegetablesAndFruitsSet1` — Sort Fruits & Vegetables - Set 1

- **Status:** FAIL / INCOMPLETE
- **Verified:** The selector opened a rendered, playable board with fruit/vegetable sorting groups.
- **Action tested:** One orange tile was dragged toward the upper fruit destination, then retried with a slower drag path.
- **Observed:** The post-action screenshots showed the source tile still present and no verified accepted placement or board transition. The move was rejected or otherwise unchanged.
- **Not tested:** Full solution, invalid interaction behavior, completion, audio/TTS, and performance across all boards.
- **Evidence:**
  - `../artifacts/gd-math-regression-20260911/action-evidence/stackVegetablesAndFruitsSet1_00_initial.png`
  - `../artifacts/gd-math-regression-20260911/action-evidence/stackVegetablesAndFruitsSet1_01_before_move.png`
  - `../artifacts/gd-math-regression-20260911/action-evidence/stackVegetablesAndFruitsSet1_01_after_move.png`
  - `../artifacts/gd-math-regression-20260911/action-evidence/stackVegetablesAndFruitsSet1_01_after_move_retry.png`

### `stackBasicShapes` — Sort Objects by 2D Shape

- **Status:** FAIL / INCOMPLETE
- **Verified:** The selector opened a rendered playable shape-sorting board.
- **Action tested:** Six drag attempts were made with before/after screenshots for each attempt.
- **Observed:** The final screenshot still showed a board with remaining/misplaced objects; no verified completion transition occurred.
- **Not tested:** Full ten-board completion, invalid interaction behavior, audio/TTS, hints, and detailed animation timing.
- **Evidence:**
  - `../artifacts/gd-math-regression-20260911/stackBasicShapes_00_initial.png`
  - `../artifacts/gd-math-regression-20260911/action-evidence/stackBasicShapes_01_before_move.png` through `stackBasicShapes_06_before_move.png`
  - Matching `*_after_move.png` files and `stackBasicShapes_final.png`

### `countWithSingleStick1To3` — One by One Up to 3

- **Status:** BLOCKED / NOT COMPLETED
- **Verified:** A rendered playable board opened. The title and pencil-count tiles/slots were visible.
- **Not tested:** Any move, solution validation, completion, invalid interaction, audio/TTS, hints, and performance.
- **Evidence:** `../artifacts/gd-math-regression-20260911/countWithSingleStick1To3_00_initial.png`

### `ssMultiplication31` — Multiply & Revise - Set 1

- **Status:** BLOCKED / NOT COMPLETED
- **Verified:** A rendered playable multiplication board opened. Number tiles, operators, result slots, and target groups were visible.
- **Notable observation:** The board visibly rendered enough to inspect, but no gameplay action was attempted in this run.
- **Not tested:** Any move, solution validation, completion, invalid interaction, audio/TTS, hints, and performance.
- **Evidence:** `../artifacts/gd-math-regression-20260911/ssMultiplication31_00_initial.png`

### `stackMultiStick1To3` — Count Up to 3

- **Status:** BLOCKED / NOT COMPLETED
- **Verified:** A rendered playable board opened. The title, one-pencil and three-pencil source tiles, and corresponding count slots were visible.
- **Not tested:** Any move, solution validation, completion, invalid interaction, audio/TTS, hints, and performance.
- **Evidence:** `../artifacts/gd-math-regression-20260911/stackMultiStick1To3_00_initial.png`

## Findings

### GD-MATH-REG-001 — Fruit/vegetable valid drag not accepted or not verified

- **Level:** `stackVegetablesAndFruitsSet1`
- **Severity:** High
- **Status:** New / observed
- **Expected:** A correctly categorized tile dropped within the matching fruit group should be accepted and remain placed.
- **Actual:** The orange tile remained visibly in the source area after two drag attempts; no accepted placement or transition was verified.
- **Evidence:** The initial, before, after, and retry screenshots listed above.
- **Next step:** Reproduce using coordinates captured from the current board and verify source/destination hitboxes; test a center drop and record the result.

### GD-MATH-REG-002 — Shape board did not reach verified completion

- **Level:** `stackBasicShapes`
- **Severity:** High
- **Status:** New / incomplete
- **Expected:** Correctly sorting all visible shapes should produce a verified board-completion transition; the configured multi-board level should continue until its terminal completion state.
- **Actual:** Six attempts did not produce a verified completion transition; the final screenshot retained unsolved/misplaced board content.
- **Evidence:** Six before/after pairs and final screenshot.
- **Next step:** Re-enumerate the live board mapping from a fresh screenshot, use target centers, and continue until board and full-level completion are visibly confirmed.

### GD-MATH-REG-003 — Android regression target unavailable

- **Scope:** All levels
- **Severity:** Blocker
- **Status:** Blocked
- **Expected:** An authorized Android device or emulator should appear in `adb devices -l` for APK regression coverage.
- **Actual:** No authorized Android targets were listed.
- **Impact:** Android install, launch, renderer, touch, device layout, and performance were not tested.

## QA Areas Not Tested

- Full completion for every requested level
- Invalid interactions and rejection feedback
- Audio/TTS
- Hints/instructions behavior beyond visible title/board rendering
- Detailed animation timing
- Android device layout and touch behavior
- Full-level performance across configured boards

## Evidence Validation

- Report path: `/home/abs-bot-01/Hermes/hermes-tester/tester-data/reports/gd-math-regression-20260911.md`
- Journal path: `/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/gd-math-regression-20260911.jsonl`
- Evidence root: `/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/gd-math-regression-20260911/`
- All cited PNG files were created with non-zero sizes.
- Journal was rewritten as JSONL and validated after capture.
- No project files were modified.

## Conclusion

The current desktop regression confirms that all five selectors can reach rendered boards, but it does not establish a passing gameplay regression. One valid-looking fruit drag was not accepted or could not be verified, and the shape board remained incomplete after six attempts. The three remaining levels were visually rendered but not functionally exercised. Android coverage remains blocked by the absence of an authorized target.
