# This program generates a silent auction
# The winner is whoever makes the HIGHEST UNIQUE bid

# RULES:
# Each person must enter their own name and bid.
# Cannot register a name that is in use by another person.
# Bid must be a valid number.
# If there are other bids to be entered, type 'yes' and hit enter when prompted to do so. Note: to avoid finishing the proccess of collecting bids by mistake, the program will only move on to the results step if someone types a 'no' in this check.
# Once all bids are in, the result will be calculated and displayed in the screen.

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
# import project modules
import auction_art as art

# function that collects all bids from the users and returns a dictionary with all bids
# having bidder name and bid amount as key and value pairs
def collect_bids():
  # bids dictionary
  bids = {}
  # variable to track 
  end_bidders = False

  while not end_bidders:
    #receive user_name input
    user_name = input("What is your name? ").lower()
    # check if there's another user with that name registered already
    if user_name in bids.keys():
      print("\n**There's already an user registered with this name!**\nLet's try again...\n")
      continue
    
    # receive user_bid input  
    user_bid = input("\nWhat's your bid? ")
    # try to convert to float when adding the bid to the bids dictionary
    try:
      bids[user_name] = float(user_bid)
    # if it fails (invalid input) restart the process of collecting data from this user 
    except ValueError:
      print("\n**Bid must be a number!**\nLet's try again...\n")
      continue

    # ask if there are other bidders pending to enter their data
    continue_bid = input("\nAre there any other bidders? Type 'yes' or 'no'.\n")
    #only if the command is a clear 'no', end this process of collecting data
    if continue_bid == 'no':
      end_bidders = True
    # clear console so the next bidder cannot see the previous bidder's inputs
    clear()
    # wait for an input to display result
    # added this so there's a gap between the last person's bid and the result display

  return bids

# function that receives a bid dictionary as argument and calcuate the results
def check_auction_result(bids):
  # find all non-unique bids
  from collections import Counter
  # create a counter from the bids dictionary values
  counts = Counter(bids.values())
  # create a new dictionary with only the keys whose value has a count greater than 1
  duplicates = {k: v for k, v in bids.items() if counts[v] > 1}

  #variables to track highest bid and current winner
  highest_unique_bid = 0
  winner_name = ''

  # loop through bids
  for bidder in bids:
    # get rid of duplicates
    if bidder in duplicates.keys():
      continue
    # if current bid is the highest so far, replace highest_bid and winner_name 
    if bids[bidder] > highest_unique_bid:
      highest_unique_bid = bids[bidder]
      winner_name = bidder.capitalize()

  # check if there's a valid winner
  if winner_name:
    return f"\n\nThe winner is {winner_name} with a bid of ${highest_unique_bid:.2f}"
  else:
    return "There were no unique bids."

# function that runs the silent auction program
def run_silent_auction():
  # splash screen
  print(art.logo)
  input('\nWelcome to the silent auction! Press ENTER to start')
  clear()
  # collect the users' bids
  bids = collect_bids()
  # pre-result screen
  print(art.logo)
  input("\nPress ENTER to check the result...")
  # print result
  print(check_auction_result(bids))

#execute program
run_silent_auction()