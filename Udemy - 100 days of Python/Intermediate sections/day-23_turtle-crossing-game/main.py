import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FINISH_LINE_Y

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

# TODO: create turtle player that starts at the bottom-center of the screen
player = Player()
# TODO: add ability to move turtle forward by pressing the up key
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO: add the ability to check when turtle reaches the top of the screen
    if player.ycor() >= FINISH_LINE_Y:
    # TODO: restart turtle position to the bottom of the screen every time the turtle reaches the top
        player.restart_position()


screen.exitonclick()


# TODO: create scoreboard that displays the player current level
# TODO: increase player level and refresh scoreboard when turtle reaches the top of the screen
# TODO: create a car 20px high by 40px wide that starts at the right edge of the screen and continuously moves forward
# TODO: add the ability to randomize the car spawn point in the y axis, excluding a safe zone at both bottom and top areas of the screen
# TODO: add the ability to spawn a new car every n-th time the game loop runs, n being a constant that represents the spawn rate
# TODO: add the ability to randomize car color
# TODO: add the ability to increase car speed at each level
# TODO: add the ability to detect collision between a car and turtle
# TODO: add the ability to display a game over message in the scoreboard when a collision between car and turtle is detected
# TODO: end the game loop when a collision between car and turtle is detected