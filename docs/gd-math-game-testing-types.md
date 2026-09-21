# GD Math Game Testing Types

This document defines the main testing types for a Godot math game. The goal is to verify that the game generates valid questions, accepts answers correctly, provides clear feedback, and supports a smooth learning experience.

## Table of Contents

1. [Testing Definitions and Simple GD Math Purposes](#testing-definitions-and-simple-gd-math-purposes)
2. [Detailed Testing Checks](#detailed-testing-checks)

## Testing Definitions and Simple GD Math Purposes

| Testing type | Definition | Simple GD Math purpose |
|---|---|---|
| Smoke Testing | A quick check of the most important functions after a build or launch. | Open the game, press **Start Game**, and confirm that a math level starts. |
| Functional Testing | Testing whether each feature works according to its requirements. | Check arithmetic answers, player actions, score updates, timers, and level progression. |
| Regression Testing | Rechecking existing features after a change to make sure nothing has broken. | After adding a new arithmetic level, verify that old levels, controls, and scoring still work. |
| UI/UX Testing | Checking the interface and the overall experience for visual or interaction problems. | Check the Answer, Next Level, Pause, and Resume buttons, menus, question text, and feedback. |
| Performance Testing | Checking speed, responsiveness, loading time, and stability. | Confirm that the game does not lag or freeze when many arithmetic questions or levels are loaded. |
| Compatibility Testing | Checking whether the game works across supported devices, screen sizes, and operating systems. | Confirm that questions and answer choices display correctly on Android, iPhone, desktop, and different screen sizes. |
| Usability Testing | Checking whether new or intended users can understand and use the game easily. | Confirm that a new player understands how to read a question and select an answer. |
| Negative Testing | Providing invalid or unexpected input to check that the game handles it safely. | Submit an empty, non-numeric, or invalid answer and confirm that the game shows a helpful message without crashing. |
| Boundary Testing | Testing values at, just inside, and just outside the allowed limits. | If a value range is **1 to 10**, test **1, 2, 9, and 10**, then check that **0** and **11** are rejected correctly. |
| Save/Load Testing | Checking whether progress is stored and restored correctly. | Complete Level 5, restart the game, and confirm that the completed level and score are still available. |
| Audio/Graphics Testing | Checking sound, music, animation, visual effects, and their timing. | Confirm that correct answers play success feedback, wrong answers play error feedback, and animations display correctly. |
| Recovery Testing | Checking how the game handles a crash, unexpected close, or interruption. | Close the game during a math level, reopen it, and confirm that saved progress is recovered safely. |

## Detailed Testing Checks

### 1. Functional Testing

Verify that each game feature works according to its requirements.

Check:

- The Play button opens the level-selection screen.
- A category opens the correct levels.
- An answer can be entered or selected.
- Correct answers produce positive feedback.
- Incorrect answers produce clear feedback.
- The score updates correctly.
- The timer starts, pauses, and ends correctly.
- The next question appears when expected.
- Level completion and game-over screens appear correctly.
- Restart resets the correct game state.

### 2. UI/UX and Usability Testing

Check whether the game is clear and easy to operate.

Verify:

- Questions are readable.
- Buttons are large enough and clearly labeled.
- The current score and timer are visible.
- Correct and incorrect feedback is easy to understand.
- Instructions explain the objective and controls.
- The player knows what to do next.
- Text does not overlap or disappear.
- The layout remains usable when the window is resized.

### 3. Negative and Boundary Testing

Test invalid input and values at the limits.

Try:

- Submitting an empty answer
- Entering letters when only numbers are expected
- Entering a decimal when decimals are not supported
- Entering a very large number
- Submitting repeatedly
- Pressing buttons rapidly
- Answering after the timer reaches zero
- Playing the first and last level
- Reaching zero lives
- Reaching the maximum score
- Restarting during a question
- Going back during a level

The game should reject unsafe or invalid input without crashing or corrupting progress.

### 4. Regression Testing

Repeat important existing tests after every significant change.

Minimum regression flow:

1. Launch the game.
2. Start a level.
3. Answer one question correctly.
4. Answer one question incorrectly.
5. Confirm score and feedback.
6. Complete or exit the level.
7. Restart the game.
8. Confirm that progress and menus behave as expected.

### 5. Performance Testing

Check whether the game remains responsive.

Test:

- Initial launch time
- Level loading time
- Question transition time
- Frame rate during animations
- Memory usage after many rounds
- Performance on low-end devices
- Long sessions for possible memory leaks

### 6. Compatibility Testing

Test supported platforms and input methods.

Check:

- Godot desktop export
- Mobile export, if supported
- HTML5 export, if supported
- Different screen sizes and aspect ratios
- Keyboard and mouse input
- Touch input
- Portrait and landscape orientation, if applicable

### 7. Save/Load Testing

Verify that player progress, completed levels, scores, and other required state are saved and restored correctly.

Example:

- Complete Level 5.
- Close and restart the game.
- Confirm that Level 5 completion and the expected score are still available.
- Confirm that incomplete or invalid data does not corrupt the saved progress.

### 8. Audio/Graphics Testing

Verify that the game's sound, music, animations, and visual effects work correctly.

Check:

- A success sound plays for a correct answer.
- An error sound plays for an incorrect answer.
- Music starts, pauses, resumes, and stops as designed.
- Animations play at the correct time.
- Visual feedback is visible and matches the answer result.
- Audio controls and mute settings work correctly.

### 9. Recovery Testing

Verify that the game handles unexpected closure, crashes, or interruptions safely.

Example:

- Close the game during an arithmetic level.
- Reopen the game.
- Confirm that saved progress is recovered, or that the game starts safely without corrupt data.
- Confirm that the player is not incorrectly awarded points for an unanswered question.

