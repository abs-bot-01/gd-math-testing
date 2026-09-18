# Render Check Report — `writeLevel1To5ICMV2`

## Test Summary

- Run ID: `20260915-render-check-writeLevel1To5ICMV2`
- Scope: rendering check for Boards 1–5
- Runtime: Godot source project with `GDM_LEVEL_ID=writeLevel1To5ICMV2`, Xvfb display `:1047`
- Result: **FAIL / BLOCKED — Board 1 is not rendering correctly; Boards 2–5 were not reachable**

## Expected Rendering

The exact authoritative configuration specifies:

- Title: `Writing Numbers 1 to 5 (icmV2)`
- Type: `icmV2`
- Variants: `characterTrace` → `numberTile`
- Board count: 10
- Expected Board 1 content: visible number glyphs, trace paths/start knobs, and usable tracing content.

## Observed Rendering

The runtime displayed only a wooden board and garbled header text (`SDWDWDWDS`). It did not display number glyphs, trace paths, start knobs, instructions, or usable gameplay controls. The same state remained after an additional wait.

Runtime JSON inspection before launch showed that `assets/config.json` did not contain the exact `writeLevel1To5ICMV2` entry. It contained only related keys `writeLevel1To5` and `writeLevel1To52AL`.

## Board Results

- Board 1: **FAIL / BLOCKED** — board background rendered, but expected tracing content was missing.
- Boards 2–5: **NOT TESTED / NOT REACHABLE** — Board 1 did not render as a playable board, so no valid transition could be performed.

## Finding

**Finding ID:** `writeLevel1To5ICMV2-runtime-config-missing-rendering`  
**Status:** `new`  
**Severity:** critical  
**Confidence:** high  
**Expected:** Boards 1–5 of the exact requested level render their configured number-tracing content.  
**Actual:** The runtime lacks the exact level key and renders an empty wooden board with garbled text; no Board 1 gameplay content appears after waiting.  
**Reproduction:** Launch `DISPLAY=:1047 GDM_LEVEL_ID=writeLevel1To5ICMV2 godot --path /home/abs-bot-01/dev/gd-math-godot`; wait at least 18 seconds; capture the window.  
**Evidence:** `artifacts/20260915-render-check-writeLevel1To5ICMV2/board01_initial.png`, `artifacts/20260915-render-check-writeLevel1To5ICMV2/board01_after_wait.png`  
**Likely cause:** The generated runtime config was not synchronized with the exact `writeLevel1To5ICMV2` configuration entry.

## Evidence

- `artifacts/20260915-render-check-writeLevel1To5ICMV2/board01_initial.png`
- `artifacts/20260915-render-check-writeLevel1To5ICMV2/board01_after_wait.png`
- Journal: `journals/20260915-render-check-writeLevel1To5ICMV2.jsonl`

## Conclusion

The check found a rendering failure on Board 1. Boards 2–5 could not be checked because the first board was not playable. No source code or level configuration was modified.
