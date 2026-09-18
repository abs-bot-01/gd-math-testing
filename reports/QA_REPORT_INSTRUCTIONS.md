# QA Report Generation Instructions

## Purpose

Create a complete, evidence-backed QA testing report in Markdown (`.md`) format for the tested game levels.

The report must use only confirmed test evidence, screenshots, runtime observations, and verified project configuration. Do not invent observations. If evidence is unavailable, write exactly:

> Screenshot not available

Every result must be clearly marked **PASS**, **FAIL**, or **BLOCKED**.

---

# QA Test Report

## 1. Test Summary

Include:

- Total levels tested
- Passed levels
- Failed levels
- Blocked levels, if any
- Overall testing result
- Device/environment used

Use a compact summary table when useful, followed by a vertical explanation for narrow-screen and eBook readability.

---

## 2. Level Details

Create a subsection for every tested level.

For each level, include:

- **Level ID:**
- **Level title:**
- **Age:**
- **Branch:**
- **Level type:**
- **Learning objective:**
- **Learning outcome:**
- **Test result:** PASS / FAIL / BLOCKED

Only report configuration values that were confirmed from the project configuration or visible runtime evidence. Clearly label configuration-derived information when gameplay confirmation was not completed.

---

## 3. QA Properties Checked

Create a subsection for every level and check all 22 properties below:

1. Level Identity
2. Level Configuration
3. Learning Objective
4. Board Layout
5. Visual Content
6. Image/Asset Quality
7. Alignment and Positioning
8. Scale and Aspect Ratio
9. Padding and Safe Margins
10. Text and Labels
11. Touch Interaction
12. Touch Target / Hitbox
13. Valid Interaction
14. Invalid Interaction
15. Solution Validation
16. Visual Feedback
17. Animation
18. Audio / TTS
19. Instructions / Hints
20. Completion State
21. Performance
22. Device Quality

For every property, provide the following fields vertically:

### Property: `<property name>`

**Expected Result:**  
Describe the expected behavior.

**Actual Result:**  
Describe only what was observed.

**Status:** PASS / FAIL / BLOCKED

**Observation:**  
Add concise evidence context, including the screenshot filename when applicable.

If the property was not tested, mark it **BLOCKED** and explain why. Do not mark an untested property PASS.

---

## 4. Action-by-Action Testing

Create one subsection for every user action performed in each level.

### Action 1

- **Action:**
- **Selected object/tile:**
- **Source position:**
- **Destination position:**
- **Why the move is correct:**
- **Expected result:**
- **Actual result:**
- **Accepted/Rejected:**
- **Screenshot:**
- **Observation:**

Repeat for every move performed.

Important rules:

- Record only actions actually performed.
- Do not infer a source position if it cannot be confirmed.
- Use `Screenshot not available` when a required screenshot was not retained.
- State whether the move was accepted or rejected based on observed board behavior.
- Do not claim completion from a changed screen alone unless the board transition or success state was visibly confirmed.

---

## 5. Screenshot Evidence

Embed every available screenshot using relative Markdown paths.

Use this structure:

### Screenshot: Initial State

![Initial State](screenshots/<levelId>_00_initial.png)

**What happened in the screenshot:**  
Describe exactly what is visible, including:

- Board layout
- Objects or tiles
- Positions
- Numbers, shapes, or images
- Text and buttons
- Alignment
- Visible issues
- Current game state

**Expected:**  
Describe what should be visible.

**Actual:**  
Describe what is actually visible.

**Result:** PASS / FAIL / BLOCKED

Do not describe details that cannot be confirmed from the screenshot.

Use the same structure for every screenshot. If a screenshot is missing, do not create a fake image reference. Write:

> Screenshot not available

---

## 6. Before and After Movement Evidence

For every movement, include both screenshots when available.

### Move `<number>` — Before Move

![Before Move](screenshots/<levelId>_<number>_before_move.png)

**Description:**  
Explain the selected object's initial position and the current board state.

If unavailable:

> Screenshot not available

### Move `<number>` — After Move

![After Move](screenshots/<levelId>_<number>_after_move.png)

**Description:**  
Explain where the object was moved, how the board changed, and whether the application accepted the move.

If unavailable:

> Screenshot not available

**Expected Result:**  
Describe the expected move result.

**Actual Result:**  
Describe the observed move result.

**Result:** PASS / FAIL / BLOCKED

---

## 7. Final State

Embed the final screenshot when available:

![Final State](screenshots/<levelId>_final.png)

If unavailable:

> Screenshot not available

Describe:

- Whether the level or board was completed
- Final board state
- Success or completion feedback
- Animation
- Sound/TTS, only if actually verified
- Whether the completion state is correct
- Whether the result represents one board or the complete level

Separate the evidence clearly:

**Expected:**  
Describe the expected completion state.

**Actual:**  
Describe the observed final state.

**Result:** PASS / FAIL / BLOCKED

Do not claim full-level completion when only one board was completed.

---

## 8. Issues Found

Create this table:

| Issue ID | Level ID | Issue Description | Severity | Expected | Actual | Screenshot | Status |
|---|---|---|---|---|---|---|---|
| QA-001 | `<levelId>` | `<description>` | Critical / High / Medium / Low | `<expected>` | `<actual>` | `<relative path or Screenshot not available>` | Open / Confirmed / Blocked / Not tested |

Use only these severity values:

- Critical
- High
- Medium
- Low

Every issue must include reproducible evidence or be explicitly marked as observed without a retained screenshot.

---

## 9. Level Result Summary

Create this table:

| Level ID | Level Title | Test Result | Issues Found | Remarks |
|---|---|---|---|---|
| `<levelId>` | `<title>` | PASS / FAIL / BLOCKED | `<issue IDs>` | `<brief evidence-based remark>` |

If only one board of a multi-board level was tested, write:

> PASS for one verified board; FAIL / INCOMPLETE for full-level scope.

---

## 10. Overall Conclusion

Summarize:

- Overall PASS / FAIL / BLOCKED result
- Major issues found
- Interaction behavior
- Visual quality
- Solution validation
- Completion behavior
- Device performance
- Whether the tested levels are ready for the next testing stage

The conclusion must distinguish:

- Verified behavior
- Observed but incomplete behavior
- Blocked or untested behavior

Do not claim that a level is fully passed if required boards, actions, screenshots, invalid interactions, audio, completion, or device checks remain untested.

---

## Evidence and Verification Checklist

Before finalizing the report:

- [ ] The report is saved as a Markdown `.md` file.
- [ ] Every requested level is listed.
- [ ] Total, passed, failed, and blocked counts are reconciled.
- [ ] Every level has all 22 QA properties.
- [ ] Every performed action is documented.
- [ ] Every available screenshot uses a relative Markdown path.
- [ ] Missing screenshots are explicitly labeled `Screenshot not available`.
- [ ] Screenshot paths point to real, non-empty files.
- [ ] Before/after evidence is not fabricated.
- [ ] Final completion evidence is distinguished from board-level transition evidence.
- [ ] Audio/TTS is not marked PASS without direct verification.
- [ ] Invalid interactions are not marked PASS unless tested.
- [ ] Full-level completion is not claimed from one completed board.
- [ ] No unverified assumptions are presented as facts.
- [ ] The report has been read back and checked for formatting.
- [ ] No project files were modified during documentation.

---

## Recommended Vertical Formatting

For eBook viewers and narrow screens:

- Prefer headings and labeled paragraphs over wide tables.
- Keep each property in its own vertical subsection.
- Keep expected and actual results on separate lines.
- Use short paragraphs and bullet lists.
- Use tables only for compact summaries and issue indexes.
- Keep screenshot descriptions immediately below each image.
- Use relative paths so the report remains portable with its evidence folder.

---

## Report Naming Convention

Use a clear filename:

```text
<scope>_qa_test_report.md
```

Examples:

```text
stackBasicShapes_final_qa_report.md
all_requested_levels_qa_test_report.md
```

**Final rule:** Report only what was actually tested and verified.