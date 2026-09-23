# Run Flow — mergeNumberUpTo5 normal one-board test

- Fresh direct source launch used `DISPLAY=:1059 GDM_LEVEL_ID=mergeNumberUpTo5 godot --path /home/abs-bot-01/dev/gd-math-godot`.
- Exact normal level rendered: `mergeNumberUpTo5`, title `Add 1 to Get Numbers Up to 5`, configured board count 10.
- Board 1 rendered with rows `1+1=2`, `2+1=3`, and `4+1=5`; no LO obstacles were present.
- All three merges were accepted: `1+1=2`, `2+1=3`, and `4+1=5`.
- Results were accepted into the matching slots: `2` to the middle `2`, `3` to the bottom `3`, and `5` to the top `5`.
- Completion feedback appeared and, after settling, the game advanced to a new board. Board 1 completion is verified; Board 2 was not tested per scope.
