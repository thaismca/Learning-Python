# TODO: create the screen where the game will be played
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Game settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLLISION_BUFFER, PADDLE_STRETCH, P1_COORDINATES, P2_COORDINATES

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

# TODO: create ball and make it move
ball = Ball()

# game state flag
game_is_on = True
# x coordinate that would touch the surface of the right paddle
max_x_right = player_1.xcor() - COLLISION_BUFFER
# x coordinate that would touch the surface of the left paddle
min_x_left = player_2.xcor() + COLLISION_BUFFER


while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

# TODO: detect collision with wall and bounce
    ball_y = ball.ycor()
    if ball_y > SCREEN_HEIGHT/2 - COLLISION_BUFFER or ball_y < -SCREEN_HEIGHT/2 + COLLISION_BUFFER:
        ball.bounce_y()

# TODO: detect collision with paddle and bounce
    '''This collision will be detected by checking two conditions: 
        - if the ball has reached the xcor that would touch the paddle, and it's still within the bounds (player's xcor)
        - and if the paddle is within the distance represented by half of the paddle size.
    Cannot rely only in a fixed distance between ball and paddle, because this distance is measured considering the center of each object,
    and this distance may vary depending on where in the paddle the collision with the ball will happen.'''
    # player_1 (right paddle)
    if player_1.xcor() > ball.xcor() > max_x_right and ball.distance(player_1) < PADDLE_STRETCH * 10:
        ball.bounce_x()
        # this prevents bug where ball will move along the length of the paddle
        ball.setposition(max_x_right - 1, ball.ycor())

    # player 2 (left paddle)
    if player_2.xcor() < ball.xcor() < min_x_left and ball.distance(player_2) < PADDLE_STRETCH * 10:
        ball.bounce_x()
        ball.setposition(min_x_left + 1, ball.ycor())

    # could have used an 'or' to link both conditionals above, but decided to keep them separate for better code readability


screen.exitonclick()

# TODO: detect when paddle misses and the other player scores

# TODO: keep and display score