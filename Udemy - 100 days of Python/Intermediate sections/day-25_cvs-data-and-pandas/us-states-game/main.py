import turtle
import pandas

# path for the csv file
DATA_FILE_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/us-states-game/50_states.csv"
PROJECT_DIRECTORY_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/us-states-game/"

# function that will print state name in map
def print_name(state, x, y):
    """prints the state name on the screen, at the provided x and y coordinate"""
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.goto(x,y)
    name.write(state, align="center", font=("Courier", 8, "normal"))

# create screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# add image as background
bg_image = "./Intermediate sections/day-25_cvs-data-and-pandas/us-states-game/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# TODO: read states from 50_states.csv and generate a list with all the 50 states
data = pandas.read_csv(DATA_FILE_PATH)
states = data.state.to_list()
# TODO: while there are still states to be guessed, display a pop up input to receive a player's answer
score = 0
while len(states) > 0:
    # TODO: display current score in the title of the pop up input
    # need to capitalize the first letter in each word, to match dataframe format
    try: 
        answer = screen.textinput(title=f"Current score: {score}/50", prompt="What's another state's name?").title()
    except:
        # if player clicks cancel -> dialog returns None
        break

    # TODO: check if player's answer matches one of the states in the 50_states.csv
    if answer in states:
        # TODO: update the list of states pending to be guessed, so the player cannot score twice with the same state
        states.remove(answer)
        # TODO: update player score
        score += 1

        # TODO: if there's a match, display state name in the map at the corresponding x,y coordinates provided in the 50_states.csv
        x_pos = int(data[data.state == answer].x)
        y_pos = int(data[data.state == answer].y)
        print_name(answer, x_pos, y_pos)

# TODO: if all states were guessed, end game with a congrats message
if len(states) == 0:
    success_message = turtle.Turtle()
    success_message.hideturtle()
    success_message.penup()
    success_message.color("green")
    success_message.goto(0,250)
    success_message.write("Congrats! You got all U.S. States right!", align="center", font=("Courier", 20, "bold"))
    screen.exitonclick()
else:
    # this can be the scenario where player clicks cancel in the pop up without completing all the states
    # save the remaining states to a .csv file -> learn tool
    learn_states_dict = {
        "missing states": states
    }
    learn_states_dataframe = pandas.DataFrame(learn_states_dict)
    # create csv from dataframe
    learn_states_dataframe.to_csv(PROJECT_DIRECTORY_PATH + "learn_states.csv")
