# Setup and launch contract

## Runtime target

The target is an external Godot project configured in `config/target.json`. The setup project does not copy or modify that project. The target must expose a deterministic selector:

```text
GDM_LEVEL_ID=<level-id>
```

The source-project launch form is:

```bash
DISPLAY=<display> GDM_LEVEL_ID=<level-id> \
  <godot> --path <project>
```

## Display

Use a fresh user-owned Xvfb display and fixed resolution, normally `1280x720x24`. Validate it with:

```bash
DISPLAY=:1200 xdpyinfo
```

Do not interact until the board is visibly rendered. A running Godot process, focused window, non-empty screenshot, or changed image hash is not enough.

## Required commands

`preflight.py` checks the configured project/config paths and these commands:

- Godot;
- `Xvfb`;
- `xdpyinfo`;
- `xdotool`;
- ImageMagick `import`.

## Screenshot backend

Use the X11 root capture for the validated display:

```bash
DISPLAY=:1200 import -window root tester-data/runs/<run-id>/artifacts/<name>.png
```

Inspect the resulting image before acting. The screenshot backend is not gameplay input.

## Read-only boundary

Do not change application source, scenes, assets, generated configuration, level data, repository state, or system-level skill directories. All durable setup and evidence files remain below `testing-setup/`.
