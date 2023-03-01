from snake import Snake
from food import Food
from turtle import Turtle, Screen
import time

# SETTINGS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# speed reccommended to be between 1 and 10
SPEED = 10


#screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create a snake
snake = Snake()
# create food instance
food = Food()

# game flag
game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

# game loop
while game_is_on:
    screen.update()
    time.sleep(1 / SPEED)
    snake.move()

    # detect collision with food by checking if the distance between snake head and food is less than food size (10) + buffer -> 15
    if snake.head.distance(food) < 15:
        # move food to new position
        food.refresh_position()




screen.exitonclick()