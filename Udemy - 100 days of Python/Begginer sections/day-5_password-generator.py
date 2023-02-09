# Password Generator Project
# getting familiar with for loops in python syntax

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ''
# if starting range at 1, remember to +1 to user input
for nr_letter in range(1, nr_letters + 1):
  # not using choice()
  index = random.randint(1, len(letters) - 1)
  letter = letters[index]
  easy_password += letter
# if starting range at 0, no need to add 1 to user input
for nr_symbol in range(0, nr_symbols):
  # using choice 
  symbol = random.choice(symbols)
  easy_password += symbol
for nr_number in range(1, nr_numbers + 1):
  # using one-line
  easy_password += random.choice(numbers)
  
print(f"Easy Level password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = list(easy_password)
random.shuffle(hard_password)
print(f"Hard Level password: {''.join(hard_password)}")
