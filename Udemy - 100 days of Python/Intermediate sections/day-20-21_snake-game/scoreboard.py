from turtle import Turtle
from settings import SCREEN_HEIGHT, DATA_FILE_PATH

# Scoreboard settings
TEXT_ALIGN = "center"
FONT_SIZE = 15
FONT = ("Courier", FONT_SIZE, "bold")

class Scoreboard(Turtle):
    """Models the scoreboard in the Snake Game. It inherities from the Turtle class"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        # keeps track of the score -> starts at 0
        self.score = 0
        # keeps track of the high score -> retrieves score from data file
        with open(DATA_FILE_PATH) as data:
            self.high_score = int(data.read())
        # sets the location of the text in the screen
        self.goto(0, (SCREEN_HEIGHT / 2) - FONT_SIZE * 2)
        self.render_score()
    
    def render_score(self):
        """Renders score text on the screen"""
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align=TEXT_ALIGN, font=FONT)

    def increase_score(self):
        """Increases score by one and updates the rendered text"""
        self.score += 1
        self.render_score()

    def reset_score(self):
        """Replaces high score if it was beaten, and resets score for a new game. High score gets written to data file."""
        if self.score > self.high_score:
            self.high_score = self.score
        with open(DATA_FILE_PATH, mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.render_score()
        
