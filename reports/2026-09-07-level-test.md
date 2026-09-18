# Android Level Device Test Report

- Run ID: `2026-09-07-level-test`
- Target APK: `/home/abs-bot-01/Downloads/gd-math-android-emulator-x86_64.apk`
- APK size: 386,592,386 bytes
- Package: `in.abstractit.gd.math.test`
- Version: `v4.4.3` (version code `80`)
- Requested levels: `mergeExample`, `introLevelStack`, `simpleIdentificationFruitsSet1`

## Readiness and blocker

**Result: BLOCKED — device test could not start.**

`adb devices -l` reported no connected or running Android device. The available Android emulator could not start because the current user lacks permission to use `/dev/kvm`:

- `/dev/kvm`: group `kvm`, permissions `crw-rw----+`
- Current user groups: `abs-bot-01 users dvc`
- `kvm` group membership does not include the current user.
- Emulator error: `x86_64 emulation currently requires hardware acceleration!` and `This user doesn't have permissions to use KVM (/dev/kvm).`

Installation, application launch, level navigation, gameplay, screenshots, and completion checks were therefore not performed. APK contents are not treated as gameplay evidence.

## Per-level report

### Level: `mergeExample`
Result: `FAIL` (blocked/not tested)
Boards tested: `0`
Tiles tested: `0`
Observed board time: `Not measured`

Passed checks:
* None — no authorized Android test target was available.

Issues found:
* **Blocker:** No ADB device/emulator available. Emulator startup failed due to missing `/dev/kvm` permission.

Evidence:
* Diagnostic output recorded in `tester-data/journals/2026-09-07-level-test.jsonl`.
* No tile or completion screenshots were produced because the app could not be installed/launched.

Status:
`deviceTestFailed`

### Level: `introLevelStack`
Result: `FAIL` (blocked/not tested)
Boards tested: `0`
Tiles tested: `0`
Observed board time: `Not measured`

Passed checks:
* None — no authorized Android test target was available.

Issues found:
* **Blocker:** No ADB device/emulator available. Emulator startup failed due to missing `/dev/kvm` permission.

Evidence:
* Diagnostic output recorded in `tester-data/journals/2026-09-07-level-test.jsonl`.
* No tile or completion screenshots were produced because the app could not be installed/launched.

Status:
`deviceTestFailed`

### Level: `simpleIdentificationFruitsSet1`
Result: `FAIL` (blocked/not tested)
Boards tested: `0`
Tiles tested: `0`
Observed board time: `Not measured`

Passed checks:
* None — no authorized Android test target was available.

Issues found:
* **Blocker:** No ADB device/emulator available. Emulator startup failed due to missing `/dev/kvm` permission.

Evidence:
* Diagnostic output recorded in `tester-data/journals/2026-09-07-level-test.jsonl`.
* No tile or completion screenshots were produced because the app could not be installed/launched.

Status:
`deviceTestFailed`

## Required remediation

Provide an authorized Android device/emulator visible to `adb devices -l`, or grant this user access to `/dev/kvm` (normally by adding the user to the `kvm` group and starting a new login/session), then rerun the requested workflow from installation through final screenshots.

No gameplay behavior, UI, maths/content, TTS, audio, animation, performance, incorrect-input, or board-timing claims are made from this blocked run.
