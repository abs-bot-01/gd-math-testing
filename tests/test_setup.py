from __future__ import annotations

import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RUNTIME = ROOT / ".runtime" / "tests"


class SetupSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        RUNTIME.mkdir(parents=True, exist_ok=True)

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(RUNTIME, ignore_errors=True)

    def test_scripts_compile(self) -> None:
        for path in SCRIPTS.glob("*.py"):
            result = subprocess.run(
                [sys.executable, "-m", "py_compile", str(path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_runner_dry_run(self) -> None:
        plan = {
            "level_id": "smoke",
            "project": str(ROOT),
            "board_limit": 1,
            "input_backend": "xdotool",
            "screenshot_backend": "ImageMagick import",
            "computer_use_invoked": False,
            "boards": [
                {
                    "board_id": 1,
                    "actions": [
                        {"source": [10, 10], "target": [20, 20], "waypoints": [[12, 12], [16, 16]]}
                    ],
                }
            ],
        }
        plan_path = RUNTIME / "dry-plan.json"
        plan_path.write_text(json.dumps(plan), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "deterministic_level_runner.py"), "--plan", str(plan_path), "--dry-run"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertTrue(output["valid"])
        self.assertEqual(output["actions"], 1)

    def test_new_run_stays_under_configured_root(self) -> None:
        config = {
            "project": str(ROOT),
            "run_root": ".runtime/tests/runs",
            "display": ":1200",
            "evidence_profile": "per-action",
            "input_backend": "xdotool",
            "screenshot_backend": "ImageMagick import",
            "computer_use_invoked": False,
        }
        config_path = RUNTIME / "config.json"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "new_run.py"),
                "--config",
                str(config_path),
                "--level-id",
                "smoke",
                "--board-count",
                "1",
                "--run-id",
                "smoke-run",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        run_dir = ROOT / ".runtime/tests/runs/smoke-run"
        self.assertTrue((run_dir / "plan.json").is_file())
        plan = json.loads((run_dir / "plan.json").read_text(encoding="utf-8"))
        self.assertEqual(plan["input_backend"], "xdotool")
        self.assertFalse(plan["computer_use_invoked"])

    def test_validate_run_accepts_valid_local_artifacts(self) -> None:
        run_dir = RUNTIME / "valid-run"
        artifacts = run_dir / "artifacts"
        artifacts.mkdir(parents=True, exist_ok=True)
        (run_dir / "plan.json").write_text(
            json.dumps(
                {
                    "level_id": "smoke",
                    "board_limit": 1,
                    "boards": [{"board_id": 1, "actions": []}],
                    "input_backend": "xdotool",
                    "screenshot_backend": "ImageMagick import",
                    "computer_use_invoked": False,
                }
            ),
            encoding="utf-8",
        )
        (run_dir / "events.jsonl").write_text(
            json.dumps({"event": "runtime_stopped", "status": "verified"}) + "\n",
            encoding="utf-8",
        )
        (run_dir / "flow.md").write_text("# flow\n", encoding="utf-8")
        image = artifacts / "final.png"
        image.write_bytes(b"not-a-real-png-but-nonempty-for-contract-smoke")
        report = RUNTIME / "valid-report.md"
        report.write_text("# QA Test Report\n\nResult: PASS\n\n![final](valid-run/artifacts/final.png)\n", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_run.py"), "--run-dir", str(run_dir), "--report", str(report)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
