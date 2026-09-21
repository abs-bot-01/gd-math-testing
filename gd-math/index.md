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

## Findings and triage

* [Findings](findings.md) - human-readable review queue with evidence links
* [Issues](issues/index.md) - reviewed actionable issues
* [Bugs](bugs/index.md) - confirmed product defects

## Knowledge

* [Knowledge index](knowledge/index.md) - reviewed project knowledge

## Runbooks

* [match-category-completion](runbooks/match-category-completion.md) - Launch gd-math, open Level Categories, select Match, open one Match level, and complete it.
