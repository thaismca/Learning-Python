# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#importing classes
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

# instantiating objects from classes imported
maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
    
# starting coffee machine
is_on = True
while is_on:
    # clear console at every new action
    clear()
    # display alert for low resources, if any
    maker.check_low_resources()

    # get available items
    menu_items = menu.get_items()
    available = maker.get_available_drinks(menu_items)
    
    # no items available
    if len(available) < 1:
        # display message and wait for the user to hit enter to turn the machine off
        print("Not enough resources in this machine.")
        input("\nPress ENTER to turn the machine off and restock resources.")
        is_on = False
        continue

    # at least one item available
    else:
        # ask for user input
        choice = input("\nWhat would you like? ").lower()

        # admin possible choice -> prints resources and money reports
        if choice == 'report':
            maker.report()
            money.report()
            input("\nPress ENTER to go back to main menu.")
            continue

        # admin possible choice -> turns machine off
        elif choice == 'off':
            is_on = False
            continue

        # try to find the drink in the list of possible items from menu 
        drink = menu.find_drink(choice)
        # if find_drink returns None, or the drink returned is not in the available menu 
        if not drink or drink not in available:
            print("\nSorry, that is not an available item.")
            input("\nPress ENTER to go back to main menu.")
            continue

        # if it's a valid, available drink 
        else:
            # print drink's cost
            print(f"\nThis drink costs ${drink['cost']:.2f}")
            # receive payment
            order_paid = money.is_done_payment(drink['cost'])
            # if payment was made in full
            if order_paid:
                # make drink
                maker.make_coffee(drink)
            input("\nPress ENTER to go back to main menu.")