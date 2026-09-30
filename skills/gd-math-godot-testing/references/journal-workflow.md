# Journal workflow for native-app exploration

Use this reference when the user requests a screenshot journal in addition to findings.

1. Create a clean, dedicated evidence directory before launching.
2. Use strictly monotonic, zero-padded filenames: `01-dashboard.png`, `02-level-1.png`, `03-left-selected.png`.
3. Capture every meaningful state boundary and each game input, not merely the beginning and end.
4. Never reuse sequence numbers or leave ambiguous duplicate names. Rename or remove accidental captures immediately.
5. Keep a Markdown report in the same directory with an explicit screenshot index mapping each image to the action and observed state.
6. Before reporting completion, verify every referenced screenshot exists and has nonzero size; verify the report itself exists.
7. Clearly separate `verified`, `observed but not completed`, and `not tested`. If a level does not advance, record the exact inputs, waits, and unchanged state; do not infer that it is broken.
