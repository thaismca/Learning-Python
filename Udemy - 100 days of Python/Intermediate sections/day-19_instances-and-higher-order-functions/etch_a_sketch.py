# this code implements a Etch-A-Sketch app
# learning about event listeners in turtle

from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_counter_clockwise():
    t.left(10)

def turn_clockwise():
    t.right(10)

def restart():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# binding functions to keypress events
s.onkeypress(key = 'w', fun = move_forward)
s.onkeypress(key = 's', fun = move_backward)
s.onkeypress(key = 'a', fun = turn_counter_clockwise)
s.onkeypress(key = 'd', fun = turn_clockwise)
s.onkey(key = 'space', fun = restart)

# setting focus on the turtle screen, in order to listen for events
s.listen()


s.exitonclick()