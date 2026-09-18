# DevTesting Report — `mergeNumberUpTo7`

- Run ID: `20260910-devTesting-mergeNumberUpTo7`
- Date: 2026-09-10
- Target: `/home/abs-bot-01/dev/gd-math-godot`
- Requested level: `mergeNumberUpTo7`
- Scope: devTesting build/readiness and direct Godot fallback; one representative level only

## Level metadata — verified

From `assets/config.json`:

- Skill age: 5
- Branch: Arithmetic
- Sequence: 60
- Tags: `match|v1|representative`
- Title: **Add 1 to Get Numbers Up to 7**
- Type: `icmV2`
- Variants: `numberTile` → `numberSlot`
- Board count: 10
- Board time: 27 seconds

## Execution results

### Android readiness — blocked

- `adb devices -l`: no connected or running device/emulator.
- `/dev/kvm` exists, but the current effective session lacks `kvm` group permission.
- APK installation and Android gameplay were not attempted after the readiness gate failed.

### `devTesting` build — blocked

Command: `./buildMaker.sh devTesting main`

- Initial attempt failed because `.build/gd-math-config` was absent.
- A local checkout was created to satisfy that prerequisite; config generation and Godot reimport completed.
- The build then exited with code 128 because `git pull --rebase` attempted SSH access and failed with `Host key verification failed` / repository access failure.
- Therefore, no newly produced devTesting APK was verified.

### Direct Godot fallback — observed but not completed

Selector used: `GDM_LEVEL_ID=mergeNumberUpTo7`, display `:99`.

- Godot launched using Mesa llvmpipe.
- The visible screen was a **Time Out** screen, not a playable `mergeNumberUpTo7` board.
- A retry produced the same visible state and process output included `Time OUT!`.
- No board or interactive tiles became available, so no move was performed.

## Result

**BLOCKED / NOT TESTED — `deviceTestFailed`**

- Boards tested: 0
- Tiles tested: 0
- Observed board time: Not measured
- Completion verified: No

## Findings

1. **Test environment blocker — build dependency/update path**
   - Status: blocked
   - The devTesting build cannot complete because its config checkout update requires unavailable SSH host-key/repository access.

2. **Test environment/runtime blocker — no playable direct-run board**
   - Status: blocked
   - The deterministic direct run reaches a visible Time Out state before the requested board is available.

These observations do not establish a gameplay defect in the level itself.

## Not tested

Gameplay, board enumeration, correct and incorrect interactions, level completion, TTS/audio, animation, performance, timing, Android touch behavior, and mobile rendering were not verified.

## Evidence

- Initial direct-run screenshot: `tester-data/artifacts/devTesting-mergeNumberUpTo7-20260910/00_initial.png`
- Retry screenshot: `tester-data/artifacts/devTesting-mergeNumberUpTo7-20260910/01_retry.png`
- Journal: `tester-data/journals/20260910-devTesting-mergeNumberUpTo7.jsonl`
