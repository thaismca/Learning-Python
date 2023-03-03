from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Game settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLLISION_BUFFER, PADDLE_STRETCH, R_PLAYER_COORDINATES, L_PLAYER_COORDINATES, SCORE_TO_WIN

# create the screen where the game will be played
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)
screen.listen()

# create and move paddle
right_paddle = Paddle(R_PLAYER_COORDINATES)
# move the player_1 paddle when up and down keys are pressed
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# create another paddle
left_paddle = Paddle(L_PLAYER_COORDINATES)
# move the player_2 paddle when w and s keys are pressed
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

#create ball and make it move
ball = Ball()
# create scoreboard
scoreboard = Scoreboard()

# game state flag
game_is_on = True
# x coordinate that would touch the surface of the right paddle
right_collision_start = right_paddle.xcor() - COLLISION_BUFFER
# x coordinate that would touch the surface of the left paddle
left_collision_start = left_paddle.xcor() + COLLISION_BUFFER


while game_is_on:
    time.sleep(0.05 * ball.difficuty_level)
    screen.update()
    ball.move()

# detect collision with wall and bounce
    ball_y = ball.ycor()
    if ball_y > SCREEN_HEIGHT/2 - COLLISION_BUFFER or ball_y < -SCREEN_HEIGHT/2 + COLLISION_BUFFER:
        ball.bounce_y()

# detect collision with paddle and bounce
    '''This collision will be detected by checking two conditions: 
        - if the ball has reached the xcor that would touch the paddle, and it's still within the bounds (player's xcor)
        - and if the paddle is within the distance represented by half of the paddle size.
    Cannot rely only in a fixed distance between ball and paddle, because this distance is measured considering the center of each object,
    and this distance may vary depending on where in the paddle the collision with the ball will happen.'''
    # right paddle
    if right_paddle.xcor() > ball.xcor() > right_collision_start and ball.distance(right_paddle) < PADDLE_STRETCH * 10:
        ball.bounce_x()
        # this prevents bug where ball will move along the length of the paddle
        ball.setposition(right_collision_start - 1, ball.ycor())

    # left paddle
    if left_paddle.xcor() < ball.xcor() < left_collision_start and ball.distance(left_paddle) < PADDLE_STRETCH * 10:
        ball.bounce_x()
        ball.setposition(left_collision_start + 1, ball.ycor())

    # could have used an 'or' to link both conditionals above, but decided to keep them separate for better code readability

# detect when paddle misses and the other player scores
    # right paddle
    if ball.xcor() > right_paddle.xcor() + COLLISION_BUFFER:
        scoreboard.left_point()
        if scoreboard.left_score == SCORE_TO_WIN:
            scoreboard.left_wins()
            game_is_on = False
        else:
            ball.restart_position()
    
    # left paddle
    if ball.xcor() < left_paddle.xcor() - COLLISION_BUFFER:
        scoreboard.right_point()
        if scoreboard.right_score == SCORE_TO_WIN:
            scoreboard.right_wins()
            game_is_on = False
        else:
            ball.restart_position()
    

screen.exitonclick()