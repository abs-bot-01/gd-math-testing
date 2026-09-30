# Direct Godot Run Evidence

Use this reference when testing a Godot project itself rather than an exported APK.

## Launch pattern

1. Confirm the project path and main scene without modifying project files.
2. Prefer a supported deterministic selector, for example:
   ```bash
   DISPLAY=:99 GDM_LEVEL_ID=<level-id> godot --path <project-path>
   ```
3. For headless Linux, start a user-owned Xvfb display first. Capture the Godot window or root screen with a native screenshot tool and verify the image dimensions and non-zero size.
4. Run one level at a time. Stop the prior process before launching the next level.

## Loader classification

Do not classify a level from a short launch attempt. Allow the loader/configuration initialization window to pass, then capture again. Classify the result as one of:

- **Playable board:** title and expected interactive objects are visibly present.
- **Persistent Loading:** loader remains visible after the wait window; no gameplay claims are allowed.
- **Blank/gray/black surface:** rendering issue until disproven with a fresh screenshot and logs.
- **Crash:** process exits or crash evidence is observed.

## Interaction evidence

For each intended move:

- capture `<levelId>_<nn>_before_move.png`;
- perform exactly one pointer/touch action using coordinates selected from the current screenshot;
- capture `<levelId>_<nn>_after_move.png` immediately;
- compare the two images visually; an unchanged board is not an accepted move;
- record the object, source, destination, reason, and observed feedback.

Do not infer acceptance from a successful pointer command. Verify a changed position, removal, feedback, or completion state. Do not call a level complete after a board merely changes; require the visible success/completion state.

## Scope distinction

A direct Godot run is not Android device testing. Report the execution target explicitly, and do not claim APK installation, device touch behavior, or mobile performance from Xvfb/Godot desktop evidence.
