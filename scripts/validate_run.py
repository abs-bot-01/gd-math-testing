#!/usr/bin/env python3
"""Validate a GD Math run's JSONL, report links, evidence, and scope."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} is not a JSON object")
        records.append(value)
    return records


def cited_images(report: str) -> list[str]:
    values: list[str] = []
    values.extend(re.findall(r"\]\(([^)]+\.png)\)", report, flags=re.IGNORECASE))
    values.extend(re.findall(r"`([^`]+\.png)`", report, flags=re.IGNORECASE))
    return list(dict.fromkeys(values))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    run_dir = args.run_dir.expanduser().resolve()
    report = args.report.expanduser().resolve()
    checks: dict[str, Any] = {}
    errors: list[str] = []
    warnings: list[str] = []

    plan_path = run_dir / "plan.json"
    events_path = run_dir / "events.jsonl"
    flow_path = run_dir / "flow.md"
    checks["run_dir_exists"] = run_dir.is_dir()
    checks["plan_exists"] = plan_path.is_file()
    checks["events_exists"] = events_path.is_file()
    checks["flow_exists"] = flow_path.is_file()
    checks["report_exists"] = report.is_file()
    for label, ok in checks.items():
        if not ok:
            errors.append(f"missing {label}")

    plan: dict[str, Any] = {}
    events: list[dict[str, Any]] = []
    report_text = ""
    if plan_path.is_file():
        try:
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
            if not isinstance(plan, dict):
                errors.append("plan root is not an object")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid plan: {exc}")
    if events_path.is_file():
        try:
            events = parse_jsonl(events_path)
            checks["events_jsonl_valid"] = True
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            checks["events_jsonl_valid"] = False
            errors.append(f"invalid events.jsonl: {exc}")
    if report.is_file():
        try:
            report_text = report.read_text(encoding="utf-8")
            checks["report_readable"] = bool(report_text.strip())
            if not report_text.strip():
                errors.append("report is empty")
        except OSError as exc:
            errors.append(f"cannot read report: {exc}")

    action_events = [event for event in events if event.get("event") == "action_performed"]
    finding_events = [event for event in events if event.get("event") == "finding_recorded"]
    cleanup_events = [event for event in events if event.get("event") == "runtime_stopped"]
    checks["action_event_count"] = len(action_events)
    checks["finding_event_count"] = len(finding_events)
    checks["cleanup_verified"] = any(event.get("status") == "verified" for event in cleanup_events)
    if events and not checks["cleanup_verified"]:
        errors.append("cleanup is not verified")

    if plan:
        checks["backend_fields_present"] = all(key in plan for key in ("input_backend", "screenshot_backend", "computer_use_invoked"))
        if not checks["backend_fields_present"]:
            errors.append("plan is missing backend provenance fields")
        if plan.get("computer_use_invoked") is True:
            warnings.append("plan records computer_use_invoked=true; confirm that this was explicitly authorized")
        checks["board_scope_present"] = "board_limit" in plan and "boards" in plan
        if not checks["board_scope_present"]:
            errors.append("plan is missing board scope")

    missing_images: list[str] = []
    for value in cited_images(report_text):
        image = Path(value)
        if not image.is_absolute():
            image = (report.parent / image).resolve()
        if not image.is_file() or image.stat().st_size == 0:
            missing_images.append(str(image))
    checks["cited_images_nonempty"] = not missing_images
    if missing_images:
        errors.extend(f"missing or empty cited image: {path}" for path in missing_images)

    if report_text and not re.search(r"\b(PASS|FAIL|PARTIAL|INCOMPLETE|BLOCKED|NOT TESTED)\b", report_text, re.IGNORECASE):
        warnings.append("report has no explicit result marker")

    result = {
        "run_dir": str(run_dir),
        "report": str(report),
        "checks": checks,
        "missing_images": missing_images,
        "warnings": warnings,
        "errors": errors,
        "ok": not errors,
        "configured_board_count": plan.get("board_limit"),
        "action_event_count": len(action_events),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
