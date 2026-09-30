#!/usr/bin/env python3
"""Check a GD Math target without launching or modifying it."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TOOLS = ("Xvfb", "xdpyinfo", "xdotool", "import")


def expand_path(value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(os.path.expanduser(value))
    return path if path.is_absolute() else (ROOT / path).resolve()


def command_path(command: str) -> str | None:
    candidate = Path(os.path.expanduser(command))
    if candidate.is_file() and os.access(candidate, os.X_OK):
        return str(candidate)
    return shutil.which(command)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def runtime_level(runtime: Any, level_id: str) -> dict[str, Any] | None:
    if not isinstance(runtime, dict):
        return None
    levels = runtime.get("levels")
    if isinstance(levels, dict):
        value = levels.get(level_id)
        return value if isinstance(value, dict) else None
    if isinstance(levels, list):
        for value in levels:
            if isinstance(value, dict) and value.get("id") == level_id:
                return value
    return None


def yaml_scalar(block: str, key: str) -> Any:
    match = re.search(rf"(?m)^\s*(?:-\s+)?{re.escape(key)}:\s*(.*?)\s*$", block)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith(("'", '"')) and value.endswith(value[0]):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def source_level(path: Path, level_id: str) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    match = re.search(rf"(?m)^-\s+id:\s*{re.escape(level_id)}\s*$", text)
    if not match:
        return None
    next_item = re.search(r"(?m)^-\s+id:\s*", text[match.end() :])
    end = match.end() + next_item.start() if next_item else len(text)
    block = text[match.start() : end]
    keys = ("id", "title", "skillAge", "branch", "type", "leftVariant", "rightVariant", "boardCount", "boardTime", "tags")
    return {key: yaml_scalar(block, key) for key in keys}


def display_state(display: str) -> dict[str, Any]:
    tool = shutil.which("xdpyinfo")
    if not tool:
        return {"reachable": None, "status": "xdpyinfo-missing"}
    result = subprocess.run(
        [tool, "-display", display],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
        timeout=5,
    )
    return {"reachable": result.returncode == 0, "status": "in-use" if result.returncode == 0 else "free-or-unavailable"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--level-id", required=True)
    parser.add_argument("--display")
    parser.add_argument("--require-display", action="store_true")
    args = parser.parse_args()

    config_path = args.config.expanduser().resolve()
    result: dict[str, Any] = {
        "setup_root": str(ROOT),
        "config": str(config_path),
        "level_id": args.level_id,
        "errors": [],
        "warnings": [],
    }
    if not config_path.is_file():
        result["errors"].append(f"config not found: {config_path}")
        print(json.dumps(result, indent=2))
        return 2

    try:
        config = read_json(config_path)
    except (OSError, json.JSONDecodeError) as exc:
        result["errors"].append(f"cannot read config: {exc}")
        print(json.dumps(result, indent=2))
        return 2

    project = expand_path(config.get("project"))
    source_config = expand_path(config.get("source_config"))
    runtime_config = expand_path(config.get("runtime_config"))
    display = args.display or str(config.get("display", ":1200"))
    result["target"] = {
        "project": str(project) if project else None,
        "source_config": str(source_config) if source_config else None,
        "runtime_config": str(runtime_config) if runtime_config else None,
        "godot": config.get("godot", "godot"),
        "display": display,
        "resolution": config.get("resolution", "1280x720x24"),
        "backends": {
            "input": config.get("input_backend", "xdotool"),
            "screenshot": config.get("screenshot_backend", "ImageMagick import"),
            "computer_use_invoked": bool(config.get("computer_use_invoked", False)),
        },
    }

    for label, path in (("project", project), ("source_config", source_config), ("runtime_config", runtime_config)):
        if path is None or not path.exists():
            result["errors"].append(f"{label} does not exist: {path}")
    commands = {name: command_path(name) for name in (str(config.get("godot", "godot")), *REQUIRED_TOOLS)}
    result["commands"] = commands
    for name, path in commands.items():
        if path is None:
            result["errors"].append(f"required command missing: {name}")

    state = display_state(display)
    result["display"] = state
    if args.require_display and not state.get("reachable"):
        result["errors"].append(f"display is not reachable: {display}")
    elif not state.get("reachable"):
        result["warnings"].append(f"display is free or unavailable; --start-xvfb can create it: {display}")

    source = None
    runtime = None
    if source_config and source_config.is_file():
        try:
            source = source_level(source_config, args.level_id)
        except OSError as exc:
            result["errors"].append(f"cannot read source config: {exc}")
    if runtime_config and runtime_config.is_file():
        try:
            runtime = runtime_level(read_json(runtime_config), args.level_id)
        except (OSError, json.JSONDecodeError) as exc:
            result["errors"].append(f"cannot read runtime config: {exc}")

    result["source_record"] = source
    runtime_keys = ("id", "title", "skillAge", "branch", "sequence", "type", "leftVariant", "rightVariant", "boardCount", "boardTime", "tags", "parser")
    result["runtime_record"] = {key: runtime.get(key) for key in runtime_keys} if runtime else None
    if source is None:
        result["errors"].append(f"exact source level ID not found: {args.level_id}")
    if runtime is None:
        result["errors"].append(f"exact runtime level ID not found: {args.level_id}")
    if source and runtime:
        source_count = source.get("boardCount")
        runtime_count = runtime.get("boardCount")
        result["identity_match"] = {
            "source_id": source.get("id"),
            "runtime_id": runtime.get("id", args.level_id),
            "source_board_count": source_count,
            "runtime_board_count": runtime_count,
            "board_count_match": source_count is None or runtime_count is None or source_count == runtime_count,
            "title_match": source.get("title") is None or runtime.get("title") is None or source.get("title") == runtime.get("title"),
        }
        if not result["identity_match"]["board_count_match"]:
            result["errors"].append("source/runtime boardCount mismatch")
        if not result["identity_match"]["title_match"]:
            result["warnings"].append("source/runtime title differs; record the conflict before gameplay")

    result["ok"] = not result["errors"]
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
