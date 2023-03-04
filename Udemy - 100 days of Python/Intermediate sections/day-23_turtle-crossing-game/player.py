from turtle import Turtle
from settings import PLAYER_MOVE_PACE, PLAYER_START_POSITION


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(PLAYER_START_POSITION)

    def move_up(self):
        """Moves turtle in the north direction at a given pace"""
        self.forward(PLAYER_MOVE_PACE)

    def restart_position(self):
        """Resets player position to the starting point"""
        self.goto(PLAYER_START_POSITION)