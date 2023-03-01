from snake import Snake
from turtle import Turtle, Screen
import time

# SETTINGS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# speed reccommended to be between 1 and 10
SPEED = 5


#screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create a snake
snake = Snake()

# game flag
game_is_on = True
screen.listen()

# game loop
while game_is_on:
    screen.update()
    time.sleep(1 / SPEED)
    
    snake.move()




screen.exitonclick()