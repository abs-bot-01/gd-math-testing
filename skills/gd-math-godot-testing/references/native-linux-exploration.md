# Native Linux Godot exploration

This setup uses native X11 tooling as its normal desktop path. Keep the target application on a validated user-owned Xvfb display and keep all persistent evidence below `tester-data/`.

## Normal path

1. Validate the display with `xdpyinfo`.
2. Launch Godot with the exact level selector.
3. Capture the X11 root with ImageMagick `import`.
4. Derive current coordinates from the screenshot.
5. Send input with `xdotool` and a paced multi-waypoint gesture.
6. Capture and visually review the settled result.

Do not treat a live process, active window, or successful command exit as proof that the board rendered or accepted input.

## Window and canvas behavior

Godot canvas controls may expose little or no accessibility metadata. Use current screenshot coordinates only after visually identifying the source and target. Do not rely on stale window IDs or coordinates after a process restart or board transition.

Do not make `_NET_ACTIVE_WINDOW` or window activation a prerequisite under minimal Xvfb. Route input to the validated display and judge acceptance from before/after visual state.

## Alternate backend

An alternate desktop backend is outside the default contract. Use it only when native X11 cannot reach the validated display and the user explicitly authorizes the deviation. Record the actual backend in the run metadata. A tool catalog or documentation mention is not evidence that it was invoked.
