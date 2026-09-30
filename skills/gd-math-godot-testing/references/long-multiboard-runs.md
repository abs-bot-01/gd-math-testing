# Long Multi-Board Runs

Use this reference when a configured level has enough boards or actions that one agent turn may exhaust its tool-iteration or wall-clock budget.

## Procedure

1. Parse the exact source and runtime board count before launching. Record the requested scope separately from the configured count.
2. Create one run directory, event stream, artifact directory, plan path, and a partial report path before starting the game.
3. Launch one persistent session with the supported level selector. Do not relaunch between boards unless the runtime itself fails.
4. At each board boundary, wait for the new board and transient reward/particle overlays to clear. Capture a stable screenshot and compute its SHA-256.
5. Map every current source, category, target, and open target slot from that screenshot. Store the mapping and screenshot hash in the plan/event stream before sending input.
6. Execute the board's complete action sequence with fixed pacing. Capture and inspect one settled post-action state per move, even when the image is transient and not retained in the standard evidence profile.
7. Count a move only when the source is resolved and the object remains in the correct open target area. If a move is rejected, allow one planned alternate target/route, then stop the board if it remains unresolved.
8. After the final move, verify all active objects are resolved and a new board or explicit terminal state appears. Record the board terminal event before continuing.
9. Checkpoint after each small batch of boards: flush events, update `flow.md`, write the current partial report, and record the next board index, current screenshot path/hash, plan path, process/display state, and cleanup status.
10. On resume, verify that the recorded process/display/session is still alive and that the checkpoint screenshot hash matches the live checkpoint. Otherwise start a fresh run and remap; never continue from stale coordinates.
11. After the final configured board, require the visible full-level completion state. Then stop the launcher and child game process, stop Xvfb, validate artifacts, and finalize the report.

## Recommended profiles

| Profile | Retained evidence | Use |
|---|---|---|
| Speed coverage | Initial and board-terminal screenshots; transient post-action captures may be deleted after review | Full configured-board smoke/functional coverage |
| Evidence retest | Initial plus one settled post-action screenshot per move | Failed boards, regressions, and control-board verification |

A speed run is not blind playback: it reduces retained files and model turns, not visual acceptance checks. Prefer a board-batch runner or a single mechanical command for repetitive drags, but keep source mapping and acceptance decisions live at every board boundary.

## Report checkpoint minimum

Every checkpointed partial report should state:

- configured boards, requested boards, completed boards, and current board;
- accepted, rejected, retried, and unverified action counts;
- the exact run, plan, event, and artifact paths;
- whether cleanup is complete;
- missing evidence and the next resumable step.

Use `PARTIAL / INCOMPLETE` until every configured board and the final completion state are verified. Never turn a process exit, changed image hash, or one completed board into a full-level PASS.
