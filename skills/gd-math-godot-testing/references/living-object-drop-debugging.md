# Living-Object Drop Debugging

Use this reference when a draggable result contacts an animated or static LivingObject near a destination slot and becomes rejected, thrown away, rotated, oversized, or misplaced.

## Diagnostic sequence

1. Re-capture the live board immediately before the drop and record the source, destination, platform bounds, and release point.
2. Compare the before/after state. If the source disappears and a malformed tile appears away from the slot, classify it as a drop-resolution/collision symptom, not a value-calculation failure.
3. Trace the runtime path in this order:
   - LivingObject collision handler: does contact force `dragState` to dropped, reset the parent, or call a throw-off/random-velocity helper?
   - Slot handler: did the slot's acceptance predicate run, and did it set the tile's parent/filled state?
   - Tile/GameObject drop helper: does rejection apply velocity or rotation after slot acceptance?
   - LivingObject scene: does its `StaticBody3D`/`CollisionShape3D` overlap the slot hitbox or the required drag route?
4. Use one bounded probe to separate causes: wait for the platform to clear and retry once, or test the same board with the obstacle extension disabled in a disposable runtime configuration. Do not keep changing coordinates after the malformed state reproduces with a different value or slot.

## Root-cause patterns

- If obstacle contact calls a throw-off path before the slot accepts the tile, slot geometry and arithmetic are not the primary fault; resolve drop ordering or collision priority.
- If the obstacle is decorative, remove its collision shape or collision layer rather than penalizing valid tiles.
- If the obstacle is intentionally interactive, defer rejection until release and give a valid slot acceptance priority. Track all overlapping obstacles instead of a single boolean when multiple LivingObjects can touch a tile.
- If the level configuration places obstacle paths over active slots, move the paths or remove that extension for the level; generated board validation must ensure every active slot has a reachable, non-overlapping drop region.

## Regression coverage

Add a focused regression test for both paths:

- valid result reaches a slot while crossing or touching an obstacle: slot fills, tile is not thrown away, and no malformed tile remains;
- invalid release on an obstacle without a valid slot: obstacle penalty still occurs.

Then run the exact level through the supported selector and verify at least one complete board plus the relevant collision log/state. Do not mark the full level fixed until every configured board completes.
