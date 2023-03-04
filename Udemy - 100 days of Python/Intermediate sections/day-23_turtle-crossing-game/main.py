import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FINISH_LINE_Y, SPAWN_INTERVAL, COLLISION_RANGE

# create screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

# create turtle player that starts at the bottom-center of the screen
player = Player()
# add ability to move turtle forward by pressing the up key
screen.onkey(player.move_up, "Up")

# create scoreboard that displays the player current level
scoreboard = Scoreboard()

# cars manager instance
cars = CarManager()

game_is_on = True
loop_counter = SPAWN_INTERVAL
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create a car 20px high by 40px wide that starts at the right edge of the screen and continuously moves forward
    # add the ability to spawn a new car every n-th time the game loop runs, n being a constant that represents the spawn interval
    if loop_counter == SPAWN_INTERVAL:
        cars.render_car()
        loop_counter = 1
    cars.move()

    # add the ability to check when turtle reaches the top of the screen
    if player.ycor() >= FINISH_LINE_Y:
    # clear all cars in the screen from the previous level
        cars.reset_all_cars()
    # restart turtle position to the bottom of the screen every time the turtle reaches the top
        player.restart_position()
    # increase player level and refresh scoreboard when turtle reaches the top of the screen
        scoreboard.increase_level()
    # add the ability to increase car speed at each level
        cars.increase_pace()

    # add the ability to detect collision between a car and turtle
    # end the game loop when a collision between car and turtle is detected
    for car in cars.all_cars:
        if car.distance(player) < COLLISION_RANGE:
    # add the ability to display a game over message in the scoreboard when a collision between car and turtle is detected
            scoreboard.render_game_over()
            game_is_on = False

    loop_counter += 1


screen.exitonclick()
