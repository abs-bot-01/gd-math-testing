# Deterministic GD Math level testing

Use one fixed state machine while solving every board from its live rendered state. Deterministic means fixed orchestration, timing, branching, and evidence rules; it does not mean fixed coordinates. Randomized boards must be mapped again from the current screenshot.

## State machine

`preflight -> launch -> board_ready -> live_mapping -> action_transaction -> visual_verification -> board_terminal -> final_visual_review -> cleanup -> artifact_validation`

## Two-phase runner

1. Create a unique run directory and a plan with the exact level ID, target project, display, resolution, board scope, and empty action lists.
2. Run `--prepare --start-xvfb` with `--retain-action-screenshots` when action-by-action evidence is required. Keep the live session alive.
3. Inspect the retained initial screenshot. Confirm title, rule, draggable sources, support objects, targets, obstacles, and current coordinates.
4. Fill the current board's live actions, add its exact `initial_screenshot_sha256`, and set `live_mapping_verified: true`.
5. Execute one action at a time. The runner captures a settled post-action image and pauses for review.
6. Approve only after visual acceptance. Use `--retry-action` no more than once for a visibly rejected action.
7. After a board transition, capture a stable new board and rebuild the mapping. Never reuse the prior board's coordinate order.
8. On the last configured board, require a visible terminal completion state. If another playable board appears, capture it as mismatch evidence and report FAIL/INCOMPLETE.
9. Stop the Godot process and Xvfb, verify no matching processes remain, and validate artifacts.

## Live mapping

Write the complete mapping before the first move:

```text
source object/value/category -> destination slot/group/open target area
```

For sorting, distinguish draggable objects from fixed reference/support tiles. For shapes, use the visible outline rule rather than semantic meaning. For merge-and-fill boards, merge the larger/base source onto the smaller addend first, wait for the result to settle, then map the result by value to the current target slot.

## Action transaction

Every state-changing action must:

1. export the validated `DISPLAY`;
2. move to the live source with `xdotool`;
3. press and hold the button;
4. use at least two intermediate waypoints;
5. release well inside the currently open destination area;
6. wait the fixed settle interval;
7. retain or transiently capture one post-action screenshot;
8. visually verify centered placement, source consumption, target resolution, feedback, or board transition.

Do not count a move because `xdotool` returned zero, because the source disappeared, or because the image hash changed. Reward animation can change the image while the target remains unresolved.

## Bounded failure handling

Branch only on explicit observations: loader/no board, unchanged/rejected action, moving obstacle, malformed result, or completion/transition. Re-capture the current state, derive a fresh source/target map, and make at most one bounded recovery. If the result remains displaced, oversized, rotated, or unresolved, record a finding and stop instead of guessing.

## Evidence profiles

- **Completion-only:** keep initial-board and final completion/transition evidence; action captures may be transient.
- **Per-action:** keep exactly one settled post-action screenshot per action, plus initial and terminal evidence. Use this when the user asks for detailed movement evidence or a defect investigation.

The setup defaults to per-action because it mirrors the verified previous runs. The profile must be consistent between `--prepare` and `--execute`.

## Validation

Run `scripts/validate_run.py`. It must verify valid JSONL, a readable report, non-empty cited screenshots, matching action/evidence records, cleanup, and requested/configured/completed board counts. Report what was not tested.
