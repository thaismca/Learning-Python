# The code in the maze-solution.py file was written in order to solve the Maze challenge in Reeborg's World.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# In order to test it:
# - go to the Reeborg's World website at the Maze challenge (link above)
# - click to open this file
# - run the code

# Some custom test words that test specific corner cases are available in the test_worlds folder
# They can be loaded by clicking 'Additional options' -> 'Open world from file'

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# to make sure the robot encounters a wall for reference
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()