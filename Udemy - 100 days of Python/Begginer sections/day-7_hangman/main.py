# this code generates a hangman game
# practicing all concepts that were resented in this course at this point
# added my own challenge and put the code that generates a game loop in a function, so player can restart a new one when game is over

import random
import hangman_art as art
from hangman_words import word_list

# to clear console
# this required some research, because solution presented in the course wouldn't work outside of replit
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#game loop
def start_game():
  # clear console from either splash screen or previous game
  clear()
  # randomly choose a word from the word_list
  chosen_word = random.choice(word_list)
  # get a reference to the word's length
  word_length = len(chosen_word)
  # generate blanks -> must match numbers of letters in chosen_word
  blanks = []
  for _ in range(word_length): # reminder: when range starts at 0, can be ommited
      blanks.append('_')

  # variable that indicates game state -> set to false on start
  game_over = False
  # variable that tracks number of player's lives -> set to max on start
  lives = len(art.lives_images) - 1
  # list to track player's guess attempts
  guess_attempts =[]

  while not game_over:
    # print the current state of lives -> image that represents it
    print(art.lives_images[lives])
    # print the blanks for the chosen_word
    print('\n' + ' '.join(blanks) + '\n')
    # prompt player to guess a letter and make it lower case
    guess = input('Guess a letter: ').lower()
    # clear console after guess
    clear()
    
    # check if player tried that letter before (guess_attempts)
    if guess in guess_attempts:
      print(f'\nYou already guessed letter {guess}')
      
    # letter was not tried before  
    else: 
      # add guess to the guess_attempts tracker
      guess_attempts.append(guess)
      
      # check if the guess exists in chosen_word
      if guess in chosen_word: # if it is, update the blanks
        # loop through each position in chosen_word
        for position in range(word_length):
          # check if guess matches the letter at the current position in chosen_word
          if guess == chosen_word[position]:
            # if yes, replace '_' in blanks with that letter
            blanks[position] = chosen_word[position]
        # inform player that the letter is not in the word
        print(f'\nLetter {guess} is in the word.')
        
        # check if the blanks are all filled out now -> blanks has no '_'
        if not '_' in blanks:
          game_over = True
          print('\n' + ' '.join(blanks) + '\n')
          input('\n:::: YOU WIN! :::::\n\nPress ENTER to start a new game ')
          start_game()
          
      # guess does not exist in chosen_word
      else:
        # take one life from player
        lives -= 1
        # inform player that the letter is not in the word
        print(f'\nLetter {guess} is not in the word.')
        
        # check if there are no lives remaining -> game over
        if lives == 0:
          game_over = True
          print(art.lives_images[lives])
          print('\n' + ' '.join(blanks) + '\n')
          input('\n:::: YOU LOSE :::::\n\nPress any ENTER to start a new game ')
          start_game()

# splash screen
print(art.logo)
input('\n\nPress ENTER to start ')
start_game()