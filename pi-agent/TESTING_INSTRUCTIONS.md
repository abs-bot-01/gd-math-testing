# Pi-agent execution brief

Use this brief when starting a GD Math Godot test from this project.

Load the local skills first. Keep every persistent file under the project root. Use the configured target only as a read-only application/configuration input.

## Exact procedure

1. Resolve the exact level ID in the authoritative source configuration and runtime `assets/config.json`. Parse ID-keyed and list-shaped runtime layouts correctly.
2. Locate and read the exact evidence contract. Do not substitute a similarly named document.
3. Confirm the project, Godot, Xvfb, `xdpyinfo`, `xdotool`, and ImageMagick `import` prerequisites.
4. Create one unique run directory with a plan, `events.jsonl`, `flow.md`, and `artifacts/` under `tester-data/runs/`.
5. Launch once with `GDM_LEVEL_ID=<level-id>` on a fresh Xvfb display. Wait for a visibly rendered board, not merely a live process or a non-empty image.
6. Capture the stable initial board and confirm the displayed title/identity.
7. Derive the complete solution mapping from that current screenshot. Distinguish draggable objects from fixed/support objects and use the level's documented rule.
8. Perform one native `xdotool` transaction at a time with a hold, at least two waypoints, a settle wait, and a post-action capture.
9. Visually verify acceptance. For merge boards, verify the merge result has settled before placing it and map the result by value to the current target slot.
10. Re-map after every board transition. Never replay coordinates from another board or run.
11. If a valid action is rejected, make one fresh bounded recovery using a new live map. Stop if the state remains unresolved or malformed.
12. Stop at the requested boundary. Treat an unexpected extra playable board after the configured final board as a completion-boundary FAIL, not as a completion signal.
13. Stop the Godot process and its children, stop Xvfb, and verify the display is unreachable.
14. Validate JSONL, screenshots, report links, configured/requested/completed board counts, and findings before reporting.

## Backend statement to put in the run metadata

```text
input_backend: xdotool
screenshot_backend: ImageMagick import on Xvfb root
visual_review_backend: Pi-agent vision or explicit human review
orchestration_backend: local deterministic_level_runner.py
computer_use_invoked: false
```

Change only the values that are actually observed. Do not claim a backend merely because the tool exists.
