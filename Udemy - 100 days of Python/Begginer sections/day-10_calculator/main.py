# calculator project
# code written as part of the day 10 of the course -> functions with outputs
# getting familiar with python syntax

import operations as op
from art import logo

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def calculator(): 
  '''Runs calculator program'''
  # reset continue flag and clear screen
  continue_calc = True
  clear()
  # print art
  print(logo)

  #get user's inputs
  num1 = input("What's the first number?\n")
  while continue_calc:
    symbol = input(f"\nWhat operation do you want to perform?\nType one of the following: {', '.join(op.operations)}\n")
    num2 = input("\nWhat's the next number?\n")

    # validate inputs
    try:
      # convert inputs to float
      num1 = float(num1)
      num2 = float(num2)
      # retrieve operation funtion based on symbol passed in the input
      operation = op.operations[symbol]
    except:
      input('Cannot calculate with the inputs provided. Press ENTER to restart.')
      continue_calc: False
      calculator() 

    # calculate and print result
    result = operation(num1, num2)
    print (f"\n{num1} {symbol} {num2} = {result}")
    #check if user wants to continue calculating
    if input(f"Type 'y' to continue calculating with {result}: ") == 'y':
      # set the first number of next operation to be the result from this previous one
      num1 = result
    else:
      # change flag to end loop and restart program
      continue_calc = False
      calculator()

# run program
calculator()