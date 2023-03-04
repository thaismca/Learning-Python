from turtle import Turtle
import random
from settings import CAR_COLORS, CAR_START_MOVE_PACE, CAR_MOVE_INCREMENT, SPAWN_RANGE_MIN, SPAWN_RANGE_MAX, SCREEN_WIDTH

class CarManager():
    def __init__(self):
        # list of existing cars
        self.all_cars = []
        # keeps track of pace
        self.pace = CAR_START_MOVE_PACE


    def render_car(self):
        """Renders a new car and adds it to the list of existing cars that are managed by this CarManager"""
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        # add the ability to randomize car color
        new_car.color(random.choice(CAR_COLORS))
        # add the ability to randomize the car spawn point in the y axis, excluding a safe zone at both bottom and top areas of the screen
        new_car.goto(SCREEN_WIDTH/2 , random.randint(SPAWN_RANGE_MIN, SPAWN_RANGE_MAX))
        self.all_cars.append(new_car)


    def move(self):
        """Moves each car in the cars list forward at the current pace"""
        for car in self.all_cars:
            car.forward(self.pace)

    def increase_pace(self):
        """Increases the current pace by the amount of the CAR_MOVE_INCREMENT in settings"""
        self.pace += CAR_MOVE_INCREMENT

    def reset_all_cars(self):
        """Clears all the existing cars in the all_cars list"""
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []

