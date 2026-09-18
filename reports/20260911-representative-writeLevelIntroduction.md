# Representative/Write Level Test Report — `writeLevelIntroduction`

- Run ID: `20260911-representative-writeLevelIntroduction`
- Date: 2026-09-11
- Requested scope: Age 3, write-tagged, `icmV2`, `deviceTested`, first matching level
- Target APK: `/home/abs-bot-01/dev/gd-math-godot/dist/gd-math-android-mobile-x86_64.apk`
- Android target: `Small_Phone_API_30_User`, `emulator-5554`, Android 11 / API 30

## Selection — verified

The first matching level in `levels.yaml` is:

- ID: `writeLevelIntroduction`
- Status: `deviceTested`
- Skill age: 3
- Branch: Geometry
- Sequence: 74
- Tags: `intro|write|master|concept`
- Title: `Introducing Line Tracing`
- Type: `icmV2`
- Variants: `characterTrace` → `numberTile`
- Board count: 1
- Board time: 14 seconds

Important: this level contains the `write` tag but is **not tagged `representative`**. It was selected because the request specified Age 3 + write + icmV2 + deviceTested, not because it passed the Representative tag rule.

## Build and device readiness

- KVM: usable.
- Emulator boot: verified; `sys.boot_completed=1`.
- APK metadata: package `in.abstractit.gd.math.test`, version `v4.4.3`, version code `80`.
- APK installation: **Success**.
- `devTesting` rebuild: blocked after config generation and Godot reimport; the config update's SSH `git pull` failed with `Host key verification failed`.

## Launch and rendering

- Godot activity launch: focused activity verified.
- Initial screenshot: black surface; no usable UI or level board.
- After dismissing Android's full-screen overlay and waiting: screen remained black.
- Logcat reported `QueuePresentKHR failed with error: 5` from Godot Vulkan presentation.

## Result

**BLOCKED — deviceTestFailed**

- Boards tested: 0
- Tiles tested: 0
- Observed board time: Not measured
- Gameplay completion: Not verified
- Trace interaction: Not tested
- Full-level completion: Not tested

This result is a rendering/environment blocker. It does not establish a gameplay defect in `writeLevelIntroduction`.

## Not tested

Trace drawing, tile interaction, invalid interaction, hitbox behavior, visual feedback, animation, TTS/audio, board completion, level completion, timing, and responsiveness were not reachable.

## Evidence

- `/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/representative-writeLevelIntroduction-20260911-launch.png`
- `/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/representative-writeLevelIntroduction-20260911-after-overlay8s.png`
- Journal: `/home/abs-bot-01/Hermes/hermes-tester/tester-data/journals/20260911-representative-writeLevelIntroduction.jsonl`
