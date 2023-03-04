from turtle import Turtle
from settings import LEVEL_TEXT_FONT, LEVEL_TEXT_POSTION, GAME_OVER_TEXT_FONT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # keep track of the level
        self.level = 1
        # turtle settings
        self.penup()
        self.hideturtle()
        # level text rendering
        self.render_level()

    def render_level(self):
        self.goto(LEVEL_TEXT_POSTION)
        self.write(f"Level: {self.level}", align="left", font=LEVEL_TEXT_FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.render_level()

    def render_game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=GAME_OVER_TEXT_FONT)

