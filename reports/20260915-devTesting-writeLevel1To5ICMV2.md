# DevTesting Report — `writeLevel1To5ICMV2`

## Run

- Run ID: `20260915-devTesting-writeLevel1To5ICMV2`
- Target: `/home/abs-bot-01/dev/gd-math-godot`
- Procedure followed: tester-data DevTesting procedure — `./buildMaker.sh devTesting main`, then direct Godot fallback with `GDM_LEVEL_ID`.
- Requested scope: first 10 boards with screenshots.

## Result

**BLOCKED — 0/10 boards completed.**

## Configuration

The authoritative `levels.yaml` record was verified:

- ID: `writeLevel1To5ICMV2`
- Title: `Writing Numbers 1 to 5 (icmV2)`
- Type: `icmV2`
- Variants: `characterTrace` → `numberTile`
- Configured boards: 10
- Board time: 18 seconds

## DevTesting build procedure

Command executed:

```bash
./buildMaker.sh devTesting main
```

Observed result:

- Config generation completed.
- `checkBuildAssets` passed: 2 tests passed.
- Webpack completed with warnings only.
- Godot project reimport completed.
- The overall procedure exited with code **128** because the config update attempted SSH `git pull --rebase` and failed with `Host key verification failed` / repository access failure.
- No newly produced APK was verified.

## Direct Godot fallback

The direct source run was launched with:

```bash
DISPLAY=:1046 GDM_LEVEL_ID=writeLevel1To5ICMV2 godot --path /home/abs-bot-01/dev/gd-math-godot
```

The runtime rendered a wooden board with garbled text (`SDWDWDWDS`) and no visible number glyphs, trace paths, start knobs, instructions, or playable controls. An additional 10-second wait produced the same empty board.

A runtime inspection also showed that the current `assets/config.json` did **not** contain the exact `writeLevel1To5ICMV2` key; only related `writeLevel1To5` and `writeLevel1To52AL` keys were present. Therefore, the requested level was not actually loaded by the runtime.

## Board results

- Board 1: **BLOCKED** — no playable content rendered.
- Boards 2–10: **NOT TESTED** — Board 1 could not be started.
- Completed: **0/10**.

## Evidence

- `/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/20260915-devTesting-writeLevel1To5ICMV2/00_initial.png`
- `/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/20260915-devTesting-writeLevel1To5ICMV2/01_after_wait.png`
- Journal: `/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/20260915-devTesting-writeLevel1To5ICMV2.jsonl`

## Conclusion

Following the tester-data DevTesting procedure exposed a configuration/build blocker before gameplay: the build procedure failed during the config checkout update, and the fallback runtime did not contain the exact requested level key. The screenshots are launch/render evidence only; no gameplay completion claim is made. No source code or level configuration was modified.
