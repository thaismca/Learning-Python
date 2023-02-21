from machine_config import resources, menu

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# print resources report
def print_report(profit):
    print("Coffee Machine resources:")
    for k, v in resources.items():
        print(f"-> {k.capitalize()}: {v['quantity']:,} {v['unit']}")
    print(f"\nMoney: {profit}")

# check for low resources
def check_low_resources():
    print("ALERT!\nLow resources:")
    for k, v in resources.items():
        if v['quantity'] < v['min']:
            print(f"-> {k.capitalize()}: {v['quantity']:,} {v['unit']}")

# check sufficient resources for drink
def is_sufficient_resources(drink):
    for ingredient, quantity in menu[drink]['ingredients'].items():
        if resources[ingredient]['quantity'] < quantity:
            return False
    return True

# show menu
def show_available_menu():
    available = []
    print("::: COFFEE MACHINE MENU :::")

    for drink in menu.keys():
        if is_sufficient_resources(drink):
            available.append(drink)
            print(f"-> {drink}")

    return(available)

# validate coins quantity
def validate_coins(qtd):
    try:
        qtd = int(qtd)
    except:
        qtd = 0
    return qtd

# receive money
def receive_money():
    money_received = 0
    
    quarters = input("How many quarters? ")
    quarters = validate_coins(quarters)
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
    for ingredient in ingredients:
        resources[ingredient]['quantity'] -= ingredients[ingredient]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
profit = 0
while is_on:
    clear()
    available_menu = show_available_menu()
    if len(available_menu) < 1:
        print("Not enough resources in this machine.")
        break
    else:
        choice = input("What would you like? ").lower()
        if choice == 'report':
            print_report(profit)
            input("Press ENTER to go back to main menu.")
            continue
        elif choice == 'off':
            is_on = False
            continue
        elif choice in available_menu:
            drink = menu[choice]
            print(f"This drink costs ${drink['cost']}")
            money_received = receive_money()
            print(f"\nAmount received: ${money_received:.2f}")
            
            is_cancelled = False
            while money_received < drink['cost'] and not is_cancelled:
                print(f"Amount due: ${drink['cost'] - money_received:.2f}\n")
                add_more = input("Want to add more coins? Type 'y' to continue or 'n' to cancel order: ")
                while add_more != 'y' and add_more != 'n':
                    add_more = input("Invalid option. Try again: ")
                if add_more == 'n':
                    print(f"Order canceled. Here is {money_received} in refund.")
                    input("Press ENTER to go back to main menu.")
                    is_cancelled = True
                    continue
                else:
                    money_received += receive_money()
                    print(f"\nAmount received: ${money_received:.2f}")
            
            if not is_cancelled:
                profit += drink['cost']
                make_drink(choice, drink['ingredients'])

                input("Press ENTER to go back to main menu")
        else:
            input("Invalid option.\nPress ENTER to go back to main menu.")
        
        


