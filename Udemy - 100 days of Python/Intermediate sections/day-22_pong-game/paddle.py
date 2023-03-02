from turtle import Turtle
from settings import PADDLE_PACE, PADDLE_STRETCH

class Paddle(Turtle):
    def __init__(self, coordinates):
        """It receives a pair or coordinates to create and render a paddle in the screen"""
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_STRETCH, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def go_up(self):
        """Moves the paddle up"""
        # increment current y coordinate
        new_y = self.ycor() + PADDLE_PACE
        # move paddle in the y axis
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down"""
        # decrement from current y coordinate
        new_y = self.ycor() - PADDLE_PACE
        # move paddle in the y axis
        self.goto(self.xcor(), new_y)