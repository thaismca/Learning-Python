# TODO: create the screen where the game will be played
from turtle import Screen, Turtle

# Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_PACE = 20

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)

# TODO: create and move paddle
paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(SCREEN_WIDTH/2 - 50,0)

def go_up():
    """Moves the paddle up"""
    # increment current y cordinate
    new_y = paddle.ycor() + PADDLE_PACE
    # move paddle in the y axis
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    """Moves the paddle down"""
    # decrement from current y cordinate
    new_y = paddle.ycor() - PADDLE_PACE
    # move paddle in the y axis
    paddle.goto(paddle.xcor(), new_y)

# move the paddle when up and down keys are pressed
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")


# game state flag
game_is_on = True
while game_is_on():
    screen.update()


screen.exitonclick()



# TODO: create another paddle

# TODO: create ball and make it move

# TODO: detect collision with wall and bounce

# TODO: detect collision with paddle and bounce

# TODO: detect when paddle misses and the other player scores

# TODO: keep and display score