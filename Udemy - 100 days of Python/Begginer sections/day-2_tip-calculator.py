# a program that receives a bill total, the tip percantage and the number of people to split the bill
# and outputs the amount that each person should pay

# note: this code assumes that the answers typed by the user will always be valid numbers
# the goal is just to work a bit with python syntax

#getting user's input
print("Welcome to the Tip Calculator!")
bill_total_str = input("What was the total bill? $")
tip_percentage_str = input("What percentage tip would you like to give? ")
party_size_str = input("How many people to split the bill? ")

#inputs conversion
bill_total = float(bill_total_str)
tip_percentage = float(tip_percentage_str)
party_size = int(party_size_str)

# note: can convert the input in the same line it's received -> i.e. bill_total_str = float(input("What was the total bill? $"))

#calculations
bill_plus_tip = bill_total + bill_total * (tip_percentage / 100)
total_per_person = (bill_plus_tip / party_size)

print(f"Each person should pay ${total_per_person:.2f}")