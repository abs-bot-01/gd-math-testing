# gd-math test evidence architecture

This project separates machine-generated runtime telemetry from the small, reviewable record that is shared with the team.

## Directory layout

```text
gd-math/
├── architecture.md          # this contract
├── setup.md                 # launch and environment information
├── runbooks/                # repeatable test procedures
├── runs/<run-id>/
│   ├── events.json          # local, high-volume event stream; never committed
│   ├── flow.md              # committed, selected flow/state changes
│   └── artifacts/           # local screenshots and other evidence
├── findings.md              # human review queue and links to evidence
├── issues/                  # confirmed or actionable issues
├── bugs/                    # confirmed product defects
└── knowledge/               # durable, non-bug learnings
```

## Events and flow

- `events.json` is the raw JSON collection of event records. An event is something that happened, expressed in the past tense where practical: app opened, app loaded, app crashed, a popup appeared, or an interaction was performed. It is not an `actions.json` file.
- Events are runtime data and may become very large. Each run gets its own `events.json` under its run ID. The file is local/temporary, is overwritten or rotated as needed, and is ignored by version control.
- `flow.md` is the committed, human-readable test flow: what happened first, what happened next, and the important state or context changes. It is a curated projection of `events.json`, not a copy of it.
- Capture screenshots for meaningful state changes (launch, a new level, a new screen, initial/final board state). Do not capture every small move unless the run is investigating a bug; bug investigations may include more detailed evidence.

## Findings lifecycle

1. A run records raw events locally and summarizes significant transitions in `runs/<run-id>/flow.md`.
2. Observations that need human review go in `findings.md`, with the run ID and links to the relevant flow, event sequence, and artifacts.
3. A confirmed/actionable item is promoted into `issues/` or `bugs/`. Keep the original finding link for traceability.
4. An observation that is not a bug is moved or summarized in `knowledge/` so future agents can use it.

`findings.md`, `flow.md`, runbooks, issues, bugs, and knowledge are reviewable Markdown and should be committed. Raw JSON event data and generated screenshots are local evidence and should not be committed.

## Commit policy

The repository must not contain raw event streams. Keep `events.json` files on the test machine and ensure they are ignored. If machine-readable history must be shared, store an intentionally designed aggregate in a database rather than committing the event files.

Every run ID should be unique and stable, for example `retest-match-input-20260902-1234`. Use that ID in findings and links so evidence remains traceable without requiring the raw event stream in Git.
