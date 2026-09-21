---
type: Runbook
title: "Match category completion"
description: "Launch gd-math, open Level Categories, select Match, open one Match level, and complete it."
tags: [runbook, match, completion]
version: 1
status: active
---

# Match category completion

- **project:** gd-math
- **target:** `/home/abs-bot-01/Downloads/gd-math.x86_64`
- **purpose:** Verify that a learner can navigate to the Match category, open a Match level, and complete the activity.
- **boundary:** Safe gameplay only; no purchases, messages, deletions, or production changes.
- **expected outcome:** One Match level is completed and the app shows clear completion feedback or progression.

## Tests

### T1 — Start the game
**objective:** Confirm the game launches to its main menu.
**steps:** Launch the supplied executable with the approved tester launcher and inspect the initial screen.
**expected:** The app launches and the main menu is visible with a Play control.

### T2 — Open Level Categories
**objective:** Navigate from the main menu to the level category selector.
**steps:** Select Play and inspect the resulting screen.
**expected:** Selecting Play opens a Level Categories screen with category choices.

### T3 — Select Match category
**objective:** Enter the Match category.
**steps:** Select Match from the category selector and inspect the resulting level list.
**expected:** The Match category opens and lists selectable Match levels.

### T4 — Open one Match level
**objective:** Open a single Match level for gameplay.
**steps:** Select the first clearly available Match level and inspect the activity screen.
**expected:** Selecting one Match level opens a playable Match activity.

### T5 — Play Match level completely
**objective:** Complete the selected Match activity from start to finish.
**steps:** Use the activity's intended interaction to match every presented item; continue until completion feedback or progression appears.
**expected:** The activity can be completed using its intended interactions and displays clear completion feedback or progression.
