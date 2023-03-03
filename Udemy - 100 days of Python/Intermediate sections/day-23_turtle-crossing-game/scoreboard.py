from turtle import Turtle
from settings import FONT, LEVEL_TEXT_POSTION

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # keep track of the level
        self.level = 1
        # turtle settings
        self.penup()
        self.hideturtle()
        # level text rendering
        self.goto(LEVEL_TEXT_POSTION)
        self.write(f"Level: {self.level}", align="left", font=FONT)

