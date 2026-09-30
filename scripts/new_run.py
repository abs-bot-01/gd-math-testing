#!/usr/bin/env python3
"""Create an isolated GD Math run directory and starter plan."""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def expand_path(value: str) -> Path:
    path = Path(os.path.expanduser(value))
    return path if path.is_absolute() else (ROOT / path).resolve()


def safe_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return cleaned or "run"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--level-id", required=True)
    parser.add_argument("--board-count", type=int, required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--scope", default="full configured level")
    parser.add_argument("--evidence-profile", choices=("per-action", "completion-only"))
    args = parser.parse_args()

    if args.board_count < 1:
        parser.error("--board-count must be positive")
    config = json.loads(args.config.expanduser().read_text(encoding="utf-8"))
    run_root = expand_path(str(config.get("run_root", "tester-data/runs")))
    run_id = args.run_id or f"{time.strftime('%Y%m%d-%H%M%S')}-{safe_id(args.level_id)}"
    run_id = safe_id(run_id)
    run_dir = run_root / run_id
    if run_dir.exists():
        raise SystemExit(f"run directory already exists: {run_dir}")
    artifacts = run_dir / "artifacts"
    transient = run_dir / "transient"
    artifacts.mkdir(parents=True)
    transient.mkdir()

    plan: dict[str, Any] = {
        "level_id": args.level_id,
        "project": str(expand_path(str(config["project"]))),
        "godot": str(config.get("godot", "godot")),
        "display": str(config.get("display", ":1200")),
        "resolution": str(config.get("resolution", "1280x720x24")),
        "initial_settle_seconds": 4.0,
        "render_timeout_seconds": 20.0,
        "ready_timeout_seconds": 30.0,
        "settle_seconds": 2.0,
        "hold_seconds": 0.25,
        "step_sleep_seconds": 0.15,
        "max_retries": 1,
        "board_limit": args.board_count,
        "requested_scope": args.scope,
        "input_backend": str(config.get("input_backend", "xdotool")),
        "screenshot_backend": str(config.get("screenshot_backend", "ImageMagick import")),
        "visual_review_backend": str(config.get("visual_review_backend", "Pi-agent vision or explicit human review")),
        "computer_use_invoked": bool(config.get("computer_use_invoked", False)),
        "evidence_profile": args.evidence_profile or str(config.get("evidence_profile", "per-action")),
        "boards": [
            {
                "board_id": index,
                "initial_screenshot_sha256": None,
                "live_mapping_verified": False,
                "actions": [],
            }
            for index in range(1, args.board_count + 1)
        ],
    }
    (run_dir / "plan.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    (run_dir / "events.jsonl").write_text("", encoding="utf-8")
    (run_dir / "flow.md").write_text(
        f"# Run Flow — {run_id}\n\n- Exact level ID: `{args.level_id}`\n- Requested scope: {args.scope}\n- Configured/requested board count: {args.board_count}\n- Status: NOT STARTED\n",
        encoding="utf-8",
    )
    (run_dir / "context-packet.md").write_text(
        "# Context Packet\n\nUse `docs/context-packet-template.md` and complete it before gameplay.\n",
        encoding="utf-8",
    )
    print(json.dumps({"run_id": run_id, "run_dir": str(run_dir), "plan": str(run_dir / "plan.json")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
