---
name: evidence-qa-reporting
description: Produce truthful reports from verified Godot test evidence.
version: 1.0.0
author: Project Maintainer, Pi-agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [qa, evidence, reports, jsonl, findings]
---

# Evidence QA Reporting

Use this skill for every run report. It separates source/configuration facts, live observations, mechanical runner state, semantic gameplay results, and missing coverage. It does not allow a process exit or image change to become a gameplay PASS.

## Run contract

Each run under `tester-data/runs/<run-id>/` contains:

- `plan.json` — exact target, scope, backend fields, and live mapping;
- `events.jsonl` — append-only raw events;
- `flow.md` — curated meaningful transitions;
- `artifacts/` — retained screenshots and evidence;
- optional transient captures that are not cited after cleanup.

## Status rules

- `PASS`: all requested boards/actions, final completion, cleanup, and validation verified.
- `FAIL`: playable behavior violates the expected contract reproducibly.
- `PARTIAL / INCOMPLETE`: some coverage exists but the requested boundary or completion was not reached.
- `BLOCKED`: a prerequisite, launch, renderer, or target prevented gameplay.
- `NOT TESTED`: no observation was attempted; do not imply a result.

Keep board-level completion separate from full-level completion. Keep desktop evidence separate from Android/device claims.

## Findings

Record a material anomaly at the moment it is observed in both:

1. the run's `events.jsonl` as a `finding_recorded` event; and
2. `tester-data/findings.jsonl` with a stable finding ID, status, severity, confidence, expected behavior, actual behavior, reproduction, and evidence.

Add a matching concise entry to `tester-data/findings.md`. Reuse a stable ID when the same defect recurs; preserve each run's evidence.

## Report format

Write `tester-data/reports/<run-id>.md` with:

- `# QA Test Report`;
- target and environment identity;
- exact source/runtime configuration;
- backend provenance;
- board-by-board actions and expected/actual/result statements;
- embedded or cited screenshots with verified paths;
- findings and evidence;
- cleanup;
- configured/requested/completed totals;
- explicit missing/not-tested evidence;
- overall conclusion.

## Validation

Run `scripts/validate_run.py`. Confirm that every cited PNG exists and is non-empty, every JSONL line parses, the report exists, every action has an event/result, cleanup is verified, and totals reconcile. If a screenshot was not retained, write `Screenshot not available` instead of inventing a path.
