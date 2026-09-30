#!/usr/bin/env python3
"""Deterministic, plan-driven Godot level runner.

The runner owns the mechanical workflow: preflight, one launch, fixed drag
transactions, bounded basic failure detection, evidence collection, cleanup,
and JSONL event/flow output. A plan supplies live coordinates derived from the
current board; the runner never reuses coordinates across boards. Per-run output
is limited to `events.jsonl`, `flow.md`, and requested evidence artifacts.

The default evidence profile is completion-only: retain the first initial
board and final completion screenshot, without capturing screenshots after
every action. `--retain-action-screenshots` is a legacy opt-in for detailed
reviews. The runner never reports a gameplay PASS from process exit alone.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


class RunnerError(RuntimeError):
    """A bounded, reportable runner failure."""


class DeterministicRunner:
    def __init__(self, plan: dict[str, Any], run_dir: Path, args: argparse.Namespace):
        self.plan = plan
        self.run_dir = run_dir
        self.artifacts = run_dir / "artifacts"
        self.transient = run_dir / "transient"
        self.artifacts.mkdir(parents=True, exist_ok=True)
        self.transient.mkdir(parents=True, exist_ok=True)
        self.args = args
        self.display = args.display or plan.get("display", ":1099")
        self.project = Path(os.path.expanduser(str(args.project or plan.get("project", ""))))
        self.level_id = str(plan["level_id"])
        self.godot = os.path.expanduser(str(args.godot or plan.get("godot", "godot")))
        self.resolution = str(plan.get("resolution", "1280x720x24"))
        self.settle = float(plan.get("settle_seconds", 1.8))
        self.hold = float(plan.get("hold_seconds", 0.25))
        self.step_sleep = float(plan.get("step_sleep_seconds", 0.12))
        self.ready_timeout = float(plan.get("ready_timeout_seconds", 30))
        self.max_retries = min(int(plan.get("max_retries", 1)), 1)
        self.input_backend = str(plan.get("input_backend", "xdotool"))
        self.screenshot_backend = str(plan.get("screenshot_backend", "ImageMagick import"))
        self.visual_review_backend = str(plan.get("visual_review_backend", "Pi-agent vision or explicit human review"))
        self.computer_use_invoked = bool(plan.get("computer_use_invoked", False))
        self.events: list[dict[str, Any]] = []
        self.godot_proc: subprocess.Popen[str] | None = None
        self.xvfb_proc: subprocess.Popen[str] | None = None
        self.events_path = run_dir / "events.jsonl"
        self.previous_hash: str | None = None
        self.last_action_screenshot: Path | None = None
        self.last_action_hash: str | None = None
        self.status = "NOT_STARTED"
        self.failure: str | None = None

    def event(self, event_name: str, **data: Any) -> None:
        record = {
            "event": event_name,
            "observed_at": time.time(),
            "level_id": self.level_id,
            "input_backend": self.input_backend,
            "screenshot_backend": self.screenshot_backend,
            "visual_review_backend": self.visual_review_backend,
            "computer_use_invoked": self.computer_use_invoked,
            **data,
        }
        self.events.append(record)
        # Keep the event stream durable while the run is in progress.  This is
        # the only machine-readable run state written by the runner.
        with self.events_path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")

    def command(self, argv: list[str], *, timeout: float = 10) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["DISPLAY"] = self.display
        return subprocess.run(argv, env=env, text=True, capture_output=True, timeout=timeout, check=False)

    def require_commands(self) -> None:
        required = [self.godot, "Xvfb" if self.args.start_xvfb else "xdpyinfo", "xdpyinfo", "xdotool", "import"]
        missing = [name for name in required if shutil.which(name) is None and not Path(name).is_file()]
        if missing:
            raise RunnerError(f"missing required commands: {', '.join(missing)}")
        if not self.project.is_dir():
            raise RunnerError(f"project directory does not exist: {self.project}")

    def validate_plan(self, *, require_actions: bool = True) -> None:
        if not self.level_id:
            raise RunnerError("plan.level_id is required")
        boards = self.plan.get("boards")
        if not isinstance(boards, list) or not boards:
            raise RunnerError("plan.boards must be a non-empty list")
        board_limit = int(self.plan.get("board_limit", len(boards)))
        if board_limit < 1 or board_limit > len(boards):
            raise RunnerError("board_limit must be between 1 and the number of planned boards")
        seen_boards: set[int] = set()
        for board in boards[:board_limit]:
            if not isinstance(board, dict) or "board_id" not in board:
                raise RunnerError("each board requires board_id and actions")
            board_id = int(board["board_id"])
            if board_id in seen_boards:
                raise RunnerError(f"duplicate board_id: {board_id}")
            seen_boards.add(board_id)
            actions = board.get("actions", [])
            if not isinstance(actions, list) or (require_actions and not actions):
                raise RunnerError(f"board {board_id} has no actions")
            if not actions:
                continue
            for index, action in enumerate(actions, start=1):
                if not isinstance(action, dict):
                    raise RunnerError(f"board {board_id} action {index} is not an object")
                for key in ("source", "target"):
                    point = action.get(key)
                    if not isinstance(point, list) or len(point) != 2 or not all(isinstance(v, (int, float)) for v in point):
                        raise RunnerError(f"board {board_id} action {index} requires numeric {key}=[x,y]")
                waypoints = action.get("waypoints", [])
                if not isinstance(waypoints, list) or any(not isinstance(p, list) or len(p) != 2 for p in waypoints):
                    raise RunnerError(f"board {board_id} action {index} has invalid waypoints")
                retry = action.get("retry")
                if retry is not None and not isinstance(retry, dict):
                    raise RunnerError(f"board {board_id} action {index} retry must be an object")
                if isinstance(retry, dict):
                    retry_source = retry.get("source", action.get("source"))
                    retry_target = retry.get("target", action.get("target"))
                    if not isinstance(retry_source, list) or len(retry_source) != 2 or not isinstance(retry_target, list) or len(retry_target) != 2:
                        raise RunnerError(f"board {board_id} action {index} retry requires source/target coordinates")
        self.event("plan_validated", board_limit=board_limit, planned_boards=len(boards), status="verified")

    def display_ready(self) -> bool:
        result = self.command(["xdpyinfo"], timeout=5)
        return result.returncode == 0

    def start_xvfb(self) -> None:
        if not self.args.start_xvfb:
            if not self.display_ready():
                raise RunnerError(f"display {self.display} is not reachable")
            return
        if self.display_ready():
            raise RunnerError(f"display {self.display} is already in use")
        self.xvfb_proc = subprocess.Popen(
            ["Xvfb", self.display, "-screen", "0", self.resolution, "-ac", "-nolisten", "tcp"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
            text=True,
        )
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if self.xvfb_proc.poll() is not None:
                raise RunnerError("Xvfb exited before the display became ready")
            if self.display_ready():
                self.event("xvfb_started", display=self.display, resolution=self.resolution, status="verified")
                return
            time.sleep(0.25)
        raise RunnerError(f"display {self.display} did not become ready")

    def launch(self) -> None:
        env = os.environ.copy()
        env["DISPLAY"] = self.display
        env["GDM_LEVEL_ID"] = self.level_id
        # Godot output is intentionally not persisted as a per-run log.  Test
        # results must come from events, screenshots, flow.md, and the shared
        # gd-math findings/knowledge records.
        self.godot_proc = subprocess.Popen(
            [self.godot, "--path", str(self.project)],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            text=True,
        )
        deadline = time.monotonic() + self.ready_timeout
        ready_seen = False
        while time.monotonic() < deadline:
            if self.godot_proc.poll() is not None:
                raise RunnerError("Godot exited during readiness")
            if not self.display_ready():
                raise RunnerError(f"display {self.display} became unavailable during readiness")
            # The rendered-board probe below is the authoritative readiness
            # check; the window check only prevents waiting on an unrelated X
            # display.  No Godot log file is needed.
            window = self.command(["xdotool", "search", "--name", "GD math"], timeout=5)
            if window.returncode == 0:
                ready_seen = True
                break
            time.sleep(0.25)
        if not ready_seen:
            raise RunnerError(f"level did not reach rendered readiness within {self.ready_timeout:g}s")
        self.event("level_loaded", selector=f"GDM_LEVEL_ID={self.level_id}", display=self.display, status="verified")
        self.wait_for_rendered_board()

    def capture(self, path: Path) -> str:
        path.parent.mkdir(parents=True, exist_ok=True)
        result = self.command(["import", "-window", "root", str(path)], timeout=15)
        if result.returncode != 0 or not path.is_file() or path.stat().st_size == 0:
            raise RunnerError(f"screenshot capture failed: {path}: {result.stderr.strip()}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        return digest

    @staticmethod
    def likely_rendered(path: Path) -> bool:
        """Reject the project's mostly-black loading screen without requiring CV."""
        try:
            from PIL import Image
        except ImportError:
            return True
        try:
            image = Image.open(path).convert("RGB").resize((64, 36))
            pixels = list(image.getdata())
            luminance = [(0.2126 * r) + (0.7152 * g) + (0.0722 * b) for r, g, b in pixels]
            mean = sum(luminance) / len(luminance)
            dark_fraction = sum(value < 12 for value in luminance) / len(luminance)
            return mean >= 20 and dark_fraction < 0.95
        except Exception:
            return True

    def wait_for_rendered_board(self) -> None:
        initial_wait = float(self.plan.get("initial_settle_seconds", 3.0))
        render_timeout = float(self.plan.get("render_timeout_seconds", 20.0))
        time.sleep(initial_wait)
        deadline = time.monotonic() + render_timeout
        probe = self.transient / "board_ready_probe.png"
        while time.monotonic() < deadline:
            if self.godot_proc is not None and self.godot_proc.poll() is not None:
                raise RunnerError("Godot exited before a rendered board was captured")
            if not self.display_ready():
                raise RunnerError(f"display {self.display} became unavailable before board render")
            self.capture(probe)
            if self.likely_rendered(probe):
                self.event("board_rendered", status="verified", readiness_probe=str(probe))
                return
            time.sleep(0.75)
        raise RunnerError(f"a rendered board was not detected within {render_timeout:g}s; last probe: {probe}")

    def drag(self, action: dict[str, Any]) -> None:
        source = action["source"]
        target = action["target"]
        path = [source, *action.get("waypoints", []), target]
        self.command_checked(["xdotool", "mousemove", "--sync", str(source[0]), str(source[1])], "move to source")
        self.command_checked(["xdotool", "mousedown", "1"], "mousedown")
        time.sleep(float(action.get("hold_seconds", self.hold)))
        for point in path[1:]:
            self.command_checked(["xdotool", "mousemove", "--sync", str(point[0]), str(point[1])], "drag waypoint")
            time.sleep(float(action.get("step_sleep_seconds", self.step_sleep)))
        self.command_checked(["xdotool", "mouseup", "1"], "mouseup")

    def command_checked(self, argv: list[str], label: str) -> None:
        result = self.command(argv, timeout=10)
        if result.returncode != 0:
            raise RunnerError(f"{label} failed: {result.stderr.strip() or result.stdout.strip()}")

    def action_screenshot_path(self, board_id: int, index: int, *, retry: bool = False) -> Path:
        suffix = "_retry" if retry else ""
        name = f"{self.level_id}_board{board_id:02d}_action{index:02d}{suffix}_after.png"
        if self.args.retain_action_screenshots:
            return self.artifacts / name
        return self.transient / name

    def execute_action(self, board_id: int, index: int, action: dict[str, Any], *, force_retry: bool = False) -> bool:
        name = str(action.get("name", f"action_{index}"))
        expected = str(action.get("expected", "visual state change"))
        if force_retry and not action.get("retry"):
            self.event("action_failed", board=board_id, action_index=index, reason="requested retry has no retry plan", status="FAIL")
            return False
        attempts = [1] if force_retry else list(range(self.max_retries + 1))
        for attempt in attempts:
            retrying = force_retry or attempt == 1
            current = dict(action)
            if retrying:
                override = action.get("retry", {})
                if isinstance(override, dict):
                    current.update(override)
            try:
                self.drag(current)
                time.sleep(float(current.get("settle_seconds", self.settle)))
                attempt_number = 2 if force_retry else attempt + 1
                if not self.args.retain_action_screenshots:
                    # Completion-only evidence deliberately does not capture an
                    # image after every action. The initial board and final
                    # completion/transition screenshot are the retained proof.
                    self.event(
                        "action_performed",
                        board=board_id,
                        action_index=index,
                        name=name,
                        attempt=attempt_number,
                        kind=action.get("kind", "drag"),
                        source=current["source"],
                        target=current["target"],
                        expected=expected,
                        screenshot=None,
                        screenshot_retained=False,
                        status="executed_without_action_evidence",
                    )
                    return True

                shot = self.action_screenshot_path(board_id, index, retry=retrying)
                digest = self.capture(shot)
                unchanged = self.previous_hash is not None and digest == self.previous_hash
                record = {
                    "board": board_id,
                    "action_index": index,
                    "name": name,
                    "attempt": attempt_number,
                    "kind": action.get("kind", "drag"),
                    "source": current["source"],
                    "target": current["target"],
                    "expected": expected,
                    "screenshot": str(shot),
                    "screenshot_sha256": digest,
                    "screenshot_retained": True,
                    "visual_unchanged_from_previous": unchanged,
                    "status": "possible_rejection" if unchanged else "needs_visual_review",
                }
                self.event("action_performed", **record)
                self.previous_hash = digest
                self.last_action_screenshot = shot
                self.last_action_hash = digest
                if unchanged and not force_retry and attempt < self.max_retries and action.get("retry"):
                    self.event("bounded_retry_started", board=board_id, action_index=index, reason="post-action image unchanged")
                    continue
                if unchanged:
                    self.event("action_failed", board=board_id, action_index=index, reason="post-action image unchanged after bounded retry", screenshot=str(shot), status="FAIL")
                    return False
                return True
            except (RunnerError, subprocess.TimeoutExpired) as exc:
                self.event("action_failed", board=board_id, action_index=index, attempt=(2 if force_retry else attempt + 1), reason=str(exc), status="BLOCKED")
                if force_retry or attempt >= self.max_retries:
                    return False
        return False

    def run(self) -> int:
        self.status = "RUNNING"
        self.event("run_started", run_id=str(self.run_dir), board_limit=int(self.plan.get("board_limit", len(self.plan["boards"]))), evidence_profile="per_action" if self.args.retain_action_screenshots else "completion_only")
        try:
            self.require_commands()
            self.validate_plan()
            self.start_xvfb()
            self.launch()
            board_limit = int(self.plan.get("board_limit", len(self.plan["boards"])))
            for board_index, board in enumerate(self.plan["boards"][:board_limit]):
                board_id = int(board["board_id"])
                self.previous_hash = None
                self.last_action_screenshot = None
                self.last_action_hash = None
                if self.args.retain_action_screenshots:
                    initial = self.artifacts / f"{self.level_id}_board{board_id:02d}_initial.png"
                elif board_index == 0:
                    initial = self.artifacts / f"{self.level_id}_initial.png"
                else:
                    initial = self.transient / f"{self.level_id}_board{board_id:02d}_initial.png"
                digest = self.capture(initial)
                self.previous_hash = digest
                self.event("board_initial_captured", board=board_id, screenshot=str(initial), screenshot_sha256=digest, retained=initial.parent == self.artifacts, status="needs_visual_review")
                actions = board["actions"]
                for index, action in enumerate(actions, start=1):
                    action_to_run = dict(action)
                    if index == len(actions) and board.get("terminal_settle_seconds") is not None:
                        action_to_run["settle_seconds"] = float(board["terminal_settle_seconds"])
                    if not self.execute_action(board_id, index, action_to_run):
                        self.status = "FAIL_OR_BLOCKED"
                        self.failure = f"board {board_id} action {index} failed"
                        return self.finish()
                if self.args.retain_action_screenshots:
                    if self.last_action_screenshot is None or self.last_action_hash is None:
                        raise RunnerError(f"board {board_id} has no terminal action screenshot")
                    terminal = self.last_action_screenshot
                    digest = self.last_action_hash
                    reused = True
                else:
                    is_final_board = board_index == board_limit - 1
                    terminal = (self.artifacts / f"{self.level_id}_completed.png" if is_final_board else self.transient / f"{self.level_id}_board{board_id:02d}_transition.png")
                    digest = self.capture(terminal)
                    reused = False
                self.event("board_terminal_captured", board=board_id, screenshot=str(terminal), screenshot_sha256=digest, retained=terminal.parent == self.artifacts, reused_action_screenshot=reused, status="needs_visual_review")
            self.status = "AUTOMATION_COMPLETE_REVIEW_REQUIRED"
            return self.finish()
        except Exception as exc:
            self.status = "BLOCKED"
            self.failure = str(exc)
            self.event("run_failed", reason=str(exc), exception_type=type(exc).__name__, status="BLOCKED")
            return self.finish()

    def finish(self) -> int:
        self.event("runtime_stopping", status="requested")
        self.stop_process(self.godot_proc)
        self.stop_process(self.xvfb_proc)
        display_alive = self.display_ready()
        godot_stopped = self.godot_proc is None or self.godot_proc.poll() is not None
        xvfb_stopped = self.xvfb_proc is None or self.xvfb_proc.poll() is not None
        display_ok = (not self.args.start_xvfb) or not display_alive
        stop_ok = godot_stopped and xvfb_stopped and display_ok
        self.event("runtime_stopped", godot_stopped=godot_stopped, xvfb_stopped=xvfb_stopped, display_reachable=display_alive, status="verified" if stop_ok else "BLOCKED")
        if self.failure:
            self.event("run_result", status=self.status, failure=self.failure)
        else:
            self.event("run_result", status=self.status, failure=None)
        self.write_events()
        flow = self.flow_text()
        (self.run_dir / "flow.md").write_text(flow)
        if not self.args.retain_action_screenshots:
            for path in self.transient.glob("*.png"):
                path.unlink(missing_ok=True)
        return 0 if self.status == "AUTOMATION_COMPLETE_REVIEW_REQUIRED" else 2

    def write_events(self) -> None:
        self.events_path.write_text(
            "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in self.events),
            encoding="utf-8",
        )

    def stop_process(self, proc: subprocess.Popen[str] | None) -> None:
        if proc is None or proc.poll() is not None:
            return
        try:
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait(timeout=5)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait(timeout=3)
            except (ProcessLookupError, subprocess.TimeoutExpired):
                pass

    def flow_text(self) -> str:
        return "\n".join([
            f"# Deterministic Runner Flow — {self.level_id}",
            "",
            f"- **Status:** {self.status}",
            f"- **Display:** `{self.display}`",
            f"- **Scope:** {self.plan.get('board_limit', len(self.plan.get('boards', [])))} planned board(s)",
            f"- **Evidence profile:** {'per-action' if self.args.retain_action_screenshots else 'completion-only'}",
            f"- **Failure:** {self.failure or 'None at mechanical runner level'}",
            "- Outputs: `events.jsonl`, `flow.md`, and requested evidence artifacts; no per-run session or Godot log files are created.",
            "- Completion-only evidence retains only the first initial-board screenshot and final completion screenshot; intermediate transition probes and action screenshots are not retained.",
            "- Semantic gameplay PASS is not inferred from process exit or process completion; review the retained initial and final states before reporting PASS.",
            "",
        ])


def terminal_snapshot(runner: DeterministicRunner, board_id: int, *, final: bool = True) -> tuple[Path, str]:
    if runner.args.retain_action_screenshots:
        if runner.last_action_screenshot is None or runner.last_action_hash is None:
            raise RunnerError(f"board {board_id} has no terminal action screenshot")
        return runner.last_action_screenshot, runner.last_action_hash
    filename = f"{runner.level_id}_completed.png" if final else f"{runner.level_id}_board{board_id:02d}_transition.png"
    terminal = (runner.artifacts / filename) if final else (runner.transient / filename)
    digest = runner.capture(terminal)
    return terminal, digest


def write_runner_files(runner: DeterministicRunner) -> None:
    runner.write_events()
    (runner.run_dir / "flow.md").write_text(runner.flow_text(), encoding="utf-8")


def read_event_stream(run_dir: Path) -> list[dict[str, Any]]:
    path = run_dir / "events.jsonl"
    if not path.is_file():
        return []
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RunnerError(f"invalid event JSON at {path}:{line_number}: {exc}") from exc
        if not isinstance(record, dict):
            raise RunnerError(f"event at {path}:{line_number} is not an object")
        records.append(record)
    return records


def attached_session_from_events(run_dir: Path) -> dict[str, Any]:
    events = read_event_stream(run_dir)
    anchors = [event for event in events if event.get("event") in {"session_ready", "next_board_ready"}]
    if not anchors:
        raise RunnerError(f"missing session_ready event: {run_dir / 'events.jsonl'}")
    anchor = anchors[-1]
    session: dict[str, Any] = {
        "run_dir": str(run_dir),
        "level_id": anchor.get("level_id"),
        "display": anchor.get("display"),
        "current_board_index": int(anchor.get("current_board_index", anchor.get("board_index", 0))),
        "current_board_id": int(anchor.get("current_board", anchor.get("board"))),
        "initial_screenshot": anchor.get("initial_screenshot"),
        "initial_screenshot_sha256": anchor.get("initial_screenshot_sha256"),
        "godot_pid": anchor.get("godot_pid"),
        "xvfb_pid": anchor.get("xvfb_pid"),
        "status": anchor.get("status"),
        "next_action_index": 1,
    }
    anchor_index = events.index(anchor)
    later = events[anchor_index + 1:]
    for event in later:
        name = event.get("event")
        if name == "action_review_pending":
            session.update({
                "pending_action_index": int(event["action_index"]),
                "pending_screenshot": event.get("screenshot"),
                "pending_screenshot_sha256": event.get("screenshot_sha256"),
                "next_action_index": int(event["action_index"]),
                "status": "AWAITING_VISUAL_REVIEW",
            })
        elif name == "action_review_approved":
            session.pop("pending_action_index", None)
            session.pop("pending_screenshot", None)
            session.pop("pending_screenshot_sha256", None)
            session["next_action_index"] = int(event["action_index"]) + 1
        elif name == "action_retry_requested":
            session["retry_used_for_action"] = int(event["action_index"])
    return session


def process_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def terminate_group(pid: int | None) -> None:
    if not pid or not process_alive(pid):
        return
    try:
        os.killpg(pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline and process_alive(pid):
        time.sleep(0.1)
    if process_alive(pid):
        try:
            os.killpg(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


def finish_attached(runner: DeterministicRunner, session: dict[str, Any]) -> int:
    runner.event("runtime_stopping", status="requested")
    terminate_group(int(session.get("godot_pgid", session.get("godot_pid", 0))))
    terminate_group(int(session.get("xvfb_pgid", session.get("xvfb_pid", 0))))
    display_alive = runner.display_ready()
    godot_stopped = not process_alive(int(session.get("godot_pid", 0)))
    xvfb_stopped = not process_alive(int(session.get("xvfb_pid", 0)))
    stop_ok = godot_stopped and xvfb_stopped and not display_alive
    runner.event("runtime_stopped", godot_stopped=godot_stopped, xvfb_stopped=xvfb_stopped, display_reachable=display_alive, status="verified" if stop_ok else "BLOCKED")
    runner.event("run_result", status=runner.status, failure=runner.failure)
    write_runner_files(runner)
    return 0 if runner.status == "AUTOMATION_COMPLETE_REVIEW_REQUIRED" and stop_ok else 2


def complete_attached_board(runner: DeterministicRunner, session: dict[str, Any], plan: dict[str, Any], board_index: int, board_id: int, terminal: Path, digest: str) -> int:
    runner.event("board_terminal_captured", board=board_id, screenshot=str(terminal), screenshot_sha256=digest, reused_action_screenshot=runner.args.retain_action_screenshots, status="needs_visual_review")
    next_index = board_index + 1
    board_limit = int(plan.get("board_limit", len(plan["boards"])))
    if next_index < board_limit:
        next_board_id = int(plan["boards"][next_index]["board_id"])
        next_session = dict(session)
        next_session.update({"current_board_index": next_index, "current_board_id": next_board_id, "initial_screenshot": str(terminal), "initial_screenshot_sha256": digest, "status": "AWAITING_LIVE_MAPPING", "next_action_index": 1})
        for key in ("pending_action_index", "pending_screenshot", "pending_screenshot_sha256", "retry_used_for_action"):
            next_session.pop(key, None)
        runner.status = "AWAITING_LIVE_MAPPING"
        runner.event(
            "next_board_ready",
            board=next_board_id,
            board_index=next_index,
            initial_screenshot=str(terminal),
            initial_screenshot_sha256=digest,
            godot_pid=session.get("godot_pid"),
            xvfb_pid=session.get("xvfb_pid"),
            display=session.get("display"),
            status="needs_live_mapping",
        )
        write_runner_files(runner)
        print(json.dumps(next_session, indent=2))
        return 3
    runner.status = "AUTOMATION_COMPLETE_REVIEW_REQUIRED"
    session["status"] = runner.status
    return finish_attached(runner, session)


def prepare_session(plan: dict[str, Any], args: argparse.Namespace, run_dir: Path) -> int:
    runner = DeterministicRunner(plan, run_dir, args)
    try:
        runner.status = "AWAITING_LIVE_MAPPING"
        runner.event("run_started", run_id=str(run_dir), mode="prepare", board_limit=int(plan.get("board_limit", len(plan["boards"]))), evidence_profile="per_action" if args.retain_action_screenshots else "completion_only")
        runner.require_commands()
        runner.validate_plan(require_actions=False)
        runner.start_xvfb()
        runner.launch()
        board = plan["boards"][0]
        board_id = int(board["board_id"])
        initial = (runner.artifacts / f"{runner.level_id}_board{board_id:02d}_initial.png" if args.retain_action_screenshots else runner.artifacts / f"{runner.level_id}_initial.png")
        digest = runner.capture(initial)
        runner.event("board_initial_captured", board=board_id, screenshot=str(initial), screenshot_sha256=digest, status="needs_live_mapping")
        session = {
            "run_dir": str(run_dir),
            "level_id": runner.level_id,
            "project": str(runner.project),
            "display": runner.display,
            "current_board_index": 0,
            "current_board_id": board_id,
            "initial_screenshot": str(initial),
            "initial_screenshot_sha256": digest,
            "godot_pid": runner.godot_proc.pid if runner.godot_proc else None,
            "godot_pgid": runner.godot_proc.pid if runner.godot_proc else None,
            "xvfb_pid": runner.xvfb_proc.pid if runner.xvfb_proc else None,
            "xvfb_pgid": runner.xvfb_proc.pid if runner.xvfb_proc else None,
            "status": "AWAITING_LIVE_MAPPING",
        }
        runner.event(
            "session_ready",
            current_board=board_id,
            current_board_index=0,
            initial_screenshot=str(initial),
            initial_screenshot_sha256=digest,
            godot_pid=session["godot_pid"],
            xvfb_pid=session["xvfb_pid"],
            display=runner.display,
            status="needs_live_mapping",
        )
        write_runner_files(runner)
        print(json.dumps(session, indent=2))
        return 0
    except Exception as exc:
        runner.status = "BLOCKED"
        runner.failure = str(exc)
        runner.event("run_failed", reason=str(exc), exception_type=type(exc).__name__, status="BLOCKED")
        return runner.finish()


def execute_session(plan: dict[str, Any], args: argparse.Namespace, run_dir: Path) -> int:
    try:
        session = attached_session_from_events(run_dir)
        runner = DeterministicRunner(plan, run_dir, args)
        runner.events = read_event_stream(run_dir)
        runner.validate_plan(require_actions=True)
        if plan["level_id"] != session["level_id"]:
            raise RunnerError("plan level_id does not match prepared session")
        if not process_alive(int(session["godot_pid"])) or not process_alive(int(session["xvfb_pid"])):
            raise RunnerError("prepared Godot/Xvfb process is no longer alive")
        if not runner.display_ready():
            raise RunnerError(f"prepared display {runner.display} is not reachable")
        board_index = int(session["current_board_index"])
        board = plan["boards"][board_index]
        board_id = int(board["board_id"])
        if board_id != int(session["current_board_id"]):
            raise RunnerError("plan board does not match the prepared current board")
        if board.get("live_mapping_verified") is not True:
            raise RunnerError("refusing to execute without live_mapping_verified=true for the current screenshot")
        if board.get("initial_screenshot_sha256") != session.get("initial_screenshot_sha256"):
            raise RunnerError("plan was not derived from the current prepared initial screenshot")
        runner.event("live_mapping_accepted", board=board_id, initial_screenshot_sha256=session["initial_screenshot_sha256"], status="verified")
        runner.previous_hash = session["initial_screenshot_sha256"]
        runner.status = "RUNNING"
        actions = board["actions"]
        for index, action in enumerate(actions, start=1):
            action_to_run = dict(action)
            if index == len(actions) and board.get("terminal_settle_seconds") is not None:
                action_to_run["settle_seconds"] = float(board["terminal_settle_seconds"])
            if not runner.execute_action(board_id, index, action_to_run):
                runner.status = "FAIL_OR_BLOCKED"
                runner.failure = f"board {board_id} action {index} failed"
                return finish_attached(runner, session)
        next_index = board_index + 1
        board_limit = int(plan.get("board_limit", len(plan["boards"])))
        terminal, digest = terminal_snapshot(runner, board_id, final=next_index >= board_limit)
        runner.event("board_terminal_captured", board=board_id, screenshot=str(terminal), screenshot_sha256=digest, retained=terminal.parent == runner.artifacts, reused_action_screenshot=runner.args.retain_action_screenshots, status="needs_visual_review")
        if next_index < board_limit:
            next_board_id = int(plan["boards"][next_index]["board_id"])
            next_session = dict(session)
            next_session.update({"current_board_index": next_index, "current_board_id": next_board_id, "initial_screenshot": str(terminal), "initial_screenshot_sha256": digest, "status": "AWAITING_LIVE_MAPPING"})
            runner.status = "AWAITING_LIVE_MAPPING"
            runner.event(
                "next_board_ready",
                board=next_board_id,
                board_index=next_index,
                initial_screenshot=str(terminal),
                initial_screenshot_sha256=digest,
                godot_pid=session.get("godot_pid"),
                xvfb_pid=session.get("xvfb_pid"),
                display=session.get("display"),
                status="needs_live_mapping",
            )
            write_runner_files(runner)
            print(json.dumps(next_session, indent=2))
            return 3
        runner.status = "AUTOMATION_COMPLETE_REVIEW_REQUIRED"
        session["status"] = runner.status
        return finish_attached(runner, session)
    except Exception as exc:
        runner = locals().get("runner")
        if runner is None:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        runner.status = "BLOCKED"
        runner.failure = str(exc)
        runner.event("run_failed", reason=str(exc), exception_type=type(exc).__name__, status="BLOCKED")
        return finish_attached(runner, session)


def execute_session_one_action(plan: dict[str, Any], args: argparse.Namespace, run_dir: Path) -> int:
    runner: DeterministicRunner | None = None
    try:
        session = attached_session_from_events(run_dir)
        runner = DeterministicRunner(plan, run_dir, args)
        runner.events = read_event_stream(run_dir)
        runner.validate_plan(require_actions=True)
        if plan["level_id"] != session["level_id"]:
            raise RunnerError("plan level_id does not match prepared session")
        if not process_alive(int(session["godot_pid"])) or not process_alive(int(session["xvfb_pid"])):
            raise RunnerError("prepared Godot/Xvfb process is no longer alive")
        if not runner.display_ready():
            raise RunnerError(f"prepared display {runner.display} is not reachable")
        board_index = int(session["current_board_index"])
        board = plan["boards"][board_index]
        board_id = int(board["board_id"])
        if board_id != int(session["current_board_id"]):
            raise RunnerError("plan board does not match the prepared current board")
        if board.get("live_mapping_verified") is not True:
            raise RunnerError("refusing to execute without live_mapping_verified=true for the current screenshot")
        if board.get("initial_screenshot_sha256") != session.get("initial_screenshot_sha256"):
            raise RunnerError("plan was not derived from the current prepared initial screenshot")
        actions = board["actions"]
        pending = session.get("pending_action_index")
        approve = args.approve_action
        retry = args.retry_action
        if approve is not None and retry is not None:
            raise RunnerError("choose either --approve-action or --retry-action")
        force_retry = False
        pending_screenshot_path: str | None = None
        pending_screenshot_hash: str | None = None
        if pending is not None:
            pending = int(pending)
            pending_screenshot_path = session.get("pending_screenshot")
            pending_screenshot_hash = session.get("pending_screenshot_sha256")
            if approve != pending and retry != pending:
                raise RunnerError(f"action {pending} is awaiting visual review; pass --approve-action {pending} or --retry-action {pending}")
            if retry == pending:
                if session.get("retry_used_for_action") == pending:
                    raise RunnerError(f"bounded retry already used for action {pending}")
                force_retry = True
                action_index = pending
                session["retry_used_for_action"] = pending
                runner.event("action_retry_requested", board=board_id, action_index=pending, status="requested")
            else:
                action_index = pending + 1
                runner.event("action_review_approved", board=board_id, action_index=pending, status="verified")
                session.pop("pending_action_index", None)
                if action_index <= len(actions):
                    session.pop("pending_screenshot", None)
                    session.pop("pending_screenshot_sha256", None)
                session.pop("retry_used_for_action", None)
        else:
            if approve is not None or retry is not None:
                raise RunnerError("no action is awaiting review")
            action_index = int(session.get("next_action_index", 1))
        if action_index > len(actions):
            if not pending_screenshot_path or not pending_screenshot_hash:
                raise RunnerError("pending terminal screenshot is unavailable")
            pending_path = Path(str(pending_screenshot_path))
            pending_hash = str(pending_screenshot_hash)
            if not pending_path.is_file():
                raise RunnerError("pending terminal screenshot is unavailable")
            runner.last_action_screenshot = pending_path
            runner.last_action_hash = pending_hash
            terminal, digest = terminal_snapshot(runner, board_id)
            return complete_attached_board(runner, session, plan, board_index, board_id, terminal, digest)
        if action_index < 1 or action_index > len(actions):
            raise RunnerError(f"action index out of range: {action_index}")
        if pending is not None and retry != pending:
            previous_hash = str(session.get("pending_screenshot_sha256", session["initial_screenshot_sha256"]))
        elif pending is not None:
            previous_hash = str(session.get("pending_screenshot_sha256", session["initial_screenshot_sha256"]))
        else:
            previous_hash = str(session.get("initial_screenshot_sha256"))
        runner.previous_hash = previous_hash
        runner.status = "RUNNING"
        action = dict(actions[action_index - 1])
        if action_index == len(actions) and board.get("terminal_settle_seconds") is not None:
            action["settle_seconds"] = float(board["terminal_settle_seconds"])
        if not runner.execute_action(board_id, action_index, action, force_retry=force_retry):
            runner.status = "FAIL_OR_BLOCKED"
            runner.failure = f"board {board_id} action {action_index} failed"
            return finish_attached(runner, session)
        session.update({"next_action_index": action_index, "pending_action_index": action_index, "pending_screenshot": str(runner.last_action_screenshot), "pending_screenshot_sha256": runner.last_action_hash, "status": "AWAITING_VISUAL_REVIEW"})
        runner.status = "AWAITING_VISUAL_REVIEW"
        runner.event("action_review_pending", board=board_id, action_index=action_index, screenshot=str(runner.last_action_screenshot), screenshot_sha256=runner.last_action_hash, status="needs_visual_review")
        write_runner_files(runner)
        print(json.dumps(session, indent=2))
        return 3
    except Exception as exc:
        if runner is None:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        runner.status = "BLOCKED"
        runner.failure = str(exc)
        runner.event("run_failed", reason=str(exc), exception_type=type(exc).__name__, status="BLOCKED")
        return finish_attached(runner, session)


def load_plan(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise RunnerError(f"cannot read plan {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RunnerError("plan root must be a JSON object")
    return value


def dry_run(plan: dict[str, Any]) -> int:
    fake_args = argparse.Namespace(
        display=plan.get("display", ":dry-run"),
        project=plan.get("project", "/dry-run"),
        godot=plan.get("godot", "godot"),
        start_xvfb=False,
        retain_action_screenshots=False,
    )
    dry_run_dir = Path(__file__).resolve().parents[1] / ".runtime" / "dry-run"
    runner = DeterministicRunner(plan, dry_run_dir, fake_args)
    runner.validate_plan()
    print(json.dumps({
        "valid": True,
        "level_id": plan["level_id"],
        "board_limit": int(plan.get("board_limit", len(plan["boards"]))),
        "actions": sum(len(board["actions"]) for board in plan["boards"][:int(plan.get("board_limit", len(plan["boards"])))]),
        "state_machine": "preflight -> launch -> board_ready -> live_mapping -> action_transaction -> board_terminal -> final_visual_review -> cleanup -> artifact_validation",
        "evidence_profile": "completion_only",
        "semantic_pass_requires_final_completion_review": True,
    }, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True, help="JSON plan containing live per-board actions")
    parser.add_argument("--run-dir", type=Path, help="output run directory; default is a timestamped directory beside the plan")
    parser.add_argument("--display", help="X display, overriding the plan")
    parser.add_argument("--project", help="Godot project path, overriding the plan")
    parser.add_argument("--godot", help="Godot executable, overriding the plan")
    parser.add_argument("--start-xvfb", action="store_true", help="start and stop Xvfb on the requested display")
    parser.add_argument("--retain-action-screenshots", action="store_true", help="legacy opt-in: capture and retain one post-action screenshot per action")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="validate the plan without launching or sending input")
    mode.add_argument("--prepare", action="store_true", help="launch once, capture a live initial board, and leave the session awaiting a mapped plan")
    mode.add_argument("--execute", action="store_true", help="execute the mapped plan against a prepared live session")
    parser.add_argument("--one-action", action="store_true", help="execute one action, then pause for visual review before the next action")
    review = parser.add_mutually_exclusive_group()
    review.add_argument("--approve-action", type=int, help="approve the pending action and advance to the next one")
    review.add_argument("--retry-action", type=int, help="retry the pending action using its single bounded retry plan")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        plan = load_plan(args.plan)
        if args.dry_run:
            return dry_run(plan)
        run_dir = args.run_dir or args.plan.parent / f"run-{time.strftime('%Y%m%d-%H%M%S')}-{plan['level_id']}"
        if args.prepare:
            return prepare_session(plan, args, run_dir)
        if args.execute:
            if args.start_xvfb:
                raise RunnerError("--execute attaches to the prepared display; do not pass --start-xvfb")
            if (args.approve_action is not None or args.retry_action is not None) and not args.one_action:
                raise RunnerError("--approve-action/--retry-action require --one-action")
            if args.one_action and not args.retain_action_screenshots:
                raise RunnerError("--one-action requires --retain-action-screenshots; completion-only runs execute without action screenshots")
            if args.one_action:
                return execute_session_one_action(plan, args, run_dir)
            return execute_session(plan, args, run_dir)
        runner = DeterministicRunner(plan, run_dir, args)
        return runner.run()
    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
