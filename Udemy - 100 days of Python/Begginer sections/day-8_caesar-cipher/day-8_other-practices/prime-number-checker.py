# code written as part of the day 8 of the course -> function parameters
# getting familiar with python syntax to define and call functions with paramenters

#import math module
import math

def prime_checker(number):
    #start prime checker as true, as it can be flipped to false in the checks
    is_prime = True
    
    number_sqrt = math.sqrt(number)
    # if a number has a integer square root, it's not prime
    if isinstance(number_sqrt, int):
        is_prime = False
    # if a number is divisible by 2, except number 2 itself, it's not prime
    elif number % 2 == 0 and number != 2:
        is_prime = False
    # if a number is divisible by 5, except number 5 itself, it's not prime
    elif number % 5 == 0 and number != 5:
        is_prime = False
    # for all other numbers that weren't catch in any of the if statements above
    else:
        # try to divide the number by each integer from 2 up to the square root of the number
        for n in range(2, math.ceil(number_sqrt)):
            if number % n == 0:
                # if the number can be evenly divided by any number in that range, it's not prime
                is_prime = False

    if is_prime:
        # this happens if none of the checks flips the is_prime checker
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# getting user input and calling the prime_checker function passing the user input as argument
n = int(input("Check this number: "))
prime_checker(number=n)