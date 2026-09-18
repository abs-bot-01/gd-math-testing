# Missing Representative Levels — Direct Godot Initial Render Report

- Run ID: `20260911-representative-missing-godot`
- Date: 2026-09-11
- Target: Godot 4.6.1 desktop via Xvfb `:99`
- Renderer: Mesa llvmpipe
- Scope: the 11 Representative Levels not covered by the previous `mergeNumberUpTo7` run

## Selection

The configuration contains 12 levels with the exact `representative` tag. `mergeNumberUpTo7` was previously tested, so this run covered the remaining 11:

1. `practicingDoubleTap`
2. `beforeAndAfter1To10`
3. `additionTable4`
4. `animalBirdWithCountTypeDH`
5. `sortRollSlideObjects`
6. `ssFormHundredsA3BOnes`
7. `ssA3B3MissingAWithoutCarry`
8. `mergeMatchHundredsOnesFrom100to999`
9. `grid4Row4Column`
10. `matchObjectWithFraction2`
11. `orderingFractions4`

## Initial rendering results

All 11 direct Godot processes logged `Started Level` with the requested level ID and expected title. Each produced a non-empty screenshot showing a rendered initial board.

| Level ID | Title | Initial board |
|---|---|---|
| `practicingDoubleTap` | Split & Fill! | Rendered / playable initial board observed |
| `beforeAndAfter1To10` | Before & After Numbers 1 to 10 | Rendered / playable initial board observed |
| `additionTable4` | Addition Table - Set 4 | Rendered / playable initial board observed |
| `animalBirdWithCountTypeDH` | Grid: Animal & Bird Labels | Rendered / playable initial board observed |
| `sortRollSlideObjects` | Sort Roll and Slide Objects | Rendered / playable initial board observed |
| `ssFormHundredsA3BOnes` | Addition: Make 100s With Ones | Rendered / playable initial board observed |
| `ssA3B3MissingAWithoutCarry` | Add without Carry Up to 999 - Set 2 | Rendered / playable initial board observed |
| `mergeMatchHundredsOnesFrom100to999` | Hear & Merge (100 to 999) - Set 2 | Rendered / playable initial board observed |
| `grid4Row4Column` | Growing Grid Challenge - Set 3 | Rendered / playable initial board observed |
| `matchObjectWithFraction2` | Match Fraction Munchies - Set 2 | Rendered / playable initial board observed |
| `orderingFractions4` | Arrange Fractions - Set 4 | Rendered / playable initial board observed |

## Result

**PARTIAL — initial rendering only**

- Levels launched: 11/11
- Initial boards rendered: 11/11
- Full levels completed: 0/11
- Gameplay moves completed: 0/11
- Android testing: not performed in this run

This run confirms level selection, deterministic launch, runtime ID/title logging, and initial board rendering. It does not establish full-level PASS results.

## Not tested

For all 11 levels, the following remain untested:

- complete correct solution;
- every configured board;
- per-action acceptance;
- invalid interaction and recovery;
- rapid/repeated interaction;
- board completion and full-level completion;
- audio/TTS;
- performance/timing;
- Android rendering/touch/device behavior.

## Evidence

Evidence directory:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/representative-missing-godot-20260911/`

It contains one initial screenshot for each of the 11 levels plus `contact_sheet.png`.

Journal:
`/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/20260911-representative-missing-godot.jsonl`
