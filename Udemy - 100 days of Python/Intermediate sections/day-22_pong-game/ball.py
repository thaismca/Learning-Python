from turtle import Turtle
from settings import BALL_PACE

class Ball(Turtle):
    def __init__(self):
        """Creates and renders a ball in the screen"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        self.x_move = BALL_PACE
        self.y_move = BALL_PACE
        self.difficuty_level = 1

    def move(self):
        """Moves ball along the x and y axis"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Makes ball move in the opposite y direction"""
        # if current y_move is positive, it turns to negative, and vice-versa
        self.y_move *= -1

    def bounce_x(self):
        """Makes ball move in the opposite x direction"""
        # if current x_move is positive, it turns to negative, and vice-versa
        self.x_move *= -1
        # increase ball speed each time it bounces in the x axis (it means collision with paddle)
        self.difficuty_level *= 0.9


    def restart_position(self):
        """Reset ball position to the center of the screen, and moves it towards the player that just scored"""
        self.home()
        self.bounce_x()