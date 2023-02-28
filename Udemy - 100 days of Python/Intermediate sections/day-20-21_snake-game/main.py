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

# create a snake body with three segments at start
starting_positions = [(0,0), (-20,0), (-40,0)]
snake = []
for pos in starting_positions:
    new_segment = Turtle()
    new_segment. shape('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(pos)
    snake.append(new_segment)

# game flag
game_is_on = True
screen.listen()

# game loop
while game_is_on:
    screen.update()
    time.sleep(1 / SPEED)
    for segment in range(len(snake) - 1, 0, -1):
        snake[segment].goto(snake[segment - 1].pos())
    snake[0].forward(20)




screen.exitonclick()