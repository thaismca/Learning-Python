# this code implements a turtle race game
# player is prompted to place a bet in one of the turtles
# if the chosen turtle gets first to the other side of the screen, player wins

from turtle import Turtle, Screen
import random as r

s = Screen()
s.setup(width = 500, height = 400)

# game state flag
is_race_on = False

# input that takes player's bet
bet = s.textinput(title='Make a bet', prompt='Which turtle will win the race? Enter a color: ').lower()

# create the turtles and set them to the starting line
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
race_turtles = []
for turtle_index in range(6):
    t = Turtle(shape='turtle')
    t.color (colors[turtle_index])
    t.penup()
    t.goto(x = -230, y = -70 + (turtle_index * 30))
    race_turtles.append(t)

# start the game when player inputs the bet
if bet:
    is_race_on = True

while is_race_on:
    for turtle in race_turtles:
        # end race if one of the turtle reaches the other side of the screen
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            continue
        
        # move turtle forward at random pace
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)

# print result in terminal
print(f'The {winner} turtle finished first.')
if winner == bet:
    print('You win!')
else:
    print('You lose.')


s.exitonclick()

