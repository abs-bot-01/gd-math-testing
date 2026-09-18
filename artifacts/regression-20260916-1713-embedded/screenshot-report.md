# Final Screenshot Visual QA Report

**Artifact set:** `regression-20260916-1713-embedded`  
**Review scope:** 24 application screenshots plus 3 generated contact sheets  
**Capture resolution:** 1280 × 720 for all application screenshots

## Screenshot gallery

The screenshots are embedded below so they are visible directly in the rendered report.

### Launch and play flow

![Launch screen](01_launch_initial.png)

![Play baseline](play_before.png)

![Play activity](play_after.png)

![Level before action](play_level_before_action.png)

![Level after action](play_level_after_action.png)

### Navigation flow

| Settings before | Settings after |
|---|---|
| ![Settings before](navigation/settings_before.png) | ![Settings after](navigation/settings_after.png) |

| Library before | Library after |
|---|---|
| ![Library before](navigation/library_before.png) | ![Library after](navigation/library_after.png) |

| Report Card before | Report Card after |
|---|---|
| ![Report Card before](navigation/report_before.png) | ![Report Card after](navigation/report_after.png) |

| Subscribe before | Subscribe after |
|---|---|
| ![Subscribe before](navigation/subscription_before.png) | ![Subscribe after](navigation/subscription_after.png) |

| About before | About after |
|---|---|
| ![About before](navigation/about_before.png) | ![About after](navigation/about_after.png) |

### Build smoke activities

![Count with single stick, 1 to 5](build_smoke/countWithSingleStick1To5_15s.png)

![Match audio count, 1 to 5](build_smoke/matchAudioCount1To5_15s.png)

![Stack yellow and green, set 1](build_smoke/stackYellowAndGreenSet1_15s.png)

### Level smoke activities

![Count with single stick, 1 to 3](level_smoke/countWithSingleStick1To3_15s.png)

![Grid, 4 rows by 4 columns](level_smoke/grid4Row4Column_15s.png)

![Merge hundreds and ones](level_smoke/mergeMatchHundredsOnesFrom100to999_15s.png)

![Merge numbers up to 7](level_smoke/mergeNumberUpTo7_15s.png)

![Order fractions](level_smoke/orderingFractions4_15s.png)

![Animal sound pattern](level_smoke/patternWithAnimalSounds_15s.png)

### Contact sheets

![Build smoke contact sheet](build_smoke/contact_sheet.png)

![Level smoke contact sheet](level_smoke/contact_sheet.png)

![Navigation contact sheet](navigation/navigation_contact_sheet.png)

## Executive summary

**Overall result: PASS — no visible blocking visual defects identified.**

The captured screens consistently render a polished 16:9 educational game UI. Main-menu navigation, parental-gate screens, library/about screens, gameplay boards, cards, illustrations, typography, and controls are visible and generally well aligned. No blank states, broken image assets, obvious overlap, or viewport-level clipping were found in the application screenshots.

The report is visual-only. It does not independently verify button behavior, audio, drag-and-drop correctness, persistence, scroll behavior, or whether a gameplay action produced the intended educational result.

## Key observations and follow-up items

- The `settings_after.png`, `report_after.png`, and `subscription_after.png` captures are pixel-identical and all show the same parent-only screen. This appears consistent with a shared parental-protection gate; verify the destination/content after selecting the confirmation control if those routes are expected to diverge.
- The five `*_before.png` navigation captures and `play_before.png` match the launch screen, which is appropriate for the shared main-menu baseline.
- `library_after.png` shows a partially visible third row inside a scrollable panel. The scrollbar makes this look intentional, but scrolling should be checked interactively to confirm that all cards are reachable.
- `about_after.png` shows a scrollable information panel with the `About`, `Privacy`, and `System Info` tabs. Only the visible portion of the About content was assessed.
- `play_level_before_action.png` and `play_level_after_action.png` show different activities. The transition is visually clean, but the screenshots alone cannot establish whether the action caused the intended level progression.

## Detailed results

### Launch and play flow

| Preview | Screenshot | Visual result | Notes |
|---|---|---|---|
| <img src="01_launch_initial.png" alt="Launch screen" width="240"> | [01_launch_initial.png](01_launch_initial.png) | **PASS** | Main menu renders correctly with coin balance, player identity, Settings, Play, Library, About Us, Report Card, and Subscribe controls. No visible overlap or clipping. |
| <img src="play_before.png" alt="Play baseline" width="240"> | [play_before.png](play_before.png) | **PASS** | Main-menu baseline before starting play; consistent with the launch screen. |
| <img src="play_after.png" alt="Play activity" width="240"> | [play_after.png](play_after.png) | **PASS** | Activity screen loads with the title `MATCH BASIC SHAPES FILL COLOR` and four clearly separated shape cards. |
| <img src="play_level_before_action.png" alt="Level before action" width="240"> | [play_level_before_action.png](play_level_before_action.png) | **PASS** | `ONE SLOT TWO APPLES` activity is framed correctly; apple cards and slot are visible and legible. |
| <img src="play_level_after_action.png" alt="Level after action" width="240"> | [play_level_after_action.png](play_level_after_action.png) | **PASS** | `MATCH BASIC SHAPES FILL COLOR` activity is rendered cleanly with matched square/triangle card content. |

### Navigation flow

| Preview | Screenshot | Visual result | Notes |
|---|---|---|---|
| <img src="navigation/settings_before.png" alt="Settings before" width="240"> | [navigation/settings_before.png](navigation/settings_before.png) | **PASS** | Main-menu baseline before navigation. |
| <img src="navigation/settings_after.png" alt="Settings after" width="240"> | [navigation/settings_after.png](navigation/settings_after.png) | **PASS** | Parent-only screen is legible; cancel and confirm controls are prominent and centered. |
| <img src="navigation/library_before.png" alt="Library before" width="240"> | [navigation/library_before.png](navigation/library_before.png) | **PASS** | Main-menu baseline before navigation. |
| <img src="navigation/library_after.png" alt="Library after" width="240"> | [navigation/library_after.png](navigation/library_after.png) | **PASS** | Library title, home control, activity cards, translucent panel, and scrollbar render correctly. |
| <img src="navigation/report_before.png" alt="Report Card before" width="240"> | [navigation/report_before.png](navigation/report_before.png) | **PASS** | Main-menu baseline before navigation. |
| <img src="navigation/report_after.png" alt="Report Card after" width="240"> | [navigation/report_after.png](navigation/report_after.png) | **PASS** | Parent-only protection screen renders consistently with Settings and Subscribe. |
| <img src="navigation/subscription_before.png" alt="Subscribe before" width="240"> | [navigation/subscription_before.png](navigation/subscription_before.png) | **PASS** | Main-menu baseline before navigation. |
| <img src="navigation/subscription_after.png" alt="Subscribe after" width="240"> | [navigation/subscription_after.png](navigation/subscription_after.png) | **PASS** | Parent-only protection screen renders consistently with Settings and Report Card. |
| <img src="navigation/about_before.png" alt="About before" width="240"> | [navigation/about_before.png](navigation/about_before.png) | **PASS** | Main-menu baseline before navigation. |
| <img src="navigation/about_after.png" alt="About after" width="240"> | [navigation/about_after.png](navigation/about_after.png) | **PASS** | About page has readable tab controls, scrollable content, character art, build ID, and home control. |

### Build smoke activities

| Preview | Screenshot | Visual result | Notes |
|---|---|---|---|
| <img src="build_smoke/countWithSingleStick1To5_15s.png" alt="Count with single stick, 1 to 5" width="240"> | [build_smoke/countWithSingleStick1To5_15s.png](build_smoke/countWithSingleStick1To5_15s.png) | **PASS** | `ONE BY ONE UP TO 5`; wooden board, source area, five stick cards, and slots are visible without obvious asset issues. |
| <img src="build_smoke/matchAudioCount1To5_15s.png" alt="Match audio count, 1 to 5" width="240"> | [build_smoke/matchAudioCount1To5_15s.png](build_smoke/matchAudioCount1To5_15s.png) | **PASS** | `COUNT & TELL UP TO 5`; megaphone prompts and counting cards are legible and well spaced. |
| <img src="build_smoke/stackYellowAndGreenSet1_15s.png" alt="Stack yellow and green, set 1" width="240"> | [build_smoke/stackYellowAndGreenSet1_15s.png](build_smoke/stackYellowAndGreenSet1_15s.png) | **PASS** | `SORT BY GREEN & YELLOW`; fruit cards and destination slots are clearly rendered on the board. |

### Level smoke activities

| Preview | Screenshot | Visual result | Notes |
|---|---|---|---|
| <img src="level_smoke/countWithSingleStick1To3_15s.png" alt="Count with single stick, 1 to 3" width="240"> | [level_smoke/countWithSingleStick1To3_15s.png](level_smoke/countWithSingleStick1To3_15s.png) | **PASS** | `ONE BY ONE UP TO 3`; two stick cards and slot areas are visible and aligned. |
| <img src="level_smoke/grid4Row4Column_15s.png" alt="Grid, 4 rows by 4 columns" width="240"> | [level_smoke/grid4Row4Column_15s.png](level_smoke/grid4Row4Column_15s.png) | **PASS** | `GROWING GRID CHALLENGE - SET 3`; numbered grid, dotted guides, and answer cards are visible. |
| <img src="level_smoke/mergeMatchHundredsOnesFrom100to999_15s.png" alt="Merge hundreds and ones" width="240"> | [level_smoke/mergeMatchHundredsOnesFrom100to999_15s.png](level_smoke/mergeMatchHundredsOnesFrom100to999_15s.png) | **PASS** | `HEAR & MERGE (100 TO 999) - SET 2`; number cards and audio prompts are rendered consistently. |
| <img src="level_smoke/mergeNumberUpTo7_15s.png" alt="Merge numbers up to 7" width="240"> | [level_smoke/mergeNumberUpTo7_15s.png](level_smoke/mergeNumberUpTo7_15s.png) | **PASS** | `ADD 1 TO GET NUMBERS UP TO 7`; operands and result cards are visible with clear spacing. |
| <img src="level_smoke/orderingFractions4_15s.png" alt="Order fractions" width="240"> | [level_smoke/orderingFractions4_15s.png](level_smoke/orderingFractions4_15s.png) | **PASS** | `ARRANGE FRACTIONS - SET 4`; fraction cards and four destination slots are legible. |
| <img src="level_smoke/patternWithAnimalSounds_15s.png" alt="Animal sound pattern" width="240"> | [level_smoke/patternWithAnimalSounds_15s.png](level_smoke/patternWithAnimalSounds_15s.png) | **PASS** | `ANIMAL SOUND PATTERN`; prompt cards, answer cards, and empty pattern slots are clearly visible. |

## Cross-screen visual checks

| Check | Result | Assessment |
|---|---|---|
| Viewport and framing | **PASS** | All application captures use 1280 × 720 and fill the frame appropriately. |
| Asset loading | **PASS** | No obvious missing, blank, or broken image assets. |
| Layout and alignment | **PASS** | Controls, cards, board frames, and panels are consistently aligned. |
| Text readability | **PASS** | Titles, labels, numbers, and navigation text are readable at the captured resolution. |
| Contrast and hierarchy | **PASS** | White/orange controls and white activity cards remain visually distinct from the illustrated backgrounds and wooden boards. |
| Clipping and overlap | **PASS** | No blocking overlap or unintended viewport clipping observed; scrollable content is noted above. |
| State transitions | **OBSERVE** | Before/after captures show clean visual state changes, but behavioral correctness requires interactive verification. |

## Contact sheets

These are derived overview images and are not additional application states:

- [build_smoke/contact_sheet.png](build_smoke/contact_sheet.png)
- [level_smoke/contact_sheet.png](level_smoke/contact_sheet.png)
- [navigation/navigation_contact_sheet.png](navigation/navigation_contact_sheet.png)

## Recommendation

Approve the screenshot set for visual presentation and regression evidence. Before final functional sign-off, verify the parental-gate confirmation paths, library/about scrolling, navigation destinations for Report Card and Subscribe, audio playback, and the semantic correctness of the gameplay transitions/actions.
