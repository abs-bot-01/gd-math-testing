# Representative Level Gameplay Test — Consolidated Report

- Run ID: `rep-gameplay-20260911-consolidated`
- Target: Godot 4.6.1 desktop via Xvfb; Mesa llvmpipe
- Scope: 11 missing Representative Levels
- Existing Run Document: unchanged
- Application code: unchanged during these tests

## Overall result

**PARTIAL / INCOMPLETE.**

All requested levels had previously rendered initial boards. This gameplay run produced partial interaction evidence for 8 levels and was blocked before gameplay for 3 levels. No full configured level was completed and no full-level PASS is claimed.

## Per-level results

| Level ID | Configured boards | Result | Verified scope |
|---|---:|---|---|
| `practicingDoubleTap` | 6 | PARTIAL | Split interaction, visible pieces, and transition to board 2 observed; full level incomplete |
| `beforeAndAfter1To10` | 6 | PARTIAL | Invalid and correct attempts captured; board remained incomplete |
| `additionTable4` | 6 | BLOCKED | Gameplay preflight did not complete; no board interaction verified |
| `animalBirdWithCountTypeDH` | 10 | BLOCKED | Gameplay preflight did not complete; no board interaction verified |
| `sortRollSlideObjects` | 10 | BLOCKED | Gameplay preflight did not complete; no board interaction verified |
| `ssFormHundredsA3BOnes` | 5 | PARTIAL | Board rendered; no accepted state transition verified |
| `ssA3B3MissingAWithoutCarry` | 5 | PARTIAL | Three drag attempts captured; no accepted move or completion verified |
| `mergeMatchHundredsOnesFrom100to999` | 10 | PARTIAL | Board rendered; attempted drag rejected; audio matching not completed |
| `grid4Row4Column` | 3 | PARTIAL | Multiple placement attempts captured; no completion state verified |
| `matchObjectWithFraction2` | 10 | PARTIAL | Multiple picture/fraction moves captured; no completion state verified |
| `orderingFractions4` | 6 | PARTIAL | Fraction ordering attempts captured; no completion state verified |

## Coverage totals

- Levels requested: 11
- Levels with gameplay evidence: 8
- Levels blocked before gameplay: 3
- Full-level completions: 0
- Full-level PASS results: 0
- Full configured-board coverage: not achieved

## Evidence

Primary evidence directory:

`/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/rep-gameplay-20260911/`

Subdirectories exist for all levels with gameplay evidence:

- `practicingDoubleTap/`
- `beforeAndAfter1To10/`
- `ssFormHundredsA3BOnes/`
- `ssA3B3MissingAWithoutCarry/`
- `mergeMatchHundredsOnesFrom100to999/`
- `grid4Row4Column/`
- `matchObjectWithFraction2/`
- `orderingFractions4/`

The earlier initial-render evidence for all 11 levels is under:

`/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/representative-missing-godot-20260911/`

## Not tested or incomplete

- Full configured-board completion for every level
- Full-level completion screens
- Android rendering and touch behavior
- Audio/TTS correctness
- Performance/timing
- Complete invalid-interaction and recovery matrix

A completed or changed board state was not treated as full-level completion. Environment and interaction blockers are reported separately from confirmed gameplay defects.

Journal:

`/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/rep-gameplay-20260911-consolidated.jsonl`
