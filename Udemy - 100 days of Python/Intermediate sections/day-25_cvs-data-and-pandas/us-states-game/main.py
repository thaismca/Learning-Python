import turtle
import pandas

# path for the csv file
DATA_FILE_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/us-states-game/50_states.csv"

# create screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# add image as background
bg_image = "./Intermediate sections/day-25_cvs-data-and-pandas/us-states-game/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

#create pop-up input to get player's answer
# answer = screen.textinput(title="Guess the state", prompt="What's another state's name?")

# TODO: read states from 50_states.csv and generate a list with all the 50 states
data = pandas.read_csv(DATA_FILE_PATH)
states = data.state
# TODO: while there are still states to be guessed, display a pop up input to receive a player's answer
# TODO: display current score in the title of the pop up input
# TODO: check if player's answer matches one of the states in the 50_states.csv
# TODO: if there's a match, display state name in the map at the corresponding x,y coordinates provided in the 50_states.csv
# TODO: update the list of states pending to be guessed, so the player cannot score twice with the same state
# TODO: update player score
# TODO: if all states were guessed, end game with a congrats message

screen.exitonclick()