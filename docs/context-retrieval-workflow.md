# GD Math context retrieval for testing

Retrieve only context needed for the requested level. Do not scan the entire target repository by default.

## Required order

1. Read the target entry in the authoritative `levels.yaml`.
2. Read the exact target runtime entry in `assets/config.json`.
3. Read the target BLC or equivalent generated board/config record when available.
4. Read the testing/quality contract relevant to the mechanic.
5. Read the representative mechanic or representative level guidance when the target is tagged representative.
6. Read LivingObject/support-object guidance when an animated object can affect hitboxes or timing.
7. Build a context packet before significant gameplay decisions.

Design intent explains the learning objective and mechanic. Runtime configuration is authoritative for target-specific IDs, variants, counts, and board boundaries. Live screenshots are authoritative for what actually rendered and what the player could interact with. Record conflicts instead of silently reconciling them.

## Representative-first resolution

For a representative target:

1. match the exact `representative` tag token in `levels.yaml`;
2. identify the mechanic family;
3. read the representative learner flow and completion condition;
4. compare object roles, counts, layout, values, and completion behavior with the target;
5. test using the representative interaction model while checking target-specific differences.

Do not infer representative status from a title or prior report.

## Stop condition

Context retrieval is complete when the mathematical target, object roles, runtime boundaries, interaction method, completion signal, relevant obstacles, and remaining unknowns are recorded. Do not continue through linked documents that do not answer a current testing question.
