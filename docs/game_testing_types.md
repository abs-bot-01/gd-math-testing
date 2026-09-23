# Game Testing Types

Common ways to test a video game. The examples use simple English and can be used for any type of game.

| What the tester does | Testing type | Simple meaning | Simple game example |
|---|---|---|---|
| Check that the game starts | Smoke testing | A quick check of the most important parts | Open the game, start a level, and make one move. Make sure the game does not crash. |
| Check that a feature works | Functional testing | Check that each feature works as planned | Move the player, pick up an item, and check that the item appears in the inventory. |
| Test old features after a change | Regression testing | Make sure a new change did not break something else | After changing the inventory, check that players can still save and load the game. |
| Test a recent fix | Sanity testing | Check that a small change works | After fixing the jump button, press it and check that the player jumps. |
| Follow written steps | Scripted testing | Test the game by following a list of steps | Follow the steps to start a level, finish it, and return to the main menu. |
| Play without written steps | Exploratory testing | Look around and try different actions to find problems | Try different paths, buttons, and objects to see if anything behaves badly. |
| Try a quick informal test | Ad hoc testing | Test an idea without a full test plan | Try to repeat a reported problem in a few different ways. |
| Use random or fast actions | Monkey testing | Use unexpected actions to find crashes or errors | Press buttons quickly, open menus again and again, and move during a screen change. |
| Use wrong or missing input | Negative testing | Check that the game handles wrong actions safely | Try to use an item that is not in the inventory. Make sure the game shows a clear message and does not crash. |
| Test the lowest and highest values | Boundary testing | Check the edges of the allowed limits | Test zero lives, one life, full health, and the highest possible score. |
| Check that features work together | Integration testing | Check that connected features work together | Complete a quest and check that the goal changes, the reward is given, and the item is saved. |
| Test the whole game | System testing | Test the complete game from start to finish | Start the game, play a level, pause, save, quit, load the game, and finish the level. |
| Check that the game meets the plan | Acceptance testing | Make sure the game meets the agreed needs | Check that players can start the game, play the main mode, and finish a level. |
| Test buttons and controls | Input testing | Check that controls do the right thing | Test the keyboard, mouse, controller, and touch controls if they are supported. |
| Check screens and buttons | UI testing | Check how the game looks and works on screen | Make sure text, buttons, menus, icons, and scores are easy to see and use. |
| Check if the game is easy to use | Usability testing | Check that players understand what to do | Ask a new player to start a level and see if they can play without help. |
| Check support for different players | Accessibility testing | Check that more people can play the game | Test subtitles, readable text, color choices, larger text, and changed controls. |
| Test different devices | Compatibility testing | Check that the game works in supported setups | Test the game on supported computers, consoles, phones, screen sizes, and controllers. |
| Check speed and stability | Performance testing | Check that the game is fast and does not freeze | Play a busy level and check that it loads quickly and runs smoothly. |
| Test online play | Network testing | Check the game when the internet is good or bad | Disconnect the internet during a match and check that the game responds safely. |
| Check saved progress | Save and load testing | Check that progress is saved and restored | Save the game, close it, open it again, and check that progress is still there. |
| Check sound and pictures | Audio and graphics testing | Check sounds, music, images, and effects | Make sure music, sounds, animations, and effects play at the right time. |
| Check game content | Content testing | Check that game information is correct and complete | Check level names, instructions, item names, goals, and rewards. |
| Check game safety and fairness | Security testing | Look for ways to break rules or access protected data | Try to change a save file or get an item twice. Make sure the game prevents this. |
| Check install and updates | Installation and update testing | Check that the game can be installed and updated | Install the game, update it, and make sure saved progress still works. |
