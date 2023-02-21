from machine_config import resources, menu

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# print resources report
def print_resources_report():
    '''It prints the current amount of each resource in the machine'''
    print("Coffee Machine resources:")
    # iterate through the resources dictionary
    for k, v in resources.items():
        # print the resource and the qauntity available
        print(f"-> {k.capitalize()}: {v['quantity']:,} {v['unit']}")

# check for low resources
def check_low_resources():
    '''It checks there are resources below the minimum amount and prints them'''
    # get a copy of all resources that are below min
    low = {k: v for k, v in resources.items() if v['quantity'] < v['min']}
    # if there are items in low
    if low.keys():
        print("ALERT!!! Low resources:")
        # for each item in low, print the item and the quantity
        for k, v in low.items():
            print(f"-> {k}: {v['quantity']} {v['unit']}")        
        print("\n")

# check sufficient resources for drink
def is_sufficient_resources(drink):
    '''It receives a drink and checks if there are sufficient resources to make that drink. Returns True if the resources are enough, False if they are not.'''
    # for each ingredient used by the drink
    for ingredient, quantity in menu[drink]['ingredients'].items():
        # if the quantity needed is less than the amount of that ingredient in resources, return False
        if resources[ingredient]['quantity'] < quantity:
            return False
    # if it never returns False, it means we have the sufficient amount of all the ingredients to make that drink return True
    return True

# show menu
def show_available_menu():
    '''Returns a list containing only the drinks available based on the amount of the ingredients in resources and prints the menu with this list.'''
    available = []
    print("::: COFFEE MACHINE MENU :::")

    # for each rink in the menu dictionary
    for drink in menu.keys():
        # if there are sufficient resources to make the drink
        if is_sufficient_resources(drink):
            # add drink to the list of available drinks
            available.append(drink)
            # print the name of the drink in the screen
            print(f"-> {drink}")

    return(available)

# validate coins quantity
def validate_coins(qtd):
    '''Receives a quantity and returns taht quantity converted to int. If the quantity passed is not convertible to int, returns 0.'''
    try:
        qtd = int(qtd)
    except:
        qtd = 0
    return qtd

# receive money
def receive_money():
    '''Prints the inputs to receive the quantity for each coin from user, and return the total amount of money from those coins.'''
    money_received = 0
    
    # get user input
    quarters = input("How many quarters? ")
    # convert input to int or 0
    quarters = validate_coins(quarters)
    # add quantity * value to money_received
    money_received += quarters * 0.25

    dimes = input("How many dimes? ")
    dimes = validate_coins(dimes)
    money_received += dimes * 0.10

    nickles = input("How many nickles? ")
    nickles = validate_coins(nickles)
    money_received += nickles * 0.05

    pennies = input("How many pennies? ")
    pennies = validate_coins(pennies)
    money_received += pennies * 0.01
        
    return money_received   

# make drink
def make_drink(drink_name, ingredients):
    '''Receives a drink name and the ingredients to make that drink. Deducts the ingredients from resources and prints the confirmation for the drink making.'''
    # for each ingredient in the ingredients received in parameters
    for ingredient in ingredients:
        #deduct the quantity used to make the drink from the resources
        resources[ingredient]['quantity'] -= ingredients[ingredient]
    
    # print drink making confirmation
    print(f"\n:: Here is your {drink_name} :: ☕ :: Enjoy! ::")

# coffee machine start
is_on = True
profit = 0
while is_on:
    # clear console at every new action
    clear()
    # display alert for low resources, if any
    check_low_resources()
    # show the menu with available items
    available_menu = show_available_menu()
    # if there are no available items
    if len(available_menu) < 1:
        # display message and wait for the user to hit enter to turn the machine off
        print("Not enough resources in this machine.")
        input("\nPress ENTER to turn the machine off and restock resources.")
        is_on = False
        continue
    # at least one item available
    else:
        # ask for user input
        choice = input("\nWhat would you like? ").lower()

        # admin possible choice -> prints report
        if choice == 'report':
            print_resources_report()
            print(f"\nMoney: ${profit:.2f}")
            input("\nPress ENTER to go back to main menu.")
            continue

        # admin possible choice -> turns machine off
        elif choice == 'off':
            is_on = False
            continue

        # choice is in available menu
        elif choice in available_menu:
            drink = menu[choice]
            # print cost
            print(f"\nThis drink costs ${drink['cost']:.2f}\n")
            # receive money and print amount received
            money_received = receive_money()
            print(f"\nAmount received: ${money_received:.2f}")
            
            is_cancelled = False
            # repeat while money received is not enough to pay for drink, and order is not cancelled
            while money_received < drink['cost'] and not is_cancelled:
                # print amount due
                print(f"Amount due: ${drink['cost'] - money_received:.2f}\n")
                # check if user wants to add more coins or cancel order
                add_more = input("Want to add more coins? Type 'y' to continue or 'n' to cancel order: ")
                # check for valid option
                while add_more != 'y' and add_more != 'n':
                    add_more = input("Invalid option. Try again: ")
                # user opts to cancel
                if add_more == 'n':
                    # print cancelation note and refund
                    print(f"\nOrder canceled. Here is ${money_received:.2f} in refund.")
                    input("\nPress ENTER to go back to main menu.")
                    # cancel order
                    is_cancelled = True
                    continue
                # user opts to add more money
                else:
                    # receive money and print accumulated amount received
                    money_received += receive_money()
                    print(f"\nAmount received: ${money_received:.2f}")
            
            # if order was not cancelled and there's enough money to pay for drink
            if not is_cancelled:
                # add the amount that pays for drink to machine profit
                profit += drink['cost']
                change = money_received - drink['cost']
                if change > 0:
                    print(f"\nHere is ${change:.2f} in change.")
                # make drink
                make_drink(choice, drink['ingredients'])

                input("\nPress ENTER to go back to main menu")

        # invalid choice
        else:
            input("Invalid option.\nPress ENTER to go back to main menu.")
