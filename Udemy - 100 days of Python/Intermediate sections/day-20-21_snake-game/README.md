# Snake Game

This project implements a clone of the Snake Game.

This game was implemented as part of the days 20 and 21 of the course 100 days of Python. All implementation was taken care of prior to watch the solution videos.

## Key difference from course solution

- All values in the course solution were hard coded, while this solution allows for customization by changing values from the Settings file.

## How it works

The player controls a long, thin creature, resembling a snake, which roams around on a bordered plane, picking up food (represented by a green dot), trying to avoid hitting its own tail or the edges of the playing area. Each time the snake eats a piece of food, its tail grows longer, making the game increasingly difficult.

The snake will be constantly moving forward, and there's a small increase on its speed as it grows longer.

In order to control the snake, player must use the arrow keys from the keyboard to change its movement direction.

![snake game screenshot](https://github.com/thaismca/Python-Practices/blob/0eecb05e73e617c610074589f93e1a0d17297b84/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-20-21_snake-game/snake_screenshot.png?raw=true)

## Implementation notes

#### GAME SETTINGS

The file settings.py have some game settings that can be changed, making the implementation more dinamic.

SCREEN_WIDTH: width of the screen
SCREEN_HEIGHT: height of the screen
SPEED: speed of snake at game start
SHAPE_STRETCH: applies for food and snake turtle shapes (default turtle shape size is 20x20)

SAVE_FILE_PATH: path for the file where the save will be kept

#### SNAKE

The file snake.py implements a class Snake, which models a Snake that represents the player in the game.

__Snake settings__

- STARTING_POS: array of tuples that represent the coordinates for the snake segments at the game start. A segment will be created and placed at each given coordinate of this array when game starts.

- MOVE_DISTANCE: represents the distance that segments run at each frame. Since default size for turtle shapes is 20x20, the move distance is set to 20*SHAPE_STRETCH. It's not reccomended to change this formula, as this can break the snake shape.

__Snake Class__

- constructor: creates a snake with an array of segments and set the snake head to the segment at the position 0 of this array.

- create_snake(): generates the first segments of an snake, considering the coordinates in the STARTING_POS array. The snake will haev as many segments as the number of coorinate tuples in this STARTING_POS array when the game starts.

- add_segment(position): adds a new segment to the given position. Called inside of the _create_snake()_ method.

- extend(): adds a new segment after the current last one.

- move(): moves the snake constantly forward at a given pace, determined by MOVE_DISTANCE.

- reset_snake(): clear current snake segments and creates a new starting snake.

- up(), down(), left(), right(): turn snake direction, if it's currently not moving towards the opposite direction (snake cannot flip direction).

#### FOOD

The file food.py implements a class Food, which models the food that the player collects during the game.

- constructor: creates a food object (green small circle) at a randon position inside of the screen.

- refresh_position(): sets new random x and y cordinates and moves the food to that position. To be called whenever the food is collected (collision detected).

#### SCOREBOARD

The file scoreboard.py implements a class Scoreboard, which models the score information that is displayed in the screen during the game.

- constructor: creates a scoreboard object at the top of the screen. This scoreboard display a current score that starts at zero, and the player's high score, that is retrieved from the save file

- render_score(): clears previous scoreboard and renders it again. Called every time the score changes.

- increase_score(): increases score by one and updates the rendered text.

- reset_score(): replaces high score if it was beaten, and resets score for a new game. High score gets written to data file.

#### MAIN

The file main.py implements the game loop. This is the file that must be executed in order to run the game.



