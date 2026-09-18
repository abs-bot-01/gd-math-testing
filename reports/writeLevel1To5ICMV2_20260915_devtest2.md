# QA Test Report

## Test Summary

Target: `writeLevel1To5ICMV2`  
Scope: first 10 boards  
Run: `writeLevel1To5ICMV2_20260915_devtest2`  
Result: **BLOCKED — 0/10 boards completed**

## Level Details

The exact `levels.yaml` entry was verified: `Writing Numbers 1 to 5 (icmV2)`, type `icmV2`, `leftVariant: characterTrace`, `rightVariant: numberTile`, and `boardCount: 10`.

The DevTest config was rebuilt using `GDM_TGT_ENV=dsg bash build.sh 1`, which exited successfully. The generated config verified two number objects per board. The rebuilt config was synchronized to the Godot runtime assets.

## Runtime Evidence

The source project was launched with `GDM_LEVEL_ID=writeLevel1To5ICMV2` on Xvfb. The runtime rendered the correct title and a playable tracing board containing numbers 4 and 3 with visible start knobs and trace paths.

A first-board screenshot was captured after the successful config rebuild. This confirms the previous empty-board blocker is resolved. The run was stopped before attempting further tracing in this clean verification run, so no board completion was claimed.

## Board Results

- Board 1: **RENDERED / NOT COMPLETED** — playable 4/3 tracing board visible.
- Boards 2–10: **NOT TESTED**.

## Screenshot Evidence

- `artifacts/writeLevel1To5ICMV2_20260915_devtest2/00_initial.png` — correct title and playable first board with visible 4 and 3 trace paths.

## QA Coverage

Identity: PASS — correct title visible.  
Configuration: PASS — exact record and 10-board configuration verified.  
Learning objective: PASS for rendering — number tracing content visible.  
Board layout: PASS.  
Visual content: PASS — number glyphs, start knobs, and trace paths visible.  
Image/asset quality: PASS for visible board.  
Alignment/scale/aspect ratio/safe margins: OBSERVED.  
Text/labels: PASS — title readable.  
Pointer interaction: NOT TESTED in this clean run.  
Hitboxes: NOT TESTED.  
Valid interaction: NOT TESTED.  
Invalid interaction: NOT TESTED.  
Solution validation: NOT TESTED.  
Visual feedback: NOT TESTED.  
Animation: NOT TESTED.  
Audio/TTS: NOT TESTED.  
Instructions/hints: NOT TESTED.  
Completion: BLOCKED — no board completion attempted in this run.  
Performance: PASS for rendered launch.  
Device/window quality: PASS — 1280×720 X11/Xvfb capture.

## Issues Found

The prior empty-board issue is not reproduced after rebuilding and synchronizing the DevTest config. Full gameplay coverage remains incomplete because the first 10 boards were not completed in this run.

## Overall Conclusion

The regenerated DevTest build now renders the requested level correctly, but this run did not complete the first 10 boards. Verified completion count: **0/10**. No source code or level configuration was modified; generated local runtime assets were refreshed for testing.

## Missing Evidence

- Before/after trace evidence for every stroke.
- Completion screenshots for boards 1–10.
- Full-level completion state.
- Invalid interaction, audio/TTS, and hints coverage.
