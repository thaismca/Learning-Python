from turtle import Turtle
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, SHAPE_STRETCH
import random

class Food(Turtle):
    """Models the food in the Snake Game. It inherities from the Turtle class"""

    def __init__(self, ):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        # reduce the default circle size (20x20) by half (10x10)
        self.shapesize(stretch_len=SHAPE_STRETCH, stretch_wid=SHAPE_STRETCH)
        # go to a random location inside the screen
        self.refresh_position()

    def refresh_position(self):
        '''Sets new random x and y cordinates and moves the food to that position'''
        available_x = (SCREEN_WIDTH / 2) - 20
        available_y = (SCREEN_HEIGHT / 2) - 20
        random_x = random.randint(-available_x, available_x)
        random_y = random.randint(-available_y, available_y)
        self.goto(random_x, random_y)
