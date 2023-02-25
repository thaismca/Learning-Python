# this code generates a hirst painting using the color palette extracted from the image provided

import colorgram

# extract color palette from image
image = 'Intermediate sections\\day-18_graphical-user-interface\hirst-painting\\image.jpg'
colors = colorgram.extract(image, 20)

# convert colorgram color objects to rgb tuples
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


from turtle import Turtle, Screen
import random as ran

# create instances of Turtle and Screen
turtle = Turtle()
screen = Screen()

# set screen colormode
screen.colormode(255)


def draw_row(columns, dot_size, step_size):
    '''Draws each one of the painting's rows with the given number of columns, dot size and space between dots'''
    # slow down the pen while drawing the dots
    turtle.speed('normal')
    # draw row of dots
    for _ in range(columns):
        turtle.dot(dot_size, ran.choice(rgb_colors))
        turtle.forward(step_size)
    # reset turtle position for next row
    turtle.speed('fastest')
    turtle.setheading(90)
    turtle.forward(step_size)
    turtle.setheading(180)
    turtle.forward(step_size * columns)
    turtle.setheading(0)


def draw_painting(rows, columns, dot_size, step_size):
    '''Draws a hirst painting with the given number of rows and columns, the dot size and space between dots'''
    turtle.penup()
    turtle.hideturtle()
    # set starting position
    left = - (step_size * columns) / 2
    down = - (step_size * rows) / 2
    turtle.setposition(left, down)

    # draw as many rows as passed in the arguments using the draw_row function
    for _ in range(rows):
        draw_row(columns, dot_size, step_size)
        

draw_painting(20, 10, 15, 30)






screen.exitonclick()