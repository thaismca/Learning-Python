
# TURTLE CROSSING GAME

This project implements a game that challenges player cross the turtle from the bottom to the top of the screen without being hit by a car. Each time the player reaches the top, a new and more challenging level starts.

This game was implemented as part of the day 23 capstone project of the course *100 days of Python*. All implementation was taken care of prior to watch the solution videos.

## Key differences from course solution

- All values in the course solutions were hard coded, while this solution allows for customization by changing values from the Settings file.

## How this app works

1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.
## Implementation notes

**GAME SETTINGS**

The file *settings.py* have some game settings that can be changed, making the implementation more dinamic.

**Screen:**
 - SCREEN_WIDTH: width of the screen
 - SCREEN_HEIGHT: height of the screen
 - FINISH_LINE_Y: y coordinate for the level finish line
 - SAFE_ZONE: area added to the top and bottom of the screen where cars won't spawn

Screen size can be ajusted. Adjustments in the screen height allows for more or less car rows. Increasing the width makes it easier for the player to anticipate and action, while decreasing it makes it more challenge due to cars being spawned closer to the player.

Finish line is calculated based on the screen height. It deducts a turtle default size (20) from the max y coordinate.

Safe zone is the buffer area where cars cannot spawn in the y axis. If it's decreased, the cars corridor gets narrower.


**Player:**
 - PLAYER_START_POSITION: coordinates where the player starts each level
 - PLAYER_MOVE_PACE: distance that the player moves at each key press

Player start point will dinamically change, based on the screen height. It deducts a turtle default size (20) from the min y coordinate.

Player moving pace can be ajusted, depending on the feel that the develpoer wants from the gameplay.


**Cars:**
 - CAR_COLORS: list of colors that a car can have
 - CAR_START_MOVE_PACE: distance that the car moves at each game loop at level 1
 - CAR_MOVE_INCREMENT: quantity that the car pace gets incremented by at each level
 - SPAWN_RANGE_MIN: lower y coordinate where a car can spawn
 - SPAWN_RANGE_MAX: higher y coordinate where a car can spawn
 - SPAWN_INTERVAL: amount of loops that need to go by before a new car spawns

Each car color is chosen randomly at each spawn from the array of car colors in the settings, feel free to add, remove or change the colors. It's just cosmetic.

Spawn range min and max are calculated based on the screen height, deducting the safe zone.

Move pace, increment and spawn interval can be adjusted, depending on the developer's game feel.

**Player and cars collision:**
 - COLLISION_RANGE: distance between car and player that triggers the collision

Collision range can be adjusted, depending on the developer's game feel.

** Scoreboard:**
 - LEVEL_TEXT_FONT: font for the level indicator text
 - LEVEL_TEXT_POSTION = position where level text is rendered(-SCREEN_WIDTH/2 + 30, SCREEN_HEIGHT/2 - 30)
 - GAME_OVER_TEXT_FONT = ("Courier", 24, "bold")

Level text position is calculated based on the screen height and width, deducting an amount that can be adjusted freely to put a distance between the text and the screen edge.