# this code generates a "rock paper scissors" game
# getting familiar with randomisation and lists in python syntax
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# generate options list
options = [rock, paper, scissors]

# calculate computer choice
random_index = random.randint(0, 2)
computer_choice = options[random_index]

# player prompt to make a choice
input_index = input(
    "What do you choose?\nType 1 for ROCK\nType 2 for PAPER\nType 3 for SCISSORS\n"
)
# check if player input is a valid option
if input_index != "1" and input_index != "2" and input_index != "3":
    # not valid - game over
    print("\nInvalid option. Game Over.")
else:
    #valid - set player choice from list of options
    player_choice = options[int(input_index) - 1]

    #calculate result
    result = ''
    #possibilities when player chooses rock
    if player_choice == rock:
        if computer_choice == rock:
            result = "It's a draw"
        elif computer_choice == paper:
            result = "You lose"
        else:
            result = "You win!"
    #possibilities when player chooses paper
    if player_choice == paper:
        if computer_choice == rock:
            result = "You win!"
        elif computer_choice == paper:
            result = "It's a draw"
        else:
            result = "You lose"
    #possibilities when player chooses scissors
    if player_choice == scissors:
        if computer_choice == rock:
            result = "You lose"
        elif computer_choice == paper:
            result = "You win!"
        else:
            result = "It's a draw"

    # print results
    # player choice
    print(f"{player_choice}")
    # computer choice
    print(f"Computer chose:\n{computer_choice}\n")
    # final result
    print(f"{result}")