
# COFFEE MACHINE

This project implements the coffee machine from day 15 using OOP paradigm.

This project was implemented as part of the day 16 of the course *100 days of Python*. All implementation was taken care of prior to watch the solution videos.

## Key differences from course solution

- **Show menu**

The implementation displayed in the course has a hard coded menu (espresso, latte, cappuccino). Only after the user selects an item and there's no sufficient resources to make that drink, it displays a message saying that the drink cannot be made due to the lack of resources. This implementation has a dinamic menu that consumes data from the machine_config file, and displays only the items that can be made with the current amount of resources available.

- **Receive money**

The implementation displayed in the course receives the amount of each coin only one. If user doesn't add enough coins in one try, the order is automatically cancelled and the money is refunded. This implementation allows the user to add more coins until the cost is covered, or the user has the option to cancel and get the refund.

- **Low resources alert**

This was added to the scope exclusivelly in this implementation.

- **Clear screen at the end of an action**

Whenever user presses enter to go back to main menu. This was added to the scope exclusivelly in this implementation.

## Implementation notes

The idea of the course in this projects was to provide the classes and challenge students to make use of those classes to reimplement the coffee machine project from day 15 using oop paradigm, without making any changes to the classes provided (as if we were using some sort of package). 

As per notes from the day 15 project, my implementation was different from the solution provided in the course, as part of my personal challenge to add more features to whatever project developed throughout this course. That being said, this one implementation is also different, and I made changes to the classes that were provided to accomodate for the features that I added.

![coffee machine screenshot](https://github.com/thaismca/Python-Practices/blob/30864761897274aee5c502248f0ff17354a27d8d/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-16_coffee_machine_oop/screenshot.PNG?raw=true)


## How this app works

1 . When the machine starts:
- the resources are at their fullest at the first use, and they are consumed at each drink that is made while the machine is on.
- the amount of profit in the machine starts at zero.

2. Turning the machine off replenishes all resources and collects the profits.

3. If any of the resources goes below its minimum while the machine is on, an alert is displayed in the screen listing all the resources that are low and the respective current quantity.

3. A list of the drinks from the machine_config menu that can be made with the current amount of available resources is displayed in the screen, and user is prompted to choose a drink.
If there are not enough resources to make any drink, a notification is displayed and the user is prompted to turn the machine off, so the resources can be replenished.

4. The user can type the name of the drink that they want. 
- If an invalid option is typed, the user is prompted with a notification and can press enter to restart.
- If a valid option is entered, the cost for the drink will be displayed, and the user will be prompted to type how many of each coin (quarter, dime, nickle and penny) they are inserting.

5. If user adds enough coins to make up for the drink's cost:
- The drink will be made, deducting the amount of ingredients from the resources.
- The cost of the drink will be added to the machine profits.
- A message with the amount of change will be displayed, if there's any.
- A message notifying the user that the drink is ready will be displayed.
- User will be prompted to press enter to return to the main menu.

6. If coins added are not enough to pay for the drink, the user will be prompted with the amount due and the option to add more coins or cancel the order.
- If order is cancelled, the money is refunded (message is displayed) and player is prompted to press enter to go back to the main menu.
- If user wants to add more coins, the user will be again prompted to type how many of each coin (quarter, dime, nickle and penny) they are inserting.
- This loop repeats until either the user insert enough coins to pay for the drink, which triggers item 5, or the user cancels the order.

7. The machine has two admin commands that can be typed instead of a drink choice:
- 'report': prints a report that lists the current quantity of each resource, and the current amount of profit that the machine has made.
- 'off': turns the machine off.

## Installation and usage
### Requirements
- must have python installed
### How to run this program
- clone this repository
- click to open the main.py file with Python
### How to use the coffee machine
#### Ordering drinks
- type the name of the drink you want (not case senstive)
- if the order entered is for an available drink, you will be prompted to insert coins
- type the number for each one of the coins (quarter, dime, nickel, penny)
- once the amount of coins entered are enpugh to cover the drink costs, you will be served your drink
- the process of inserting coins can be interrupted at any round, so your order will be cancelled and you will receive a refund of the amount you've added
#### Running admin commands
- you can see a report on the amount of resources and money currently available on the machine by typing *report* instead of a drink
- you can turn the machine off by typing *off* instead of a drink
- turning the machine off and on again "replenishes" the resources and "collects" the profits
