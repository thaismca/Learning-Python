
# US STATES GAME

This project implements a game that challenges player to type correctly the name of all US states. For each correct guess, the name of the state is displyed on the map, at its proper location.

This game was implemented as part of the day 26 of the course *100 days of Python*. All implementation was taken care of prior to watch the solution videos.

## Key differences from course solution

- Solution presented in the course does not account for the scenario where player types the same state name more than once. It keeps adding up the same state to the score.
- Solution presented in the course does not display a congrats message if player guesses all states correctly.
- Solution presented in the course does not account for the scenario where the player clicks "cancel" or submits an empty string in the input.

## How this app works

1. Player is presented with a map of the U.S. without the name of the states, and is prompted to type the name of a state in a pop up.

2. If the player types a name that is correct and i wasn't typed before, this correct answer is added to the player's score, and the name of the state is displayed on the map.

3. The pop up will continue to be displayed until the player guesses all the states correctly, or click cancel to exit the game.

4. The current player score is displayed at the title of the pop up.

5. If player clicks "cancel" in the popup, or tries to submit an empty string, the game exists, and a list with all states that were pending to be guessed are exported to a .csv file

6. If player manage to type the names of all 50 states, the game ends with a congrats message.
## Implementation notes

Problem was broken down into the following TODOs:

- create screen with a map of the US in the background
- read states from 50_states.csv and generate a list with all the 50 states
- while there are still states to be guessed, display a pop up input to receive a player's answer
- display current score in the title of the pop up input
- check if player's answer matches one of the states in the 50_states.csv
- if there's a match, display state name in the map at the corresponding x,y coordinates provided in the 50_states.csv
- update the list of states pending to be guessed, so the player cannot score twice with the same state
- update player score
- if all states were guessed, end game with a congrats message
- if player cancels or submits an empty string, export missing states to .csv file as learning tool and exit game


Notes:
- the aswer provided by the player will be title cased prior to the comparison with the list of the states.
- Both read from and write to .csv were done using pandas library.
