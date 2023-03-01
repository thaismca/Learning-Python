from turtle import Turtle
import random

class Food(Turtle):
    """Models the food in the Snake Game. It inherities from the Turtle class"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        # reduce the default circle size (20x20) by half (10x10)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        # go to a random location inside the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.speed("fastest")
        self.goto(random_x, random_y)

