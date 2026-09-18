# QA Test Report

**Project:** GD Math Godot  
**Test scope:** Five requested levels; direct Godot desktop execution  
**Test mode:** Read-only testing; no project files were modified  
**Report evidence root:** `../artifacts/gd-math-levels/`

## 1. Test Summary

| Item | Result |
|---|---|
| Total levels tested | 5 requested; 1 level functionally exercised for one board; 4 levels reached an initial rendered board but were not functionally completed |
| Passed levels | 0 full-level passes; `stackBasicShapes` passed only for one completed board |
| Failed levels | 0 confirmed gameplay failures |
| Blocked levels | `stackBasicShapes` full 10-board scope incomplete; `countWithSingleStick1To3`, `ssMultiplication31`, `stackMultiStick1To3` functionally untested |
| Overall testing result | **FAIL / INCOMPLETE** for the requested complete level scope |
| Device/environment | Linux desktop, Godot 4.6.1, Xvfb display `:99`, 1280×720, Mesa llvmpipe |
| Android device testing | Not performed; no authorized ADB device was available |

**Scope note:** The configuration specifies `boardCount: 10` for `stackBasicShapes`. Evidence confirms one board-level completion and transition, not completion of all ten boards. The other requested levels have initial board screenshots, but no verified action sequence or completion evidence.

## 2. Level Details

### 2.1 `stackVegetablesAndFruitsSet1`

- **Level ID:** `stackVegetablesAndFruitsSet1`
- **Level title:** Sort Fruits & Vegetables - Set 1
- **Age:** 2
- **Branch:** Objects
- **Level type:** `icmV2`
- **Learning objective:** Sort fruit and vegetable objects into their matching groups. This is configuration/title-derived; gameplay completion was not verified.
- **Learning outcome:** Learner is expected to distinguish and group fruits and vegetables. Not functionally verified.
- **Test result:** **BLOCKED / NOT COMPLETED**

### 2.2 `stackBasicShapes`

- **Level ID:** `stackBasicShapes`
- **Level title:** Sort Objects by 2D Shape
- **Age:** 6
- **Branch:** Geometry
- **Level type:** `icmV2`
- **Learning objective:** Sort visible objects according to their 2D shape.
- **Learning outcome:** Learner is expected to identify matching shape groups and place each object in the correct slot. One board-level outcome was verified; all ten configured boards were not tested.
- **Test result:** **FAIL / INCOMPLETE** for full requested scope; **PASS** for one board-level completion.

### 2.3 `countWithSingleStick1To3`

- **Level ID:** `countWithSingleStick1To3`
- **Level title:** One by One Up to 3
- **Age:** 3
- **Branch:** Numbers
- **Level type:** `icmV2`
- **Learning objective:** Match quantities one-by-one up to 3. Configuration/title-derived; gameplay was not verified.
- **Learning outcome:** Learner is expected to associate quantities 1, 2, and 3 with matching count slots. Not functionally verified.
- **Test result:** **BLOCKED / NOT COMPLETED**

### 2.4 `ssMultiplication31`

- **Level ID:** `ssMultiplication31`
- **Level title:** Multiply & Revise - Set 1
- **Age:** 10
- **Branch:** Arithmetic
- **Level type:** `icmV2`
- **Learning objective:** Complete multiplication/revision number relationships. Configuration/title-derived; gameplay was not verified.
- **Learning outcome:** Learner is expected to complete multiplication and related number slots. Not functionally verified.
- **Test result:** **BLOCKED / NOT COMPLETED**

### 2.5 `stackMultiStick1To3`

- **Level ID:** `stackMultiStick1To3`
- **Level title:** Count Up to 3
- **Age:** 3
- **Branch:** Numbers
- **Level type:** `icmV2`
- **Learning objective:** Match quantities up to 3. Configuration/title-derived; gameplay was not verified.
- **Learning outcome:** Learner is expected to count and place the matching quantity tiles. Not functionally verified.
- **Test result:** **BLOCKED / NOT COMPLETED**

## 3. QA Properties Checked

### Status meanings

- **PASS:** Confirmed by current running-game evidence.
- **FAIL:** A confirmed incorrect behavior was observed.
- **BLOCKED:** The property could not be verified because the required interaction or completion state was not reached.

### 3.1 `stackVegetablesAndFruitsSet1`

| Property | Expected Result | Actual Result | Status | Observation |
|---|---|---|---|---|
| Level Identity | Correct ID and title displayed | No current running-game evidence available in this report | BLOCKED | Configuration confirms the requested ID/title only |
| Level Configuration | Board matches configured type, age, branch, variants, and challenge | Static configuration read; gameplay comparison not completed | BLOCKED | No completed board evidence |
| Learning Objective | Fruit/vegetable sorting objective is clear | Not functionally observed | BLOCKED | Objective is configuration/title-derived |
| Board Layout | Complete playable board visible | No current evidence included | BLOCKED | Board interaction not completed |
| Visual Content | All expected objects visible and correct | Not verified | BLOCKED | No action evidence |
| Image/Asset Quality | No missing or broken assets | Not verified | BLOCKED | No completed visual inspection |
| Alignment and Positioning | Objects and slots aligned | Not verified | BLOCKED | No completed visual inspection |
| Scale and Aspect Ratio | Board scales correctly | Not verified | BLOCKED | No completed visual inspection |
| Padding and Safe Margins | Content stays within safe area | Not verified | BLOCKED | No completed visual inspection |
| Text and Labels | Title/instructions readable | Not verified | BLOCKED | No current screenshot evidence |
| Touch Interaction | Expected drag/drop or configured interaction responds | Not tested | BLOCKED | No verified move |
| Touch Target / Hitbox | Targets are reachable and accurate | Not tested | BLOCKED | No verified move |
| Valid Interaction | Correct fruit/vegetable placement accepted | Not tested | BLOCKED | No verified move |
| Invalid Interaction | Wrong category handled correctly | Not tested | BLOCKED | No invalid move evidence |
| Solution Validation | Only correct solution completes | Not tested | BLOCKED | No completion evidence |
| Visual Feedback | Correct/incorrect feedback appears | Not tested | BLOCKED | No action evidence |
| Animation | Expected animations play | Not tested | BLOCKED | No action evidence |
| Audio / TTS | Configured audio/TTS works | Not tested | BLOCKED | No audio evidence |
| Instructions / Hints | Instructions/hints are usable | Not tested | BLOCKED | No evidence |
| Completion State | Level completes correctly | Not tested | BLOCKED | No final state |
| Performance | No crash/freeze/lag | Not verified | BLOCKED | No functional run completed |
| Device Quality | Layout/input/device quality acceptable | Not verified | BLOCKED | Android target unavailable |

### 3.2 `stackBasicShapes`

| Property | Expected Result | Actual Result | Status | Observation |
|---|---|---|---|---|
| Level Identity | Correct ID and title displayed | `stackBasicShapes` / `Sort Objects by 2D Shape` observed | PASS | Initial screenshot shows the requested level title |
| Level Configuration | Board matches configured type, age, branch, variants, challenge | Static configuration matched the requested level; one board was rendered | PASS | Full 10-board comparison not completed |
| Learning Objective | Objects are sorted by 2D shape | Visible board used two shape groups and matching placement | PASS | Objective was consistent with the observed board |
| Board Layout | Complete playable board visible | Initial board and subsequent new board were visible | PASS | Evidence available for one board flow |
| Visual Content | Objects and slots visible | Objects and destination groups were visible | PASS | No missing playable object was confirmed in the completed board |
| Image/Asset Quality | No missing or broken assets | No missing/broken asset was observed in the completed board | PASS | Visual inspection only |
| Alignment and Positioning | Objects/slots aligned | Board elements were visible and usable | PASS | No confirmed alignment defect |
| Scale and Aspect Ratio | Correct 1280×720 rendering | Rendered at 1280×720 | PASS | No confirmed clipping |
| Padding and Safe Margins | Content stays within safe area | Playable content stayed within visible board | PASS | No confirmed margin defect |
| Text and Labels | Title and visible labels readable | Title was readable | PASS | No confirmed text-rendering defect |
| Touch Interaction | Drag/drop responds | Drag interactions were performed | PASS | One board sequence exercised |
| Touch Target / Hitbox | Objects and slots can be targeted | Targets responded when released within slot centers | PASS | Earlier edge releases could be rejected; center drops worked |
| Valid Interaction | Correct shape placement accepted | Correct placements were accepted for one board | PASS | After-move screenshots available |
| Invalid Interaction | Wrong placement rejected or handled | Not intentionally tested in the final completed sequence | BLOCKED | No valid invalid-move evidence |
| Solution Validation | Correct solution completes board | Board transitioned to a new board after placement sequence | PASS | One board only |
| Visual Feedback | Success/transition feedback appears | Board transition/new board was observed | PASS | Final screenshot documents the post-completion state |
| Animation | Expected animation plays | No detailed animation timing was measured | BLOCKED | Transition was observed, but animation details were not separately recorded |
| Audio / TTS | Configured audio/TTS works | Not independently verified | BLOCKED | No audio capture/evidence |
| Instructions / Hints | Instructions/hints usable | Not independently tested | BLOCKED | No evidence |
| Completion State | Board recognizes completion | New board appeared after the completed board | PASS | Full level completion not verified |
| Performance | No crash/freeze/lag | No crash/freeze observed during one board | PASS | Full 10-board performance not measured |
| Device Quality | No layout/input quality problems | Desktop rendering was usable for one board | PASS | Android device quality not tested |

### 3.3 `countWithSingleStick1To3`

| Property | Expected Result | Actual Result | Status | Observation |
|---|---|---|---|---|
| Level Identity | Correct ID/title displayed | Initial board screenshot was captured; no action evidence | PASS | Identity was visually observed, but functional route was not completed |
| Level Configuration | Configuration matches gameplay | Static configuration read; gameplay comparison incomplete | BLOCKED | No completed sequence |
| Learning Objective | One-to-one counting up to 3 is clear | Not functionally verified | BLOCKED | No move evidence |
| Board Layout | Complete board visible | Initial rendered board was captured | PASS | Functional board state not completed |
| Visual Content | Tiles/numbers correct | Not fully verified through interaction | BLOCKED | No action evidence |
| Image/Asset Quality | No broken assets | Not verified across interaction | BLOCKED | No completed run |
| Alignment and Positioning | Objects aligned | Not fully verified | BLOCKED | No completed run |
| Scale and Aspect Ratio | Correct scaling | Initial screenshot rendered at 1280×720 | PASS | Functional quality not completed |
| Padding and Safe Margins | No clipping | No confirmed clipping in initial screenshot | PASS | Interaction not tested |
| Text and Labels | Text readable | Initial screen captured; no full text audit | BLOCKED | Not fully verified |
| Touch Interaction | Count tiles respond | Not tested | BLOCKED | No move evidence |
| Touch Target / Hitbox | Targets respond accurately | Not tested | BLOCKED | No move evidence |
| Valid Interaction | Correct count accepted | Not tested | BLOCKED | No move evidence |
| Invalid Interaction | Wrong count handled | Not tested | BLOCKED | No invalid evidence |
| Solution Validation | Correct sequence completes | Not tested | BLOCKED | No completion evidence |
| Visual Feedback | Feedback appears | Not tested | BLOCKED | No action evidence |
| Animation | Animation works | Not tested | BLOCKED | No action evidence |
| Audio / TTS | Audio works | Not tested | BLOCKED | No audio evidence |
| Instructions / Hints | Instructions work | Not tested | BLOCKED | No evidence |
| Completion State | Level completes | Not tested | BLOCKED | No final state |
| Performance | No crash/freeze/lag | Not verified | BLOCKED | No functional run |
| Device Quality | Device quality acceptable | Not verified | BLOCKED | Android target unavailable |

### 3.4 `ssMultiplication31`

| Property | Expected Result | Actual Result | Status | Observation |
|---|---|---|---|---|
| Level Identity | Correct ID/title displayed | Initial board screenshot was captured; no action evidence | PASS | Identity was visually observed, but functional route was not completed |
| Level Configuration | Configuration matches gameplay | Static configuration read; gameplay comparison incomplete | BLOCKED | No completed sequence |
| Learning Objective | Multiplication/revision objective is clear | Not functionally verified | BLOCKED | No move evidence |
| Board Layout | Complete board visible | Initial rendered board was captured | PASS | Functional board state not completed |
| Visual Content | Numbers/operators/slots correct | Not fully verified | BLOCKED | No action evidence |
| Image/Asset Quality | No broken assets | Not verified across interaction | BLOCKED | No completed run |
| Alignment and Positioning | Number board aligned | Not fully verified | BLOCKED | No completed run |
| Scale and Aspect Ratio | Correct scaling | Initial screenshot rendered at 1280×720 | PASS | Functional quality not completed |
| Padding and Safe Margins | No clipping | No confirmed clipping in initial screenshot | PASS | Interaction not tested |
| Text and Labels | Text readable | Initial screen captured; no full text audit | BLOCKED | Not fully verified |
| Touch Interaction | Number tiles respond | Not tested | BLOCKED | No move evidence |
| Touch Target / Hitbox | Targets respond accurately | Not tested | BLOCKED | No move evidence |
| Valid Interaction | Correct number accepted | Not tested | BLOCKED | No move evidence |
| Invalid Interaction | Wrong number handled | Not tested | BLOCKED | No invalid evidence |
| Solution Validation | Correct sequence completes | Not tested | BLOCKED | No completion evidence |
| Visual Feedback | Feedback appears | Not tested | BLOCKED | No action evidence |
| Animation | Animation works | Not tested | BLOCKED | No action evidence |
| Audio / TTS | Audio works | Not tested | BLOCKED | No audio evidence |
| Instructions / Hints | Instructions work | Not tested | BLOCKED | No evidence |
| Completion State | Level completes | Not tested | BLOCKED | No final state |
| Performance | No crash/freeze/lag | Not verified | BLOCKED | No functional run |
| Device Quality | Device quality acceptable | Not verified | BLOCKED | Android target unavailable |

### 3.5 `stackMultiStick1To3`

| Property | Expected Result | Actual Result | Status | Observation |
|---|---|---|---|---|
| Level Identity | Correct ID/title displayed | Initial board screenshot was captured; no action evidence | PASS | Identity was visually observed, but functional route was not completed |
| Level Configuration | Configuration matches gameplay | Static configuration read; gameplay comparison incomplete | BLOCKED | No completed sequence |
| Learning Objective | Counting up to 3 is clear | Not functionally verified | BLOCKED | No move evidence |
| Board Layout | Complete board visible | Initial rendered board was captured | PASS | Functional board state not completed |
| Visual Content | Count tiles/slots correct | Not fully verified | BLOCKED | No action evidence |
| Image/Asset Quality | No broken assets | Not verified across interaction | BLOCKED | No completed run |
| Alignment and Positioning | Objects aligned | Not fully verified | BLOCKED | No completed run |
| Scale and Aspect Ratio | Correct scaling | Initial screenshot rendered at 1280×720 | PASS | Functional quality not completed |
| Padding and Safe Margins | No clipping | No confirmed clipping in initial screenshot | PASS | Interaction not tested |
| Text and Labels | Text readable | Initial screen captured; no full text audit | BLOCKED | Not fully verified |
| Touch Interaction | Count tiles respond | Not tested | BLOCKED | No move evidence |
| Touch Target / Hitbox | Targets respond accurately | Not tested | BLOCKED | No move evidence |
| Valid Interaction | Correct count accepted | Not tested | BLOCKED | No move evidence |
| Invalid Interaction | Wrong count handled | Not tested | BLOCKED | No invalid evidence |
| Solution Validation | Correct sequence completes | Not tested | BLOCKED | No completion evidence |
| Visual Feedback | Feedback appears | Not tested | BLOCKED | No action evidence |
| Animation | Animation works | Not tested | BLOCKED | No action evidence |
| Audio / TTS | Audio works | Not tested | BLOCKED | No audio evidence |
| Instructions / Hints | Instructions work | Not tested | BLOCKED | No evidence |
| Completion State | Level completes | Not tested | BLOCKED | No final state |
| Performance | No crash/freeze/lag | Not verified | BLOCKED | No functional run |
| Device Quality | Device quality acceptable | Not verified | BLOCKED | Android target unavailable |

## 4. Action-by-Action Testing

Only `stackBasicShapes` reached an action sequence. The evidence set contains after-action screenshots for four actions. The corresponding before-action screenshots were not available in the final action-evidence directory, so they are explicitly marked unavailable here.

### `stackBasicShapes` — Action 1

- **Action:** Drag the first circular-shape object to the upper circular group.
- **Selected object/tile:** Circular-shape object; exact object label is not confirmed from the retained screenshot metadata.
- **Source position:** Right-side source area; exact coordinates not preserved in the report metadata.
- **Destination position:** Upper destination group.
- **Why the move is correct:** The object's visible 2D outline matches the circular group.
- **Expected result:** Object is accepted and remains in the upper group.
- **Actual result:** After-action evidence shows the board updated following the drag.
- **Accepted/Rejected:** Accepted.
- **Screenshot:** Before screenshot not available; after screenshot available below.
- **Observation:** No confirmed rejection was observed for this action.

### `stackBasicShapes` — Action 2

- **Action:** Drag the next shape-matching object to the lower group.
- **Selected object/tile:** Shape object; exact object label is not confirmed from the retained screenshot metadata.
- **Source position:** Right-side source area; exact coordinates not preserved in the report metadata.
- **Destination position:** Lower destination group.
- **Why the move is correct:** The object's visible 2D outline matches the lower group.
- **Expected result:** Object is accepted and remains in the lower group.
- **Actual result:** After-action evidence shows the board updated following the drag.
- **Accepted/Rejected:** Accepted.
- **Screenshot:** Before screenshot not available; after screenshot available below.
- **Observation:** No confirmed rejection was observed for this action.

### `stackBasicShapes` — Action 3

- **Action:** Drag the second circular-shape object to the upper circular group.
- **Selected object/tile:** Circular-shape object; exact object label is not confirmed from the retained screenshot metadata.
- **Source position:** Right-side source area; exact coordinates not preserved in the report metadata.
- **Destination position:** Upper destination group.
- **Why the move is correct:** The object's visible 2D outline matches the circular group.
- **Expected result:** Object is accepted and remains in the upper group.
- **Actual result:** After-action evidence shows the board updated following the drag.
- **Accepted/Rejected:** Accepted.
- **Screenshot:** Before screenshot not available; after screenshot available below.
- **Observation:** No confirmed rejection was observed for this action.

### `stackBasicShapes` — Action 4

- **Action:** Drag the second non-circular shape object to the lower group.
- **Selected object/tile:** Shape object; exact object label is not confirmed from the retained screenshot metadata.
- **Source position:** Right-side source area; exact coordinates not preserved in the report metadata.
- **Destination position:** Lower destination group.
- **Why the move is correct:** The object's visible 2D outline matches the lower group.
- **Expected result:** Object is accepted and the board completes.
- **Actual result:** The board transitioned to a new board after the completed sequence.
- **Accepted/Rejected:** Accepted.
- **Screenshot:** Before screenshot not available; after screenshot available below.
- **Observation:** The transition is evidence of board-level completion, not full-level completion.

## 5. Screenshot Evidence

All paths below are relative to this report file: `../artifacts/gd-math-levels/`.

### `stackBasicShapes` — Initial State

![Initial State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_00_initial.png)

**What happened in the screenshot:** The direct Godot level is visible at 1280×720. The level title and a playable sorting board are visible. Objects and destination groups are present. No confirmed clipping or broken asset is documented from this screenshot.

**Expected:** The requested level identity, title, playable objects, and matching destination slots should be visible.

**Actual:** The requested level board is visible and playable.

**Result:** PASS

### `stackBasicShapes` — Action 1 After Move

![Action 1 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png)

**Description:** The board is shown after the first drag. The board state has changed from the initial state, consistent with an accepted placement.

**Expected:** The selected object remains in the correct shape group.

**Actual:** The after-action board is rendered; the move was recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Action 2 After Move

![Action 2 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png)

**Description:** The board is shown after the second drag. The board has updated again.

**Expected:** The selected object remains in the matching destination group.

**Actual:** The after-action board is rendered; the move was recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Action 3 After Move

![Action 3 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png)

**Description:** The board is shown after the third drag. The board has updated again.

**Expected:** The selected object remains in the matching destination group.

**Actual:** The after-action board is rendered; the move was recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Action 4 After Move

![Action 4 After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png)

**Description:** The board is shown after the fourth drag.

**Expected:** The final required object is accepted and the board completes.

**Actual:** The board-level sequence completed and the game transitioned to a new board.

**Result:** PASS

### `stackBasicShapes` — Final State

![Final State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png)

**Description:** The screenshot shows the post-completion state after the action sequence. The game has advanced to a new board rather than remaining on the same unsolved board.

**Expected:** A completed board should trigger a success/transition state.

**Actual:** A new board appeared, confirming one board-level completion. The full ten-board level completion was not tested.

**Result:** PASS for one board; FAIL/INCOMPLETE for the full level scope.

### Initial Screenshots for the Other Requested Levels

#### `stackVegetablesAndFruitsSet1`

![Initial State](../artifacts/gd-math-levels/stackVegetablesAndFruitsSet1_00_initial.png)

**What happened:** Screenshot not available at the final evidence path for this report. No verified image is embedded.

**Expected:** A rendered fruit/vegetable sorting board.

**Actual:** Screenshot not available.

**Result:** BLOCKED

#### `stackBasicShapes` alternate initial evidence

![Initial State](../artifacts/gd-math-levels/stackBasicShapes_00_initial.png)

**What happened:** This is the retained initial board evidence used for the functional one-board test.

**Expected:** A rendered shape-sorting board.

**Actual:** A rendered shape-sorting board was observed.

**Result:** PASS

#### `countWithSingleStick1To3`

![Initial State](../artifacts/gd-math-levels/countWithSingleStick1To3_00_initial.png)

**What happened:** The screenshot is not in the final action-evidence folder used for this report. The earlier initial screenshot was captured during direct Godot execution, but its final relative evidence location is not available here.

**Expected:** A rendered one-to-one count board.

**Actual:** Screenshot not available at the final report evidence location.

**Result:** BLOCKED

#### `ssMultiplication31`

![Initial State](../artifacts/gd-math-levels/ssMultiplication31_00_initial.png)

**What happened:** The screenshot is not in the final action-evidence folder used for this report. The earlier initial screenshot was captured during direct Godot execution, but its final relative evidence location is not available here.

**Expected:** A rendered multiplication/revision board.

**Actual:** Screenshot not available at the final report evidence location.

**Result:** BLOCKED

#### `stackMultiStick1To3`

![Initial State](../artifacts/gd-math-levels/stackMultiStick1To3_00_initial.png)

**What happened:** The screenshot is not in the final action-evidence folder used for this report. The earlier initial screenshot was captured during direct Godot execution, but its final relative evidence location is not available here.

**Expected:** A rendered count-up-to-3 board.

**Actual:** Screenshot not available at the final report evidence location.

**Result:** BLOCKED

## 6. Before and After Movement Evidence

Before-action screenshots for the final action-evidence set are not available. They are not fabricated here.

### `stackBasicShapes` — Move 1

#### Before Move

**Screenshot:** Screenshot not available.

**Description:** The pre-move state cannot be described from a retained before screenshot.

#### After Move

![After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png)

**Description:** The board is rendered after the first move and shows a changed board state.

**Expected Result:** Correct object accepted into the matching group.

**Actual Result:** Move recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Move 2

#### Before Move

**Screenshot:** Screenshot not available.

**Description:** The pre-move state cannot be described from a retained before screenshot.

#### After Move

![After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png)

**Description:** The board is rendered after the second move and shows a changed board state.

**Expected Result:** Correct object accepted into the matching group.

**Actual Result:** Move recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Move 3

#### Before Move

**Screenshot:** Screenshot not available.

**Description:** The pre-move state cannot be described from a retained before screenshot.

#### After Move

![After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png)

**Description:** The board is rendered after the third move and shows a changed board state.

**Expected Result:** Correct object accepted into the matching group.

**Actual Result:** Move recorded as accepted.

**Result:** PASS

### `stackBasicShapes` — Move 4

#### Before Move

**Screenshot:** Screenshot not available.

**Description:** The pre-move state cannot be described from a retained before screenshot.

#### After Move

![After Move](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png)

**Description:** The board is rendered after the fourth move.

**Expected Result:** Final object accepted and board completes.

**Actual Result:** Board transition/new board was observed.

**Result:** PASS

## 7. Final State

### `stackBasicShapes`

![Final State](../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png)

- **Level completed:** One board completed; full ten-board level not completed.
- **Final board state:** New board/post-completion state visible.
- **Success/completion feedback:** Board transition observed.
- **Animation:** Detailed animation not independently measured.
- **Sound/TTS:** Not independently verified.
- **Completion correctness:** Correct for the one completed board; full-level completion remains unverified.

### Other Levels

Screenshot not available for a verified final state. No completion claim is made for the other four levels.

## 8. Issues Found

| Issue ID | Level ID | Issue Description | Severity | Expected | Actual | Screenshot | Status |
|---|---|---|---|---|---|---|---|
| QA-001 | `stackBasicShapes` | Full configured level contains 10 boards, but only one board was completed in this run | High | All configured boards should be tested and completed for a full-level PASS | One board completed; remaining boards not tested | `stackBasicShapes_final.png` | Open / Incomplete |
| QA-002 | `stackBasicShapes` | Releasing near a slot boundary can reject a drag | Medium | A valid object dropped within the target should be accepted consistently | Earlier attempts near the boundary were rejected; center drops worked | Screenshot not available for the rejected attempt | Observed |
| QA-003 | All other requested levels | No action-by-action or final completion evidence retained in the final report evidence set | High | Every requested level should have complete interaction and completion evidence | Functional testing not completed | Screenshot not available | Blocked |
| QA-004 | All levels | Audio/TTS was not independently verified | Low | Configured audio/TTS should be tested | No audio evidence captured | Screenshot not applicable | Not tested |
| QA-005 | All levels | Invalid interaction behavior was not verified in the final run | Medium | Incorrect moves should be rejected/handled correctly | No final invalid-move evidence | Screenshot not available | Not tested |

## 9. Level Result Summary

| Level ID | Level Title | Test Result | Issues Found | Remarks |
|---|---|---|---|---|
| `stackVegetablesAndFruitsSet1` | Sort Fruits & Vegetables - Set 1 | BLOCKED / NOT COMPLETED | QA-003, QA-004, QA-005 | No retained action/final evidence |
| `stackBasicShapes` | Sort Objects by 2D Shape | FAIL / INCOMPLETE for full level; PASS for one board | QA-001, QA-002, QA-004, QA-005 | One board completed and transitioned to the next |
| `countWithSingleStick1To3` | One by One Up to 3 | BLOCKED / NOT COMPLETED | QA-003, QA-004, QA-005 | No retained action/final evidence |
| `ssMultiplication31` | Multiply & Revise - Set 1 | BLOCKED / NOT COMPLETED | QA-003, QA-004, QA-005 | No retained action/final evidence |
| `stackMultiStick1To3` | Count Up to 3 | BLOCKED / NOT COMPLETED | QA-003, QA-004, QA-005 | No retained action/final evidence |

## 10. Overall Conclusion

The direct Godot test confirmed that `stackBasicShapes` can be opened, interacted with, and completed for one board using shape-based drag-and-drop. A new board appeared after the action sequence, which is evidence of board-level completion. The evidence does not establish completion of all ten configured boards.

The remaining four requested levels do not have retained action-by-action or final-state evidence in the report evidence set. Their learning objectives and configurations were read from the project configuration, but gameplay behavior, invalid interactions, feedback, audio/TTS, completion, and performance were not verified.

**Overall result: FAIL / INCOMPLETE for the requested complete QA scope.**

The tested scope is **not ready for the next testing stage** until:

1. All configured boards for `stackBasicShapes` are completed and recorded.
2. All four remaining levels receive complete action-by-action testing.
3. Before-and-after screenshots are retained for every movement.
4. Invalid interactions, audio/TTS, instructions/hints, animations, and performance are explicitly verified.
5. A final completion state is captured for every level.

No project files, source code, level data, scenes, assets, settings, or configuration were modified during testing.

## Evidence Inventory

### Retained action-evidence screenshots

- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_00_initial.png`
- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_01_after_move.png`
- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_02_after_move.png`
- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_03_after_move.png`
- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_04_after_move.png`
- `../artifacts/gd-math-levels/action-evidence/stackBasicShapes_final.png`

### Missing evidence explicitly not fabricated

- `stackBasicShapes_01_before_move.png` through `stackBasicShapes_04_before_move.png` in the final action-evidence directory
- Retained action evidence for `stackVegetablesAndFruitsSet1`
- Retained action evidence for `countWithSingleStick1To3`
- Retained action evidence for `ssMultiplication31`
- Retained action evidence for `stackMultiStick1To3`
- Verified final completion screenshots for the four incomplete levels
- Audio/TTS evidence
- Invalid-interaction evidence

### Related video evidence

- `../artifacts/gd-math-levels/recordings/stackBasicShapes_one_board_evidence.mp4`

This video is supplementary evidence for the one-board interaction; it does not prove completion of all ten configured boards.

---

**Report generated:** Read-only QA documentation based on retained direct-Godot evidence and project configuration. 
