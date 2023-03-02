from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

# game settings
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, SPEED, SHAPE_STRETCH

#screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create game scoreboard instance
scoreboard = Scoreboard()
# create a snake instance
snake = Snake()
# create food instance
food = Food()

#listening for key presses to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

# game state flag
game_is_on = True
# game loop
while game_is_on:
    screen.update()
    time.sleep(1 / SPEED)
    snake.move()

    # detect collision with food by checking if the distance between snake head and food is less than food size (default shape size 20 * SHAPE_STRETCH)
    if snake.head.distance(food) < 20 * SHAPE_STRETCH:
        # move food to new position
        food.refresh_position()
        # update score
        scoreboard.increase_score()
        # extend snake -> add a segment after the current last one
        snake.extend()

    # detect collision with wall by checking if snake's head reaches a certain x or y cordinate right at the edge of the screen
    x_boundary = SCREEN_WIDTH/2
    y_boundary = SCREEN_HEIGHT/2
    # checking for collision in the four directions
    if snake.head.xcor() >= x_boundary or snake.head.xcor() <= -x_boundary or snake.head.ycor() >= y_boundary or snake.head.ycor() <= -y_boundary:
        game_is_on = False

    # detect collision between the snake's head and any other segment by checking
    # if the distance between head and any of the segments that represent the rest of the snake's body is less than half of a segment
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < (SHAPE_STRETCH * 20)/2:
            game_is_on = False


scoreboard.game_over()




screen.exitonclick()