# Existing-Run Analysis Reference

Use this reference when the requested deliverable is an analysis of a completed QA run rather than a new test.

## Retrieval recipe

1. Search session history using the exact level ID and likely variant names. Include tool messages when the user asks about tool-call history.
2. Select the exact session whose title, user request, run ID, and result match. Do not merge a base level with an LO variant or combine separate retests unless comparison is explicitly requested.
3. Read the session in bounded windows until the requested run ends. Stop before later unrelated turns, such as cost, configuration, or provider discussions.
4. Use the run's existing `events.json`, `flow.md`, report, and screenshots as corroborating evidence. Do not relaunch the game merely to improve a retrospective analysis.
5. Parse or count the transcript programmatically when reporting totals. The unit is an individual tool invocation; a single assistant message may contain several calls.

## Call classification

| Classification | Use when |
|---|---|
| Necessary | Required by the requested scope, evidence contract, live interaction, cleanup, or final verification |
| Partly necessary | Useful but duplicated, overly broad, or mixed with unrelated variant data |
| Not necessary | Does not contribute to the requested run, is a source-code detour, or repeats already verified evidence |
| Failed/irrelevant | Returned an error, stale path, unavailable backend, empty search, or evidence for another run |

Judge necessity against the user's scope, not against whether the call produced output. A successful call can still be unnecessary.

## Reconciliation checklist

- Confirm the exact level variant and requested board scope.
- Count individual invocations and separately count assistant tool-call messages if useful.
- Preserve batched calls as separate rows with a message ID and suffix such as `8950-A` and `8950-B`.
- Identify the first rendered-board evidence, each gameplay action, each post-action verification, cleanup, and artifact verification.
- Separate gameplay calls from exploratory setup, broad searches, source inspection, stale-path attempts, and later unrelated turns.
- Reconcile configured boards, requested boards, completed boards, screenshot count, event count, and final PASS/FAIL/BLOCKED status before making totals.
- State what was not tested and link the exact existing report/session when available.
