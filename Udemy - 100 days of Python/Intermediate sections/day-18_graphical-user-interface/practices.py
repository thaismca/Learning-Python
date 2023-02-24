# the following functions were implemented as part of the practices from day 18 of the course
# learning how to work with Turtle graphics

from turtle import Turtle, Screen
import random as ran


turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.shape('classic')
turtle.color('coral')

def random_color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    return (r, g, b)


def draw_shapes():
    '''Draws shapes of random colors, from triangle to decagon, increasing the number of sides by one at each iteration'''
    for sides in range(3, 10):
        turtle.pencolor(random_color())

        angle = 360/sides
        for _ in range(sides):
            turtle.right(angle)
            turtle.forward(100)

# draw_shapes()

def first_random_walk(steps):
    '''Draws a random walk with the given number of steps, each step with a random color'''
    directions = [
        'turtle.forward(20)',
        'turtle.backward(20)',
    ]
    turns =[
        'turtle.right(90)',
        'turtle.left(90)',
        'turtle.right(0)'
    ]

    turtle.pensize(10)

    for _ in range(steps):
        turtle.pencolor(random_color())
        direction = ran.choice(directions)
        turn = ran.choice(turns)
        eval(direction)
        eval(turn)

# first_random_walk(150)

def refactored_random_walk(steps, step_length = 30):
    '''Draws a random walk with the given number of steps, each step with the given length (default to 30) and a random color'''
    directions = [0, 90, 180, 270]

    turtle.pensize(10)

    for _ in range(steps):
        turtle.pencolor(random_color())
        turtle.forward(step_length)
        turtle.setheading(ran.choice(directions))

# refactored_random_walk(150, 40):


def draw_spirograph(radius, angle_increment):
    '''Receives the radius for the circles and the angle that spaces the circles out, and draws a spirograph'''
    turtle.speed('fastest')
    angle = 0
    while angle < 360:
        turtle.circle(radius)
        angle += angle_increment
        turtle.setheading(angle)
        turtle.pencolor(random_color())

draw_spirograph(100, 10)






screen.exitonclick()