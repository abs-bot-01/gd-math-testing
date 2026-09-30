# Testing-setup evidence architecture

This project separates raw runtime telemetry from the small, reviewable QA record. It is the evidence contract for every Pi-agent GD Math run.

## Directory layout

```text
testing-setup/
├── config/                         # target paths and local backend settings
├── docs/                           # this contract and procedures
├── skills/                         # project-local skills; no global installation
├── scripts/                        # runner and validation utilities
├── templates/                      # plan, flow, report, and context templates
├── tester-data/
│   ├── runs/<run-id>/
│   │   ├── plan.json               # run input and live mapping checkpoint
│   │   ├── events.jsonl            # local raw event stream
│   │   ├── flow.md                 # curated state-change record
│   │   └── artifacts/              # screenshots and retained evidence
│   ├── reports/<run-id>.md
│   ├── findings.md
│   ├── findings.jsonl
│   ├── issues/
│   ├── bugs/
│   └── knowledge/
└── tests/
```

## Event and flow rules

- `events.jsonl` is newline-delimited JSON. It records what happened, including backend metadata, actions, screenshots, reviews, findings, cleanup, and final status.
- `flow.md` is a short human-readable projection of meaningful state transitions. It is not a dump of the event stream.
- Screenshots and raw events are local run evidence. Keep them below `tester-data/`; do not write persistent setup state to system directories.
- A run must record `input_backend`, `screenshot_backend`, `visual_review_backend`, and `computer_use_invoked` separately.
- A tool catalog entry or a loaded skill is not a tool invocation. Backend provenance comes only from the run commands and transcript records.

## Findings lifecycle

1. Record the observation immediately in the run event stream.
2. Add a matching structured record to `tester-data/findings.jsonl`.
3. Add a concise human-facing entry to `tester-data/findings.md` with links to the run, flow, raw events, and evidence.
4. Promote confirmed/actionable defects to `issues/` or `bugs/` only after review.
5. Store durable non-bug behavior in `knowledge/`.

## Scope rules

Keep requested board scope separate from configured `boardCount`. A completed board is not full-level completion. A new playable board after the configured final board is a completion-boundary mismatch. Android or device claims require a real device run; desktop Xvfb evidence is desktop-only.
