---
name: native-x11-input
description: Send verified Godot input through isolated X11 displays.
version: 1.0.0
author: Project Maintainer, Pi-agent
license: MIT
platforms: [linux]
metadata:
  tags: [x11, xvfb, xdotool, godot, drag-drop]
---

# Native X11 Input

Use this skill for GD Math desktop input. It sends real X11 pointer events to the validated Xvfb display and keeps screenshots, visual review, and input provenance separate. It does not use `computer_use` by default.

## Prerequisites

Verify the target display with `xdpyinfo` and require `xdotool` and ImageMagick `import`. Use a fresh user-owned Xvfb display whenever possible. Keep all evidence under `tester-data/` in the setup project.

## Drag contract

For each current screenshot-derived source/target pair:

```text
export DISPLAY=<validated-display>
xdotool mousemove --sync <source-x> <source-y>
xdotool mousedown 1
sleep <hold>
xdotool mousemove --sync <waypoint-1-x> <waypoint-1-y>
sleep <step>
xdotool mousemove --sync <waypoint-2-x> <waypoint-2-y>
sleep <step>
xdotool mousemove --sync <target-x> <target-y>
sleep <step>
xdotool mouseup 1
sleep <settle>
DISPLAY=<validated-display> import -window root <post-action.png>
```

Use at least two intermediate waypoints even when no obstacle is visible; Godot's drag recognizer may reject a direct jump. Export `DISPLAY` for the whole sequence, not only the first command. Release well inside the currently open destination area.

Bound synchronous pointer moves with a short timeout. If a move stalls while the button is down, immediately send `xdotool mouseup 1` on the validated display, capture the post-release state, and classify the gesture as interrupted/unverified. Do not call it a gameplay rejection until the screenshot shows the resulting state.

## Verification

A command exit code is mechanical evidence only. Accept a move only when a fresh screenshot shows stable centered placement, source consumption, target resolution, feedback, or board transition. If a move is rejected, re-map from the fresh state and allow one bounded recovery.

## Obstacles and animation

Capture immediately before a drop and compare consecutive frames when a LivingObject can overlap the path or target. Start during a clear outbound phase and route around the moving body. If a valid result becomes malformed or leaves the target unresolved after one clear-window recovery, record the defect and stop.

## Backend audit

Record these fields per run:

```text
input_backend=xdotool
screenshot_backend=ImageMagick import
computer_use_invoked=false
```

If a different input tool is authorized, change the fields to observed values and explain the deviation. Never infer that `computer_use` was used from an available-tool list.
