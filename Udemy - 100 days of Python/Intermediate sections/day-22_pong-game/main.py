# TODO: create the screen where the game will be played
from turtle import Screen
from paddle import Paddle

# Game settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, P1_COORDINATES, P2_COORDINATES

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)
screen.listen()

# TODO: create and move paddle
player_1 = Paddle(P1_COORDINATES)
# move the player_1 paddle when up and down keys are pressed
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")

# TODO: create another paddle
player_2 = Paddle(P2_COORDINATES)
# move the player_2 paddle when w and s keys are pressed
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")


# game state flag
game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()


# TODO: create ball and make it move

# TODO: detect collision with wall and bounce

# TODO: detect collision with paddle and bounce

# TODO: detect when paddle misses and the other player scores

# TODO: keep and display score