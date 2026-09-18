# Recent Testing Report

**Reporting period:** 10–11 September 2026  
**Target:** GD Math Godot application  
**Primary runtime:** Godot 4.6.1 desktop, Xvfb, Mesa llvmpipe  
**Scope:** Recent desktop gameplay, regression, representative-level, and Android retest activity

## Status marker

> **PARTIAL / INCOMPLETE — desktop rendering is broadly verified, but no recent multi-board/full-level regression pass is complete. Android coverage remains blocked.**

## Executive summary

- Recent runs launched the application and rendered the requested initial boards successfully across the tested desktop targets.
- One focused level, `writeLevelIntroduction`, passed its complete one-board desktop flow.
- `mergeNumberUpTo7` verified merge, result placement, and transition from board 1, but not completion of its configured 10-board level.
- The 11-level representative gameplay run produced evidence for 8 levels and was blocked before gameplay for 3; no full-level pass was verified.
- The GD Math regression run rendered all 5 requested initial boards, but did not achieve a full-level pass.
- Android testing was blocked by either no authorized ADB target or a black-screen Vulkan presentation failure.
- No application source or project files were modified during the reported tests.

## Recent run results

| Run / target | Result | Verified | Not verified or blocked |
|---|---|---|---|
| `writeLevelIntroduction` desktop | **PASS** | 1/1 board completed; both trace paths accepted; completion/home state shown | Android, invalid trace, audio, performance |
| `mergeNumberUpTo7` desktop rerun | **PARTIAL** | Board 1 transition; merge and correct result placement for exercised rows; board 2 reached | Full 10-board completion, Android, negative cases, audio, performance |
| 11 representative levels | **PARTIAL / INCOMPLETE** | Gameplay evidence for 8/11 levels | 3 blocked before gameplay; 0 full-level completions |
| `animalBirdWithCountTypeDH` desktop | **PARTIAL / INCOMPLETE** | First board rendered; Type/Count UI visible; interaction attempts captured | 0/10 boards completed; accepted answers not verified |
| GD Math regression — 5 levels | **FAIL / INCOMPLETE** | 5/5 initial boards rendered | 0 full-level passes; fruit drag and shape completion unresolved; 3 levels only rendered |
| `writeLevelIntroduction` Android retest | **BLOCKED** | APK installed; emulator available | Fresh launch black screen; `QueuePresentKHR failed with error: 5` |

## Detailed findings

### Confirmed positive coverage

1. **Application launch and initial rendering**
   - The requested desktop levels opened and displayed usable initial boards in the recent runs.
   - The 5-level GD Math regression rendered all 5 requested initial boards.

2. **Completed desktop level**
   - `writeLevelIntroduction` completed its only configured board.
   - Both vertical line-tracing paths were accepted.
   - The app transitioned to a visible completion/home state.

3. **Partial arithmetic gameplay**
   - `mergeNumberUpTo7` accepted exercised merge and matching-result placement actions.
   - A transition from board 1 to a subsequent board was verified.

### Open gameplay issues or incomplete coverage

- `stackVegetablesAndFruitsSet1`: an orange tile remained in the source area after two drag attempts; accepted placement was not verified.
- `stackBasicShapes`: six drag attempts did not produce a verified completion transition; the final board remained unsolved or misplaced.
- `animalBirdWithCountTypeDH`: the board appears to use spinner/tap interaction, but no accepted Type or Count answer was verified.
- Representative arithmetic, fraction, grid, and matching levels generally produced interaction evidence without verified full-level completion.
- Audio/TTS, performance, animation timing, invalid-interaction recovery, and complete configured-board coverage remain unverified.

### Android blocker

- Some runs had no authorized device or emulator in `adb devices -l`.
- The `writeLevelIntroduction` retest used an available emulator and installed APK, but launch produced a black screen. Logcat reported `QueuePresentKHR failed with error: 5`.
- Android install, rendering, touch, layout, and performance coverage therefore remains blocked.

## Coverage summary

- Recent representative levels: **11 requested; 8 with gameplay evidence; 3 blocked before gameplay; 0 full-level completions**.
- GD Math regression levels: **5 requested; 5 initial boards rendered; 0 full-level passes**.
- Focused completed desktop level: **1/1 configured board completed for `writeLevelIntroduction`**.
- Recent confirmed full-level passes overall: **1 focused desktop level**.

## Evidence and source reports

All paths below are under `/home/abs-bot-01/Hermes/hermes-tester/tester-data/`.

- `reports/rep-gameplay-20260911-consolidated.md`
- `reports/gd-math-regression-20260911.md`
- `reports/20260911-animalBirdWithCountTypeDH-godot.md`
- `reports/20260911-writeLevelIntroduction-godot.md`
- `reports/20260911-writeLevelIntroduction-retest.md`
- `reports/20260910-devTesting-mergeNumberUpTo7-rerun.md`
- `artifacts/rep-gameplay-20260911/`
- `artifacts/gd-math-regression-20260911/`
- `artifacts/writeLevelIntroduction-godot-20260911/`

## Recommended next actions

1. Re-run the unresolved fruit and shape levels using destination-center drops and fresh board-coordinate mapping.
2. Complete every configured board before assigning a full-level PASS.
3. Determine the intended spinner/tap interaction for `animalBirdWithCountTypeDH` and verify an accepted Type and Count answer.
4. Resolve the Android Vulkan/black-screen issue and repeat APK launch and touch coverage on an authorized target.
5. Add audio/TTS, invalid-interaction, and performance checks after core gameplay transitions are stable.

## Final assessment

The recent testing establishes meaningful desktop rendering coverage and a small amount of verified gameplay, including one complete single-board desktop level. It does **not** establish a passing regression baseline for the broader level set. The overall status remains **PARTIAL / INCOMPLETE**, with gameplay completion and Android rendering as the main outstanding areas.
