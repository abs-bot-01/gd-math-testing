# Input-method provenance

Record the backend actually used by the test, not every tool that was available.

## Default backend

For this setup the default gameplay backend is native X11:

```text
input_backend: xdotool
screenshot_backend: ImageMagick import on Xvfb root
visual_review_backend: Pi-agent vision or explicit human review
orchestration_backend: scripts/deterministic_level_runner.py
computer_use_invoked: false
```

The runner's drag implementation issues `xdotool mousemove --sync`, `mousedown`, paced waypoint moves, and `mouseup`. The runner also uses `xdotool` for window/display checks. Screenshots use ImageMagick `import`; screenshots are not input.

## Computer-use rule

Do not use `computer_use` for ordinary GD Math gameplay in this project. If a user explicitly authorizes a different backend, record it in the run metadata and explain why native X11 was unavailable. A `tool_search` result, skill catalog entry, or documentation mention of `computer_use` is not an invocation.

## Audit rule

For a post-run backend question:

1. inspect the run's `events.jsonl` and plan;
2. inspect the exact session transcript if available;
3. inspect the runner implementation when input is encapsulated;
4. count only actual invocations and executed commands within the test scope;
5. exclude later report/counting turns.

Report input, screenshot, visual review, and orchestration channels separately.
