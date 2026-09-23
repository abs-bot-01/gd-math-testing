# Run Flow — mergeNumberUpTo5Lo one-board test

- Runtime config and source config identified `mergeNumberUpTo5Lo`; runtime reported 10 configured boards.
- Direct source launch used `DISPLAY=:1052 GDM_LEVEL_ID=mergeNumberUpTo5Lo godot --path /home/abs-bot-01/dev/gd-math-godot`.
- Board 1 rendered with title `ADD 1 TO GET NUMBERS UP TO 5 - LO` and three rows: `4+1=5`, `4+1=5`, and `1+1=2`; destination values were `2`, `5`, and `5`.
- All three merges were accepted, producing result tiles `5`, `5`, and `2`.
- The `2` result was dragged toward the top `2` slot using a paced path around the visible brick platform. The result became an oversized/rotated white tile near the right side instead of settling in the slot.
- After a four-second wait, the top slot remained unresolved and the board did not advance. The board was blocked before completion; no further blind retries were made.
