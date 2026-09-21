---
type: Flow
title: "Flow — explore-20260902-1112"
description: "Explore the main user-facing flows and identify important defects or blockers."
events: events.json
tags: [run, explore]
result: partial
generated: { by: tester/1.0, at: 2026-09-02T06:03:13Z }
---

# Flow — explore-20260902-1112

Explore the main user-facing flows and identify important defects or blockers.

- **project:** [gd-math](../../index.md)
- **target:** `/home/abs-bot-01/Downloads/gd-math.x86_64`
- **mode:** explore
- **boundary:** Safe exploratory testing only; no purchases, messages, deletions, or production changes.
- **environment:** Linux disposable Xvfb desktop at 1280x720
- **started:** 2026-09-02T05:49:04Z
- **status:** partial — Explored the main menu, first puzzle flow, parent-gated About Us, Settings, Library scrolling, and Pattern activity. The app launches and major navigation surfaces are usable. One Pattern lesson produced a blank, apparently unrecoverable exercise state and was recorded as a medium-severity needs-retest finding.

## Contents

- [Coverage](#coverage)
- [Blocked work](#blocked-work)
- [Summary](#summary)
- [Evidence](#evidence)

Step anchors: [1](#seq-1) · [2](#seq-2) · [3](#seq-3) · [4](#seq-4) · [5](#seq-5) · [6](#seq-6) · [7](#seq-7) · [8](#seq-8)

## Coverage

<a id="seq-1"></a>

### 1 — Launch app and inspect main menu (`passed`)

**expected:** App opens to a usable main menu

**observed:** Main menu opens in a 1200x675 window with score 20, Player1, settings, play, library, About Us, Report Card, and Subscribe controls.

![main-menu](artifacts/main-menu.png)

*main-menu — Launch app and inspect main menu*

<a id="seq-2"></a>

### 2 — Play first visible puzzle and drag an apple into the empty slot (`passed`)

**expected:** The puzzle accepts the item and advances or provides clear feedback.

**observed:** Puzzle screen shows instruction ONE SLOT TWO APPLES with two apple cards and one empty slot; dragging the left apple toward the slot visibly moves the card, but no success/advance feedback is shown in the captured state.

![puzzle-after-drag](artifacts/puzzle-after-drag.png)

*puzzle-after-drag — Play first visible puzzle and drag an apple into the empty slot*

<a id="seq-3"></a>

### 3 — Open About Us and inspect parent gate (`passed`)

**expected:** About information opens with an understandable access control.

**observed:** A parent-only gate appears, recommending a device screen lock, with red X and green check controls; tapping X returns to the main menu.

![about-parent-gate](artifacts/about-parent-gate.png)

*about-parent-gate — Open About Us and inspect parent gate*

<a id="seq-4"></a>

### 4 — Open Settings (`passed`)

**expected:** Settings screen is readable and controls respond.

**observed:** Settings shows Kiosk Mode toggle (off), a time slider displaying 04:00, a second slider displaying 60, Reset button, Home button, and Help button.

![settings](artifacts/settings.png)

*settings — Open Settings*

<a id="seq-5"></a>

### 5 — Open Library (`passed`)

**expected:** Available learning levels are listed clearly and can be selected.

**observed:** Library opens with cards for levels 2 through 7, labeled Age 2 through Age 7, and a visible vertical scrollbar indicating more content below.

![library](artifacts/library.png)

*library — Open Library*

<a id="seq-6"></a>

### 6 — Scroll Library to lower content (`passed`)

**expected:** Additional activity cards are reachable and remain readable.

**observed:** Additional cards are visible: Match, Colours, Pattern, Count, Audio, and Fill.

![library-lower](artifacts/library-lower.png)

*library-lower — Scroll Library to lower content*

<a id="seq-7"></a>

### 7 — Open Pattern activity (`passed`)

**expected:** Pattern activity presents a clear set of lessons or exercises.

**observed:** Pattern page opens with title Pattern and list entries including duplicated What is a Pattern? rows, Pattern with Fruits - Part 1, Pattern with Vegetables - Part 1, and Rotating Fan with SFX - Example; scrollbar indicates more entries.

![pattern-list](artifacts/pattern-list.png)

*pattern-list — Open Pattern activity*

<a id="seq-8"></a>

### 8 — Observe Pattern exercise after selecting duplicated lesson (`blocked`)

**expected:** A usable exercise loads with cards or instructions.

**observed:** The exercise remains on the wooden board with only the heading ONE SLOT TWO APPLES; the content cards disappear and no instructions, controls, completion state, or recovery control become visible during observation.

**notes:** Potential blocker; needs retest across restart/other levels.

![pattern-stuck](artifacts/pattern-stuck.png)

*pattern-stuck — Observe Pattern exercise after selecting duplicated lesson*

## Blocked work

- seq 8: Observe Pattern exercise after selecting duplicated lesson

## Summary

Explored the main menu, first puzzle flow, parent-gated About Us, Settings, Library scrolling, and Pattern activity. The app launches and major navigation surfaces are usable. One Pattern lesson produced a blank, apparently unrecoverable exercise state and was recorded as a medium-severity needs-retest finding.

## Evidence

- [main-menu.png](artifacts/main-menu.png)
- [puzzle-after-drag.png](artifacts/puzzle-after-drag.png)
- [about-parent-gate.png](artifacts/about-parent-gate.png)
- [settings.png](artifacts/settings.png)
- [library.png](artifacts/library.png)
- [library-lower.png](artifacts/library-lower.png)
- [pattern-list.png](artifacts/pattern-list.png)
- [pattern-stuck.png](artifacts/pattern-stuck.png)
