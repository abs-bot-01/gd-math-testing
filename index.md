# Tester Run Index

- `addHeightTestLevel-20260917` — `addHeightTestLevel` — BLOCKED / INCOMPLETE — Board 1 rendered; merge interaction failed; 0/5 boards completed; two findings recorded — `reports/addHeightTestLevel-20260917.md`

- `regression-20260916-1713` — Regression Testing — PARTIAL / INCOMPLETE — desktop Godot launch/navigation/level/build smoke verified; user/cloud/playlists/full-board/device coverage incomplete; one repeated invalid-resource-UID warning recorded — `reports/regression-20260916-1713.md`
- `regression-20260916-1713-embedded` — Markdown regression report with inline-embedded screenshots; 27 screenshots in a dedicated artifacts folder — `reports/regression-20260916-1713-embedded.md`

- `representative-20260916-1539` — 12 Representative Levels — PARTIAL / INCOMPLETE — 12/12 initial boards rendered; 4/12 exploratory actions showed clear state changes; 0 full-level completions; Android unavailable — `reports/representative-20260916-1539.md`

- `20260911-animalBirdWithCountTypeDH-godot` — `animalBirdWithCountTypeDH` — PARTIAL / INCOMPLETE — board rendered; no accepted Type/Count answer or completion verified — `reports/20260911-animalBirdWithCountTypeDH-godot.md`

- `rep-gameplay-20260911-consolidated` — 11 Representative Levels — PARTIAL / INCOMPLETE — 8 with gameplay evidence, 3 blocked, 0 full-level completions — `reports/rep-gameplay-20260911-consolidated.md`

- `rep-gameplay-20260911` — `practicingDoubleTap`, `beforeAndAfter1To10` — PARTIAL — direct desktop gameplay; board transition verified for practicingDoubleTap; full-level completion not verified — `reports/rep-gameplay-20260911.md`
- `20260911-representative-missing-godot` — 11 Representative Levels — PARTIAL — 11/11 initial boards rendered; gameplay/full completion not tested — `reports/20260911-representative-missing-godot.md`

- `20260911-writeLevelIntroduction-godot` — `writeLevelIntroduction` — PASS (direct Godot) — 1/1 board completed; Android not covered — `reports/20260911-writeLevelIntroduction-godot.md`

- `20260911-writeLevelIntroduction-retest` — `writeLevelIntroduction` — BLOCKED — fresh Android launch black; Vulkan QueuePresentKHR failure — `reports/20260911-writeLevelIntroduction-retest.md`

- `20260911-representative-writeLevelIntroduction` — `writeLevelIntroduction` — BLOCKED — Android black/Vulkan render failure; gameplay not reached — `reports/20260911-representative-writeLevelIntroduction.md`

- `gd-math-regression-20260911` — GD Math Godot — FAIL / INCOMPLETE — 5 rendered initial boards; no full-level pass; fruit drag and shape completion issues observed; Android blocked — `reports/gd-math-regression-20260911.md`
- `20260910-devTesting-mergeNumberUpTo7-rerun` — `mergeNumberUpTo7` — PARTIALLY TESTED — first-board transition verified; full level incomplete — `reports/20260910-devTesting-mergeNumberUpTo7-rerun.md`
- `20260910-devTesting-mergeNumberUpTo7` — `mergeNumberUpTo7` — BLOCKED / NOT TESTED — 2 blockers — `reports/20260910-devTesting-mergeNumberUpTo7.md`

Each completed run adds one line with run ID, target, result, finding count, and report path.

## Status
- Findings file: `findings.jsonl`
- Questions file: `questions.jsonl`
- Decisions file: `decisions.jsonl`
- Knowledge file: `knowledge.jsonl`
- Journals: `journals/`
- Evidence: `artifacts/`
- Reports: `reports/`

## Recurrence policy
Repeated findings should retain a stable fingerprint, link prior occurrences, preserve evidence, and include an escalation recommendation. Explicitly suppressed findings remain suppressed only according to a recorded human decision.

## Data contract
All JSONL files contain one valid UTF-8 JSON object per line. Evidence paths are relative to this directory's parent workspace. Secrets and tokens are never stored.

## Reporting
Reports are Markdown files. The Tester should attach the report path through Hermes gateway delivery and show a concise rendered summary in chat.

- writeLevel1To5ICMV2_20260915: BLOCKED; writeLevel1To5ICMV2; 0/10 boards; empty source-run board; evidence under artifacts/writeLevel1To5ICMV2_20260915/; report reports/writeLevel1To5ICMV2_20260915.md
