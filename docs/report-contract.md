# QA report contract

Every completed or stopped run must produce a readable Markdown report under `tester-data/reports/<run-id>.md`.

## Required sections

- `# QA Test Report`
- Test Summary
- Level Details
- Source/runtime identity and configuration
- Environment and backend provenance
- Board-by-board action coverage
- Screenshot evidence with Expected, Actual, and Result
- Final state
- Issues/findings
- Level result summary
- Overall conclusion
- Explicit missing or not-tested evidence

## Result rules

- `PASS`: all requested configured boards, required actions, final completion, cleanup, and artifact validation are verified.
- `FAIL`: playable behavior exposed a reproducible violation.
- `PARTIAL / INCOMPLETE`: some actions or boards were verified but requested scope or completion is unfinished.
- `BLOCKED`: gameplay was unreachable due to environment, launch, renderer, or target prerequisites.

Do not mark untested audio, invalid interactions, hints, performance, device behavior, or accessibility as PASS because a board solved.

## Evidence rules

Every cited screenshot must exist and be non-empty. If evidence was not retained, write exactly `Screenshot not available`; never invent a path. Every reported action must have a matching event and available evidence or an explicit missing-evidence statement. Findings in the report must have matching structured records in `tester-data/findings.jsonl`.
