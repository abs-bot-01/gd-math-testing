---
name: gd-math-godot-testing
description: Test GD Math Godot levels with verified X11 input.
version: 1.0.0
author: Project Maintainer, Pi-agent
license: MIT
platforms: [linux]
metadata:
  tags: [godot, gd-math, qa, x11, xdotool, evidence]
  references:
    - references/vertical-report-and-drag-drop.md
    - references/living-object-drop-debugging.md
    - references/long-multiboard-runs.md
    - references/post-run-analysis.md
---

# GD Math Godot Testing

Use this local skill for every GD Math Godot gameplay or regression test. It defines a fixed, evidence-backed desktop flow for Pi-agent and intentionally keeps setup state inside this project. It does not modify the application under test and does not require a system-level skill installation.

## When to use

Use for launching, rendering, interacting with, retesting, or reporting a GD Math Godot level. Do not use it to claim Android, touch, production, or device behavior from a desktop Xvfb run.

## Required local files

Read these before gameplay:

- `docs/architecture.md`
- `docs/setup.md`
- `docs/deterministic-level-testing.md`
- `docs/context-retrieval-workflow.md`
- `skills/native-x11-input/SKILL.md`
- `skills/evidence-qa-reporting/SKILL.md`
- the relevant files under `references/`

## Backend contract

The default backend is:

```text
input_backend: xdotool
screenshot_backend: ImageMagick import on Xvfb root
visual_review_backend: Pi-agent vision or explicit human review
orchestration_backend: scripts/deterministic_level_runner.py
computer_use_invoked: false
```

Do not use `computer_use` for ordinary gameplay. If an alternate backend is explicitly authorized, record it as an observed run value. A catalog entry, loaded skill, or tool-search result is not an invocation.

## State machine

Use exactly:

`preflight -> launch -> board_ready -> live_mapping -> action_transaction -> visual_verification -> board_terminal -> final_visual_review -> cleanup -> artifact_validation`

The run is not a PASS until visual review, terminal state, cleanup, and artifact validation all succeed.

## Procedure

1. **Resolve identity.** Match the exact requested ID in the authoritative source configuration and the runtime `assets/config.json`. Parse ID-keyed and list-shaped runtime layouts. Record title, type, variants, board count, rule, and requested scope. Stop configuration claims if the exact ID is absent or mismatched.
2. **Retrieve context.** Follow `docs/context-retrieval-workflow.md`. Read the relevant testing/quality, mechanic, runtime, representative, and LivingObject/support-object context only when it answers a current question. Record source conflicts.
3. **Create the run.** Use `scripts/new_run.py` or create a unique directory under `tester-data/runs/<run-id>/`. Keep `plan.json`, `events.jsonl`, `flow.md`, and `artifacts/` together. Do not use stale coordinates or prior screenshots.
4. **Preflight.** Run `scripts/preflight.py`. Verify the project and configuration paths, Godot, Xvfb, `xdpyinfo`, `xdotool`, ImageMagick `import`, display, resolution, and board scope. Keep application and configuration trees read-only.
5. **Launch.** Prefer the direct source-project selector: `GDM_LEVEL_ID=<id> godot --path <project>` on a fresh Xvfb display. Use one bounded readiness wait and one rendered-board probe. A live process, window, non-empty image, or mostly-black loader is not a playable board.
6. **Capture and map.** Capture one stable full-board screenshot. Confirm the displayed title/ID. Enumerate every visible draggable object, fixed reference/support object, destination, label, rule, and moving obstacle. Write the complete source-to-destination mapping before the first move.
7. **Execute one action.** Use the deterministic runner or the local X11 skill. Move from the current live source to a verified open destination with a hold, at least two waypoints, a settle wait, and one post-action capture. Do not send a blind plan made from another board.
8. **Verify visually.** Require the tile/object to remain centered and accepted, the source to be consumed or resolved, the target to resolve, or a verified board transition. `xdotool` success and image-hash changes are not acceptance.
9. **Handle failure once.** On an explicit rejection, unchanged board, obstacle timing miss, or malformed result, recapture the current state, rebuild the mapping, and allow one bounded recovery. If the state remains unresolved, record a finding and stop instead of adding retries.
10. **Remap transitions.** After every board transition, wait for the new board and transient overlays to settle, capture a fresh stable checkpoint, hash it, and derive a new mapping. Never reuse row order, source positions, or target coordinates.
11. **Respect boundaries.** A completed board is not a full-level completion. If the final configured board reveals another playable board instead of a terminal state, capture it, classify the completion boundary as FAIL/INCOMPLETE, and do not interact with the extra board unless scope is explicitly expanded.
12. **Clean up.** Terminate the launcher and child Godot process, stop Xvfb, and verify the display is unreachable. Checking only a wrapper PID is insufficient.
13. **Report and validate.** Write `flow.md`, the report, and structured findings. Run `scripts/validate_run.py`. Reconcile requested scope, configured boards, completed boards, actions, retries, findings, evidence, and missing tests.

## Mechanic rules

- **Sorting:** use the documented visual/physical rule, such as 2D outline or Roll/Slide behavior. Do not drag fixed support tiles merely because they look similar.
- **Merge-and-fill:** drag the larger/base source onto the smaller addend unless the live contract shows otherwise. Wait for both inputs to be consumed and the result to remain stable. Map result value to the current matching slot, not necessarily the row where it was merged.
- **Stacked/group targets:** release well inside the currently open target area. Re-map the open area after every accepted placement; the geometric center may be occupied.
- **LivingObject obstacles:** observe a complete movement cycle. Start only while the object is fully beyond the target and moving away. Route around its current body. A valid tile that becomes oversized, rotated, misplaced, or unresolved after a clear-window attempt is a finding, not a reason for blind retries.
- **Tracing/writing:** follow the live path from the current knob using small incremental moves; verify the completion effect and transition.

## Evidence profiles

Use `per-action` when the user requests movement evidence or a defect investigation. Retain exactly one settled post-action image per action plus initial/terminal evidence. Use `completion-only` for fast coverage; still verify every action transiently and retain initial/final evidence. Keep the same profile in prepare and execute phases.

## Verification checklist

Before reporting:

- exact ID/title/source/runtime match recorded;
- current board mapping recorded for every tested board;
- every action has an event and visible acceptance/rejection result;
- screenshot paths cited by the report exist and are non-empty;
- JSONL parses completely;
- findings have matching structured records;
- cleanup and display shutdown verified;
- requested/configured/completed board totals reconcile;
- untested audio, invalid interaction, hints, performance, accessibility, Android, and device areas are stated;
- no application source/configuration files changed.

See `docs/report-contract.md` and the linked references for report shape and edge cases.
