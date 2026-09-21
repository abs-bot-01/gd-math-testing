---
type: Findings
title: "Findings — gd-math"
description: "Human-readable findings report for project gd-math."
lifecycle: review-queue
tags: [findings]
generated: { by: tester/1.0, at: 2026-09-02T07:13:50Z }
---

# Findings — gd-math

| # | Finding | Description | Severity | Status |
|---|---------|-------------|----------|--------|
| 1 | [F1](#f1) | Selecting a Pattern lesson led to a board showing only the ONE SLOT TWO APPLES heading after the content ca… | medium | needs-retest |
| 2 | [F2](#f2) | Retest using click selection after the original drag attempts also produced no visible selection, movement,… | high | needs-retest |

<a id="f1"></a>

## F1 — Pattern lesson can enter an unusable blank exercise state

**run:** [explore-20260902-1112](runs/explore-20260902-1112/flow.md)

**description:** Selecting a Pattern lesson led to a board showing only the ONE SLOT TWO APPLES heading after the content cards disappeared, with no visible way to continue or return.

**expected:** A populated exercise with actionable content and a completion or navigation path.

**observed:** Wooden board remains with only ONE SLOT TWO APPLES heading; exercise cards are absent and no controls or feedback are visible.

![pattern-stuck](runs/explore-20260902-1112/artifacts/pattern-stuck.png)

*pattern-stuck.png*

**references:** [`flow.md`](runs/explore-20260902-1112/flow.md#seq-8); raw event sequence: `runs/explore-20260902-1112/events.json#seq=8`

**seen in:** 1 run(s) (first: explore-20260902-1112, latest: explore-20260902-1112)

<a id="f2"></a>

## F2 — Match Basic Shapes level does not respond to matching attempts

**run:** [retest-match-input-20260902-1234](runs/retest-match-input-20260902-1234/flow.md)

**description:** Retest using click selection after the original drag attempts also produced no visible selection, movement, feedback, or progression.

**expected:** The intended click-based interaction, if supported, should show selection or progress.

**observed:** No click response was visible. This rules out drag gesture type as the only explanation, but does not isolate the setup from the game level.

| Evidence | Notes |
|---|-------|
| ![match-after-attempts](runs/runbook-match-20260902-1146/artifacts/match-after-attempts.png) | match-after-attempts.png |
| ![click-retest](runs/retest-match-input-20260902-1234/artifacts/click-retest.png) | click-retest.png |

**references:** [`flow.md`](runs/retest-match-input-20260902-1234/flow.md#seq-1), [`runbook flow`](runs/runbook-match-20260902-1146/flow.md#seq-5); raw event sequences: `runs/retest-match-input-20260902-1234/events.json#seq=1`, `runs/runbook-match-20260902-1146/events.json#seq=5`

**seen in:** 2 run(s) (first: runbook-match-20260902-1146, latest: retest-match-input-20260902-1234)

