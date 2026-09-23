# Project index — gd-math

## Architecture

* [Evidence architecture](architecture.md) - event, flow, finding, issue, bug, and knowledge boundaries

## Setup

* [Setup](setup.md) - how to launch and configure the app under test

## Runs

Each run has a committed `flow.md` and local, ignored `events.json` stream. The flow contains only selected events and meaningful state changes.

* [Run explore-20260902-1112](runs/explore-20260902-1112/flow.md) - Explore the main user-facing flows and identify important defects or blockers.
* [Run retest-match-input-20260902-1234](runs/retest-match-input-20260902-1234/flow.md) - Determine whether Match input failure is caused by setup/gesture delivery or by the game level.
* [Run runbook-match-20260902-1146](runs/runbook-match-20260902-1146/flow.md) - Verify navigation to Match category and complete one Match level.
* [Run 20260921-mergeNumberUpTo5Lo-devtest-185535](runs/20260921-mergeNumberUpTo5Lo-devtest-185535/flow.md) - Dev-test mergeNumberUpTo5Lo; Board 1 exposed a malformed top-slot placement and boards 2–10 were not tested.
* [Run 20260921-mergeNumberUpTo5Lo-retest10-093837](runs/20260921-mergeNumberUpTo5Lo-retest10-093837/flow.md) - Retest of all 10 configured boards; Board 1 reproduced the malformed result placement and boards 2–10 were not tested.
* [Run 20260922-mergeNumberUpTo5Lo-one-board-1326](runs/20260922-mergeNumberUpTo5Lo-one-board-1326/flow.md) - One-board execution; all three merges completed, then result-2 placement was blocked by the known malformed-slot defect.
* [Run 20260922-mergeNumberUpTo5Lo-retest-one-board-1342](runs/20260922-mergeNumberUpTo5Lo-retest-one-board-1342/flow.md) - Timed one-board retest; all three merges completed, then result-3 placement reproduced the malformed-slot defect.
* [Run 20260922-mergeNumberUpTo5Lo-one-board-1355](runs/20260922-mergeNumberUpTo5Lo-one-board-1355/flow.md) - One-board retest using LO fully-away/moving-away timing; placement still became malformed and the board did not complete.
* [Run 20260922-mergeNumberUpTo5Lo-one-board-1442](runs/20260922-mergeNumberUpTo5Lo-one-board-1442/flow.md) - One-board execution; all merges completed, top and bottom targets resolved, but the final middle-5 placement remained malformed and the board did not complete.

## Findings and triage

* [Findings](findings.md) - human-readable review queue with evidence links
* [Issues](issues/index.md) - reviewed actionable issues
* [Bugs](bugs/index.md) - confirmed product defects

## Knowledge

* [Knowledge index](knowledge/index.md) - reviewed project knowledge

## Runbooks

* [match-category-completion](runbooks/match-category-completion.md) - Launch gd-math, open Level Categories, select Match, open one Match level, and complete it.
