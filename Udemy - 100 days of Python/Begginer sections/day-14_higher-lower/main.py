# This code implements a Higher-Lower Game

from game_data import data
import art
import random

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# function to compare followers count
def has_more_followers(a, b):
    '''Receives two items from the game_data list and returns the letter that represents the option that has more followers. If they have the same amount, returns 0'''
    if a['follower_count'] > b['follower_count']:
        return 'a'
    elif b['follower_count'] > a['follower_count']:
        return 'b'
    else:
        return 0

# function that checks if player guessed correctly
def is_player_correct(player_guess, correct_answer):
    '''Receives the player guess and the correct answer. Returns True if player is correct and False if not.'''
    # player will be correct if the correct answer is chosen, which can be either one when both options have the same amount of followers
    if player_guess == correct_answer or correct_answer == 0:
        return True
    else:
        return False

# function tha runs the game
def start_game():
    # generate randomized list from game_data, without changing the original list
    randomized_list = random.sample(data, len(data))
    # keep track of round
    game_round = 0
    # keep track of score
    game_score = 0
    # get first option A
    option_a = randomized_list[game_round]

    # game over flag
    is_game_over = False

    while not is_game_over and game_round < len(randomized_list) -1:
        # get option B
        option_b = randomized_list[game_round + 1]
        # get a reference to correct answer
        answer = has_more_followers(option_a, option_b)

        #round screen
        clear()
        print(f"Round: {game_round + 1} / {len(randomized_list)}")
        print(art.game_logo)
        print(f"Score: {game_score}")
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(art.vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
        # get player's input
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        #validate player's input
        while guess != 'a' and guess != 'b':
            print(f"\nInvalid option, try again.")
            guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        # check player's answer
        if not is_player_correct(guess, answer):
            print("\nYou got it wrong.")
            is_game_over = True
        else:
            # increment round and score
            game_round += 1
            game_score += 1
            # make option_a become option_b
            option_a = option_b
    
    # if all items in the list were already displayed in the game 
    if game_round >= len(randomized_list) -1:
        # ultimate victory screen
        clear()
        print(art.game_logo)
        print(f"Score: {game_score}")
        print("\nCONGRATS!!! You guessed all correctly!")

    # check if user wants to start new game
    if input("\nGame Over! Type 'y' to star a new game or 'n' to exit: ") == 'y':
        start_game()
    else:
        exit()

# splash screen
print(art.game_logo)
print("""WELCOME TO THE HIGHER-LOWER GAME!
Let's see if you can guess who out of two accounts has more Instagram followers.

You are going to be prompted with two options at each round.
If you guess it right, you score one point and move on to the next round.
If you guess it wrong, it's game over.
Will you be able to reach the end of our list in one play?""")
input("\nPress ENTER to start... ")
start_game()