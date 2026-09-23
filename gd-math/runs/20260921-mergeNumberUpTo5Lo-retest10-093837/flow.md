# Run Flow — mergeNumberUpTo5Lo retest

- Runtime source and generated config both report 10 boards for `mergeNumberUpTo5Lo`.
- Direct desktop launch used `DISPLAY=:1042 GDM_LEVEL_ID=mergeNumberUpTo5Lo godot --path /home/abs-bot-01/dev/gd-math-godot`.
- Board 1 rendered with live rows `3+1=4`, `4+1=5`, and `4+1=5`.
- The top-row `3+1` merge was accepted and produced result `4`.
- Placing result `4` into the bottom `4` slot again produced a large rotated/oversized tile over the target. The malformed state persisted after a four-second wait.
- This reproduces the prior result-placement defect with a different value/target geometry. No blind retry was made; Board 1 remained unresolved and Boards 2–10 were not tested.
