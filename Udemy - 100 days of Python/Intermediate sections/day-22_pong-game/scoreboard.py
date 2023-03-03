
from turtle import Turtle
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

# Scoreboard settings
TEXT_ALIGN = "center"
FONT_SIZE = 60
FONT = ("Courier", FONT_SIZE, "bold")

class Scoreboard(Turtle):
    """Models the scoreboard in the Pong Game. It inherities from the Turtle class"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        # keep track of the scores -> start at 0
        self.right_score = 0
        self.left_score = 0
        self.render_score()
    
    def render_score(self):
        """Renders score text on the screen"""
        self.goto((SCREEN_WIDTH / 8), (SCREEN_HEIGHT / 2) - FONT_SIZE * 1.5)
        self.write(f"{self.right_score}", align=TEXT_ALIGN, font=FONT)

        self.goto((-SCREEN_WIDTH / 8), (SCREEN_HEIGHT / 2) - FONT_SIZE * 1.5)
        self.write(f"{self.left_score}", align=TEXT_ALIGN, font=FONT)

    def right_point(self):
        """Increases right score by one and updates the rendered text"""
        self.right_score += 1
        self.clear()
        self.render_score()

    def left_point(self):
        """Increases left score by one and updates the rendered text"""
        self.left_score += 1
        self.clear()
        self.render_score()