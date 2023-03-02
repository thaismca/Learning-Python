from turtle import Turtle
from settings import BALL_PACE

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")

    def move(self):
        new_x = self.xcor() + BALL_PACE
        new_y = self.ycor() + BALL_PACE
        self.goto(new_x, new_y)