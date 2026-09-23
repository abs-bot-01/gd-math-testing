# Run Flow — mergeNumberUpTo5Lo timed retest

- Fresh direct launch used `DISPLAY=:1054 GDM_LEVEL_ID=mergeNumberUpTo5Lo godot --path /home/abs-bot-01/dev/gd-math-godot`.
- Board 1 rendered with live rows `2+1=3`, `1+1=2`, and `4+1=5`; destination values were `3`, `5`, and `2`.
- All three merges completed after allowing the final merge animation to settle, producing results `3`, `2`, and `5`.
- The top target platform was observed near the edge of the target and the result `3` was dragged directly into the top `3` slot.
- The result became an oversized/rotated white tile over the top destination. After four seconds, the slot remained unresolved and the board did not advance.
- Board 1 was not completed; no further blind retries were made.
