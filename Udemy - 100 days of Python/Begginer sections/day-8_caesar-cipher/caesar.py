# getting familiar with python syntax to define and call functions with parameters

# module that contains function to encode/decode messages
# and a function to generate the caesar cipher running program

# alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function to encrypt/decode a text
def caesar_cipher(text, shift, direction):
  # a variable to track errors
  errors = False
  # check if direction is valid
  if direction != 'encode' and direction != 'decode':
    print('\n\t-> Invalid direction')
    errors = True
  # check if text is valid
  if len(text) <= 0:
    print('\n\t-> Message cannot be empty')
    errors = True
    # check if shift is valid
  try:
    # make shift an int that is the remainder of the division of itself by the number of letters in alphabet list
    # covers the cases where the shift from user input is greater than the alphabet length -> it starts to count from the start of the list again
    shift = int(shift) % len(alphabet)
  except ValueError:
    print('\n\t-> Shift must be a integer')
    errors = True
  #if one or more errors were encountered, return
  if errors:
    return '\nCANNOT PROCEED WITH THE GIVEN INPUTS'

  # no errors
  else:
    # a variable for the encrypted/decoded text
    text_result = ''
    # loop through the characters in the string that was passed as argument
    for char in text:
      # if the character is not in the alphabet list
      if not char in alphabet:
        # add the character itself to the encoded/decoded message
        text_result += char
      # character is in the alphabet list
      else:
        # get the index of the corresponding character in the alphabet list
        result_index = alphabet.index(char)
        
        # if direction is encode
        if direction == 'encode':
          # add shift to the character's index
          result_index += shift
          # if the resulting index is greater than the alphabet list length
          if result_index >= len(alphabet):
            # that difference will represent the correct result_index instead
            result_index -= len(alphabet)
            
        # if direction is decode
        elif direction == 'decode':
          # deduct shift from the character's index
          # since you can represent an index using a negative number to go backwards in a list, no need to have a check to correct the enc_index < 0
          result_index = alphabet.index(char) - shift
        
          # add the letter from the alphabet list at the result_index to the encrypted message
        text_result += alphabet[result_index]
        
    return f'Your {direction}d message:\n{text_result}'
  
# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
# a function to generate running caesar cipher program
def run_caesar_cipher():
  # getting user inputs
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\nType your message:\n").lower()
  shift = input("\nType the shift number:\n")
  print(caesar_cipher(text, shift, direction))
  input('\n\nPress ENTER to go again...')
  clear()
  run_caesar_cipher()