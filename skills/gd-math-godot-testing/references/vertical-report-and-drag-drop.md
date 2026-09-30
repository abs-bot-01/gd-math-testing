# Vertical Report and Drag-and-Drop Reference

## Recommended evidence tree

```text
artifacts/<run-id>/
  <levelId>_00_initial.png
  <levelId>_01_before_move.png
  <levelId>_01_after_move.png
  <levelId>_02_before_move.png
  <levelId>_02_after_move.png
  <levelId>_final.png
reports/<run-id>.md
journals/<run-id>.jsonl
```

Use report-relative links such as:

```markdown
![Initial State](../artifacts/<run-id>/<levelId>_00_initial.png)
```

## Vertical Markdown pattern

For narrow screens, avoid wide action tables. Use:

```markdown
### Action 1

**Action:** Drag the circle to the circle group.

**Expected Result:** The object remains in the destination group.

**Actual Result:** The object remained in the destination group.

**Status:** PASS

**Before:** Screenshot not available.

![After Move](../artifacts/run/level_01_after_move.png)
```

Keep wide tables only for compact summaries and issue indexes.

## Interaction-mode and drag/drop pitfalls

- Exact-match the requested level ID in the authoritative configuration before inspecting generated runtime data; a generated related level is not a substitute.
- Inspect the current randomized board before deciding the mapping and interaction mode.
- Read the level's learner-flow/configuration notes for the control contract: spinner/tap selectors require opening the option panel and selecting an option; drag/drop requires a visible movable object and destination.
- Separate packaged access checks from source/dev gameplay checks. A subscription wall can explain why the packaged route is inaccessible, but it cannot prove the level works or fails.
- A rendered board background without visible content is a blocked preflight, not a playable initial state; retain the screenshot and stop interaction claims until content appears.
- Do not classify by real-world object meaning when the rule is shape.
- For category stacks, release inside the currently open portion of the target, preferably the center of an unoccupied slot; the geometric center is safe only before cards occupy the group, because dropping on an accepted card can leave the source unresolved or trigger a false rejection.
- Wait after each release or option selection and confirm the target visibly changes or remains accepted.
- After a board transition, wait for reward/particle overlays to clear and capture a fresh stable mapping image; if the runner's checkpoint points at the prior-board frame, append a transition checkpoint with the new image hash before executing the next plan.
- Treat an unchanged board as rejected or unverified input, not as a gameplay failure, until the interaction mode and current control state have been checked.
- A new board proves one board completed, not the entire configured level.
- Do not call a video complete unless its final frames show the success or transition state.
- If a before/after screenshot was not retained, say `Screenshot not available`; never create a guessed path.

## Report reconciliation

Before delivery, compare:

- requested level count
- configured board count
- boards actually completed
- action count
- existing screenshot count
- PASS/FAIL/BLOCKED totals

A full-level PASS requires evidence for the full requested scope, not just a successful first board.
