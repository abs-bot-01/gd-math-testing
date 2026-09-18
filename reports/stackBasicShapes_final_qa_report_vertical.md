# QA Test Report

## Level: `stackBasicShapes`

**Title:** Sort Objects by 2D Shape  
**Project:** GD Math Godot  
**Result:** **FAIL / INCOMPLETE for full level; PASS for one verified board**  
**Test mode:** Direct Godot desktop execution, read-only  
**Environment:** Linux desktop, Godot 4.6.1, Xvfb `:99`, 1280×720, Mesa llvmpipe  
**Android testing:** Not performed; no authorized Android device was available.

> One board was completed and the game transitioned to a new board. The configuration specifies 10 boards; all 10 were not completed.

---

## 1. Test Summary

### Total levels in this report

1. `stackBasicShapes`

### Board scope

- Configured boards: **10**
- Boards functionally completed: **1**
- Full level completed: **No / not tested to completion**

### Final result

**FAIL / INCOMPLETE for the full-level scope.**  
**PASS for the single verified board.**

### Safety and modification status

- Project files modified: **No**
- Source code modified: **No**
- Level data modified: **No**
- Assets/scenes/settings modified: **No**
- Commit or push performed: **No**

---

## 2. Level Information

### Level ID

`stackBasicShapes`

### Level title

Sort Objects by 2D Shape

### Age

6

### Branch

Geometry

### Level type

`icmV2`

### Variants

`numberTile` → `numberSlot`

### Challenge

`{}`

### Board time

28 seconds

### Configured board count

10

### Learning objective

Place each object into the destination group matching its visible 2D shape.

### Learning outcome

The learner identifies matching shape groups and completes a board by placing all objects correctly.

### Configuration source

`/shared/hermes/gd-math-godot/assets/config.json`

---

## 3. Solution Rule

The board is solved by matching the visible **2D outline** of each object to the corresponding destination group.

Objects must not be sorted by their real-world meaning or category.

### Solution sequence used

1. Drag the first circular-shape object to the upper circular group.
2. Drag the second circular-shape object to the upper circular group.
3. Drag the first non-circular shape object to the lower matching group.
4. Drag the second non-circular shape object to the lower matching group.
5. Confirm that the board transitions to a new board.

### Drop behavior

Drops were released inside the destination group rather than on the boundary. Earlier boundary releases could be rejected; center drops worked.

---

## 4. QA Properties Checked

### 4.1 Level Identity

**Expected:** The correct level ID and title are displayed.  
**Actual:** `stackBasicShapes` and `Sort Objects by 2D Shape` were observed.  
**Status:** **PASS**  
**Observation:** Confirmed from the initial board evidence.

### 4.2 Level Configuration

**Expected:** The runtime board corresponds to the configured type, age, branch, variants, and challenge.  
**Actual:** The configuration matched the requested level and one board rendered.  
**Status:** **PASS**  
**Observation:** The full ten-board configuration was not exercised.

### 4.3 Learning Objective

**Expected:** The board clearly tests sorting by 2D shape.  
**Actual:** The board used shape-based destination groups.  
**Status:** **PASS**  
**Observation:** Consistent with the title and configuration.

### 4.4 Board Layout

**Expected:** A complete playable board is visible.  
**Actual:** Movable objects and destination groups were visible.  
**Status:** **PASS**  
**Observation:** One board was tested.

### 4.5 Visual Content

**Expected:** All required objects and slots are visible.  
**Actual:** Playable objects and destination groups were visible.  
**Status:** **PASS**  
**Observation:** No missing playable object was confirmed.

### 4.6 Image/Asset Quality

**Expected:** No broken or missing assets are visible.  
**Actual:** No confirmed broken asset was observed.  
**Status:** **PASS**  
**Observation:** Visual inspection only.

### 4.7 Alignment and Positioning

**Expected:** Objects and destination groups are aligned and usable.  
**Actual:** The board was usable; no confirmed alignment defect was observed.  
**Status:** **PASS**  
**Observation:** One board observed.

### 4.8 Scale and Aspect Ratio

**Expected:** The board renders without distortion.  
**Actual:** The board rendered at 1280×720.  
**Status:** **PASS**  
**Observation:** No confirmed clipping was observed.

### 4.9 Padding and Safe Margins

**Expected:** Playable content remains inside the safe visible area.  
**Actual:** Playable content remained within the visible board.  
**Status:** **PASS**  
**Observation:** No confirmed margin defect.

### 4.10 Text and Labels

**Expected:** The title and visible labels are readable.  
**Actual:** The level title was readable.  
**Status:** **PASS**  
**Observation:** No confirmed text-rendering defect.

### 4.11 Touch Interaction

**Expected:** Drag/drop interaction responds to input.  
**Actual:** Drag interactions were performed successfully.  
**Status:** **PASS**  
**Observation:** Direct Godot desktop pointer input was used.

### 4.12 Touch Target / Hitbox

**Expected:** Objects and destination groups can be targeted accurately.  
**Actual:** Center drops worked; releases near a slot boundary could be rejected.  
**Status:** **PASS**  
**Observation:** The destination group interior should be used.

### 4.13 Valid Interaction

**Expected:** Correct shape placement is accepted.  
**Actual:** Correct placements were accepted for one board.  
**Status:** **PASS**  
**Observation:** After-move evidence is available.

### 4.14 Invalid Interaction

**Expected:** An incorrect placement is rejected or handled correctly.  
**Actual:** No invalid move was intentionally tested in the final run.  
**Status:** **BLOCKED**  
**Observation:** No final invalid-move evidence is available.

### 4.15 Solution Validation

**Expected:** The correct solution completes the board.  
**Actual:** The game transitioned to a new board after the solution sequence.  
**Status:** **PASS**  
**Observation:** Board-level completion was confirmed.

### 4.16 Visual Feedback

**Expected:** Correct placement and completion feedback appear.  
**Actual:** A board transition/new board appeared after completion.  
**Status:** **PASS**  
**Observation:** Detailed effect timing was not measured.

### 4.17 Animation

**Expected:** Expected movement and success animations play correctly.  
**Actual:** Animation behavior was not independently evaluated frame-by-frame.  
**Status:** **BLOCKED**  
**Observation:** No dedicated animation evidence was captured.

### 4.18 Audio / TTS

**Expected:** Configured audio and TTS work.  
**Actual:** Audio/TTS was not independently verified.  
**Status:** **BLOCKED**  
**Observation:** No audio evidence was captured.

### 4.19 Instructions / Hints

**Expected:** Instructions and hints are usable.  
**Actual:** Instructions and hints were not independently tested.  
**Status:** **BLOCKED**  
**Observation:** No evidence is available.

### 4.20 Completion State

**Expected:** The board recognizes completion.  
**Actual:** A new board appeared after the final accepted move.  
**Status:** **PASS**  
**Observation:** One board only; full-level completion was not verified.

### 4.21 Performance

**Expected:** No crash, freeze, or significant lag occurs.  
**Actual:** No crash or freeze was observed during one board.  
**Status:** **PASS**  
**Observation:** Full ten-board performance was not measured.

### 4.22 Device Quality

**Expected:** Layout and input quality are acceptable on the test device.  
**Actual:** Desktop rendering and drag input were usable.  
**Status:** **PASS**  
**Observation:** Android device quality was not tested.

---

## 5. Action-by-Action Testing

> The final retained action-evidence directory contains the initial screenshot and after-move screenshots. The corresponding before-move files were not retained there and are explicitly marked unavailable.

### Action 1

**Action:** Drag the first circular-shape object to the upper circular group.  
**Selected object/tile:** Circular-shape object; exact label is not confirmed in retained metadata.  
**Source position:** Right-side source area; exact coordinates are not preserved.  
**Destination position:** Upper destination group.  
**Why correct:** The visible 2D outline matches the circular group.  
**Expected result:** The object is accepted and remains in the upper group.  
**Actual result:** The board updated after the drag.  
**Accepted/Rejected:** **Accepted**  
**Before screenshot:** Screenshot not available.  
**After screenshot:** `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png`  
**Observation:** No confirmed rejection was observed.

### Action 2

**Action:** Drag the next shape-matching object to the lower destination group.  
**Selected object/tile:** Shape object; exact label is not confirmed in retained metadata.  
**Source position:** Right-side source area; exact coordinates are not preserved.  
**Destination position:** Lower destination group.  
**Why correct:** The visible 2D outline matches the lower group.  
**Expected result:** The object is accepted and remains in the lower group.  
**Actual result:** The board updated after the drag.  
**Accepted/Rejected:** **Accepted**  
**Before screenshot:** Screenshot not available.  
**After screenshot:** `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png`  
**Observation:** No confirmed rejection was observed.

### Action 3

**Action:** Drag the second circular-shape object to the upper circular group.  
**Selected object/tile:** Circular-shape object; exact label is not confirmed in retained metadata.  
**Source position:** Right-side source area; exact coordinates are not preserved.  
**Destination position:** Upper destination group.  
**Why correct:** The visible 2D outline matches the circular group.  
**Expected result:** The object is accepted and remains in the upper group.  
**Actual result:** The board updated after the drag.  
**Accepted/Rejected:** **Accepted**  
**Before screenshot:** Screenshot not available.  
**After screenshot:** `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png`  
**Observation:** No confirmed rejection was observed.

### Action 4

**Action:** Drag the second non-circular shape object to the lower destination group.  
**Selected object/tile:** Shape object; exact label is not confirmed in retained metadata.  
**Source position:** Right-side source area; exact coordinates are not preserved.  
**Destination position:** Lower destination group.  
**Why correct:** The visible 2D outline matches the lower group.  
**Expected result:** The final object is accepted and the board completes.  
**Actual result:** The game transitioned to a new board.  
**Accepted/Rejected:** **Accepted**  
**Before screenshot:** Screenshot not available.  
**After screenshot:** `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png`  
**Observation:** The transition confirms board-level completion.

---

## 6. Screenshot Evidence

### Initial State

![Initial State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_00_initial.png)

**Visible:** A 1280×720 direct-Godot game board with the requested level, movable objects, and destination groups.  
**Expected:** A playable initial board with the requested level identity and matching slots.  
**Actual:** A playable `stackBasicShapes` board is visible.  
**Result:** **PASS**

### Action 1 — After Move

![Action 1 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png)

**Visible:** The board after the first drag, with an updated board state.  
**Expected:** The selected object remains in the correct group.  
**Actual:** The move was recorded as accepted and the board updated.  
**Result:** **PASS**

### Action 2 — After Move

![Action 2 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png)

**Visible:** The board after the second drag, with another updated state.  
**Expected:** The selected object remains in the matching group.  
**Actual:** The move was recorded as accepted and the board updated.  
**Result:** **PASS**

### Action 3 — After Move

![Action 3 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png)

**Visible:** The board after the third drag, with another updated state.  
**Expected:** The selected object remains in the matching group.  
**Actual:** The move was recorded as accepted and the board updated.  
**Result:** **PASS**

### Action 4 — After Move

![Action 4 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png)

**Visible:** The board after the fourth drag.  
**Expected:** The final object is accepted and the board completes.  
**Actual:** The board-level sequence completed and the game transitioned to a new board.  
**Result:** **PASS**

### Final State

![Final State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png)

**Visible:** The post-completion state after the action sequence.  
**Expected:** A completed board should trigger a success or transition state.  
**Actual:** A new board appeared.  
**Result:** **PASS for one board; FAIL / INCOMPLETE for the full level**

---

## 7. Before and After Movement Evidence

### Move 1

**Before:** Screenshot not available.  
**After:** [View screenshot](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png)  
**Result:** **PASS** — move recorded as accepted.

### Move 2

**Before:** Screenshot not available.  
**After:** [View screenshot](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png)  
**Result:** **PASS** — move recorded as accepted.

### Move 3

**Before:** Screenshot not available.  
**After:** [View screenshot](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png)  
**Result:** **PASS** — move recorded as accepted.

### Move 4

**Before:** Screenshot not available.  
**After:** [View screenshot](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png)  
**Result:** **PASS** — move accepted and board transitioned.

---

## 8. Final State

![Final State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png)

- Board completion: **Confirmed for one board**
- Full level completion: **Not tested; 10 boards are configured**
- Final state: New board/post-completion state appeared
- Success feedback: Board transition observed
- Animation: Not independently measured
- Sound/TTS: Not independently verified
- Completion correctness: Confirmed for the one completed board only

---

## 9. Issues Found

### QA-SBS-001 — Full configured level not completed

- **Severity:** High
- **Expected:** All 10 configured boards are tested for a full-level PASS.
- **Actual:** One board was completed; remaining boards were not tested.
- **Screenshot:** `stackBasicShapes_final.png`
- **Status:** Open / Incomplete

### QA-SBS-002 — Boundary drop sensitivity

- **Severity:** Medium
- **Expected:** A valid object released within the destination should be accepted consistently.
- **Actual:** Earlier releases near the slot boundary were rejected; center drops worked.
- **Screenshot:** Screenshot not available for the rejected attempt.
- **Status:** Observed

### QA-SBS-003 — Invalid interaction not tested

- **Severity:** Medium
- **Expected:** Incorrect placement is rejected or handled correctly.
- **Actual:** No final invalid-move evidence was captured.
- **Screenshot:** Screenshot not available.
- **Status:** Not tested

### QA-SBS-004 — Audio/TTS not verified

- **Severity:** Low
- **Expected:** Configured audio/TTS works.
- **Actual:** No audio evidence was captured.
- **Screenshot:** Not applicable.
- **Status:** Not tested

### QA-SBS-005 — Detailed animation not verified

- **Severity:** Low
- **Expected:** Movement and success animations play correctly.
- **Actual:** No dedicated animation evidence was captured.
- **Screenshot:** Screenshot not available.
- **Status:** Not tested

---

## 10. Level Result Summary

### Level ID

`stackBasicShapes`

### Level title

Sort Objects by 2D Shape

### Test result

**FAIL / INCOMPLETE for full level; PASS for one board**

### Issues found

QA-SBS-001 through QA-SBS-005

### Remarks

One board was completed and the game transitioned to a new board. Full ten-board completion and several secondary QA properties remain unverified.

---

## 11. Overall Conclusion

The direct Godot run confirmed that `stackBasicShapes` can be opened and solved at board level using shape-based drag-and-drop. Correct placements were accepted, and the game transitioned to a new board after the final move.

The evidence does not confirm completion of all 10 configured boards. Invalid interactions, audio/TTS, instructions/hints, detailed animation behavior, and full-level performance were not independently verified.

**Final QA result: FAIL / INCOMPLETE for the full level; PASS for the single verified board.**

The level should not be marked fully ready for the next testing stage until all configured boards are completed and the remaining blocked properties are verified.

---

## 12. Evidence Inventory

### Available screenshots

- [Initial state](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_00_initial.png)
- [Action 1 after move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png)
- [Action 2 after move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png)
- [Action 3 after move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png)
- [Action 4 after move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png)
- [Final state](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png)

### Missing evidence

- `stackBasicShapes_01_before_move.png`
- `stackBasicShapes_02_before_move.png`
- `stackBasicShapes_03_before_move.png`
- `stackBasicShapes_04_before_move.png`
- Invalid-interaction screenshot
- Audio/TTS evidence
- Dedicated animation evidence
- Full ten-board completion evidence

### Related video

[One-board evidence video](../artifacts/gd-math-levels/recordings/stackBasicShapes_one_board_evidence.mp4)

The video is supplementary one-board evidence and does not prove completion of all ten configured boards.

---

**Report generated from retained direct-Godot evidence. No project files were modified.**
