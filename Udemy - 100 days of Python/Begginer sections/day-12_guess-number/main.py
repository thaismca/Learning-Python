# The following code implements a "Guess the Number" game as part of the day 13 of the python course

# import logo from art
from art import game_logo
# import random module
import random

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# global game settings
MIN_NUMBER = 1
MAX_NUMBER = 100
DIFFICULTY_LEVELS = {
    'easy': 10,
    'medium': 8,
    'hard': 5
}

def set_difficulty_level():
    '''Prompts player to select a difficulty level from options available in game settings and return the numbr of attempts
    that player has at that level'''
    # get options available from global game settings
    difficulty_options = [option for option in DIFFICULTY_LEVELS.keys()]
    # ask player to choose difficulty level
    difficulty_selected = input(f"\nChoose a difficulty. Type {' or '.join(difficulty_options)}: ").lower()
    # validate selection 
    while difficulty_selected not in difficulty_options:
        difficulty_selected = input("Invalid option, try again: ")
    # set number of attempts based on difficult selection
    attempts = DIFFICULTY_LEVELS[difficulty_selected]

    return attempts

def verify_guess(guess, answer):
    '''Takes a guess and the correct answer and returns the result'''
    if guess == answer:
        return "\nTHAT'S CORRECT! YOU WIN!!!"
    elif guess > answer:
        return "Too high."
    else:
        return "Too low."

def start_game():
    # game start
    clear()
    correct_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    player_guess = 0
    print(game_logo)
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

    # difficulty selection
    player_attempts = set_difficulty_level()

    # player still have attempts left and haven't guessed correctly
    while player_attempts > 0 and player_guess != correct_number:
        # show atempts left and take player's guess
        print(f"\nYou have {player_attempts} attempts remaining to guess the number.")
        player_guess = input("Make a guess: ")
        # validate guess
        try:
            player_guess = int(player_guess)
            # print result for this round
            print(verify_guess(player_guess, correct_number))    
        except:
            print("This is not a valid number and you wasted this attempt.")
        
        #update attempts left
        player_attempts -= 1

        # check if player still has attempts remaining
        if player_attempts == 0:
            print("\nYou've run out of guesses. You lose.")
    
    # check if player wants to exit or start another game
    if input("\nDo you want to start another game? Type 'y' or 'n': ") == 'y':
        start_game()
    else:
        exit()

# start game
start_game()













