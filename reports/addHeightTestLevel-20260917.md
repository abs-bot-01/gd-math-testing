# QA Test Report

## Test Summary

**Result: BLOCKED / INCOMPLETE**

- Target: `addHeightTestLevel`
- Run: `addHeightTestLevel-20260917`
- Target mode: desktop Godot direct run, `DISPLAY=:16.0`
- Selector: `GDM_LEVEL_ID=addHeightTestLevel`
- Runtime: Godot 4.6.1, Mesa llvmpipe
- Configured boards: 5
- Boards rendered: 1/5
- Boards completed: 0/5
- Full-level completion: not verified
- Android/device coverage: not tested

The first board rendered and matched the configured title. The required merge interaction did not produce a merged tile, so the flow could not reach target completion or the remaining boards.

## Level Details

Source configuration was read from `data/yamlFiles/levels.yaml` and runtime configuration from `assets/config.json`.

- ID: `addHeightTestLevel`
- Title: `Merge Tiles to Make Length - Set 1 - LO`
- Skill age: 9
- Branch: Measurements
- Type/parser: `icmV2`
- Variants: `numberTile` → `numberSlot`
- Tags: `length|master|v5.8`
- Configured board count: 5
- Intended rule: merge compatible centimetre tiles, then place the result in the matching slot
- Runtime/source identity: matched

## Runtime Evidence

### Initial playable board

![Board 1 ready](../artifacts/addHeightTestLevel-20260917/05_board1_ready.png)

**Expected:** A playable board for the requested level is displayed.

**Actual:** The requested title is visible. Board 1 displayed source tiles `10 cm`, `20 cm`, `30 cm`, and `80 cm`, with target slots `50 cm` and `90 cm`.

**Result:** PASS for rendering and identity.

### Merge attempt

![Before merge](../artifacts/addHeightTestLevel-20260917/06_before_merge_30_20.png)

**Expected:** Dragging `30 cm` onto `20 cm` creates a `50 cm` merged result.

![After merge](../artifacts/addHeightTestLevel-20260917/07_after_merge_30_20.png)

**Actual:** The `30 cm` tile moved but remained separate; no `50 cm` result, acceptance feedback, target fill, or board transition appeared.

**Result:** FAIL; full flow BLOCKED.

## QA Properties

1. **Identity** — Expected: requested level identity. Actual: title matched. Status: **PASS**. Evidence: `05_board1_ready.png`.
2. **Configuration** — Expected: runtime entry with five boards and `icmV2`. Actual: source/runtime values matched. Status: **PASS**. Evidence: `assets/config.json`, `levels.yaml`.
3. **Learning objective** — Expected: combine centimetre tiles to equivalent lengths. Actual: objective is present in source metadata. Status: **PASS**. Evidence: `levels.yaml`.
4. **Board layout** — Expected: source tiles and target slots visible. Actual: four tiles and two targets visible. Status: **PASS**. Evidence: `05_board1_ready.png`.
5. **Visual content** — Expected: readable values and units. Actual: values and `cm` labels readable. Status: **PASS**. Evidence: `05_board1_ready.png`.
6. **Image/asset quality** — Expected: assets render without blocking corruption. Actual: board and tile assets rendered. Status: **PASS**. Evidence: `05_board1_ready.png`.
7. **Alignment** — Expected: controls aligned within the board. Actual: board rendered; one source tile overlapped the visual area of a target. Status: **OBSERVED; not fully assessed**. Evidence: `05_board1_ready.png`.
8. **Scale/aspect ratio** — Expected: usable desktop layout. Actual: playable board fit the window. Status: **PASS**. Evidence: `05_board1_ready.png`.
9. **Safe margins** — Expected: interactive content stays inside board. Actual: visible content stayed inside the board. Status: **PASS**. Evidence: `05_board1_ready.png`.
10. **Text/labels** — Expected: title and measurement labels are readable. Actual: title and labels were readable. Status: **PASS**. Evidence: `05_board1_ready.png`.
11. **Touch/pointer interaction** — Expected: drag interaction accepted. Actual: drag delivered, but merge was not accepted. Status: **FAIL**. Evidence: `06_before_merge_30_20.png`, `07_after_merge_30_20.png`.
12. **Hitboxes** — Expected: tile-to-tile drop hitbox works. Actual: no merge on a current-board tile drop. Status: **FAIL**. Evidence: `06_before_merge_30_20.png`, `07_after_merge_30_20.png`.
13. **Valid interaction** — Expected: `30 + 20` produces `50`. Actual: tiles remained separate. Status: **FAIL**. Evidence: `07_after_merge_30_20.png`.
14. **Invalid interaction** — Expected: invalid drop is safely rejected with feedback. Actual: not separately tested after the merge blocker. Status: **NOT TESTED**.
15. **Solution validation** — Expected: merged result can fill the matching slot. Actual: could not reach this step. Status: **BLOCKED**.
16. **Visual feedback** — Expected: merge/acceptance feedback. Actual: no merge feedback observed. Status: **FAIL**. Evidence: `07_after_merge_30_20.png`.
17. **Animation** — Expected: merge/completion animation where applicable. Actual: not reached. Status: **NOT TESTED**.
18. **Audio/TTS** — Expected: relevant feedback audio. Actual: not tested. Status: **NOT TESTED**.
19. **Instructions/hints** — Expected: usable instructions/hints. Actual: no separate hint flow tested. Status: **NOT TESTED**.
20. **Completion** — Expected: all five boards and final completion state. Actual: 0/5 boards completed. Status: **BLOCKED**.
21. **Performance** — Expected: stable playable runtime. Actual: board rendered; performance was not profiled. Status: **NOT TESTED**.
22. **Device quality** — Expected: target-device behavior. Actual: desktop only; Android/device not tested. Status: **NOT TESTED**.

## Findings

### `addHeightTestLevel-merge-tiles-not-accepted` — HIGH — new

The required merge interaction is not accepted. A compatible `30 cm` + `20 cm` drag leaves both tiles separate and prevents filling the `50 cm` target. The source level record itself notes that merge-and-fill is not possible because of label conversion and requires Godot development.

Structured record: `tester-data/findings.jsonl`.

### `godot-invalid-ext-resource-uid-fallback` — LOW — recurring

The launch log contains invalid external-resource UID warnings for `tracingOutline.ttf` in `character.tscn`, `tile.tscn`, and `slot.tscn`; Godot falls back to the text paths and the board still renders.

Evidence: `../artifacts/addHeightTestLevel-20260917/godot_rerun.log`.

## Coverage and Missing Evidence

- Board 1 rendered and one required merge action was attempted.
- Boards 2–5 were not tested because Board 1 could not progress.
- Full-level completion was not verified.
- Invalid interaction, animation, audio/TTS, hints, performance profiling, Android/device behavior, and final completion were not tested.
- The project source and runtime configuration were not modified.

## Overall Conclusion

The level is launchable and visually renders the requested Board 1, but the core merge-and-fill mechanic is blocked. The level cannot be considered functionally complete or passing until compatible tiles merge and the merged result can be placed into the target slot.
