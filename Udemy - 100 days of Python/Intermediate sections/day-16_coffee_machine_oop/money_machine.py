class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"\nMoney: {self.CURRENCY}{self.profit:.2f}")

    def validate_quantity(self, qtd):
        '''Receives a quantity and returns that quantity converted to int. If the quantity passed is not convertible to int, returns 0.'''
        try:
            qtd = int(qtd)
        except:
            qtd = 0
        return qtd

    def receive_coins(self):
        """Returns the total calculated from coins inserted."""
        print("\nPlease insert coins.")
        for coin in self.COIN_VALUES:
            coin_quantity = self.validate_quantity(input(f"How many {coin}?: "))
            self.money_received += coin_quantity * self.COIN_VALUES[coin]
        print(f"\nAmount received: ${self.money_received:.2f}")
        return self.money_received
    
    def add_more_coins(self):
        """Returns True when user wants to add more coins, or False if user wants to cancel order."""
        add_more = input("Want to add more coins? Type 'y' to continue or 'n' to cancel order: ")
        # check for valid option
        while add_more != 'y' and add_more != 'n':
            add_more = input("Invalid option. Try again: ")
        # user opts to cancel
        if add_more == 'n':
            return False
        # user opts to add more coins
        else:
            return True

    def is_done_payment(self, cost):
        """Returns True once payment is made in full, or False if insufficient and order is cancelled."""
        self.receive_coins()
        while self.money_received < cost:
            print(f"Amount due: ${cost - self.money_received:.2f}\n")
            # check if user wants to add more coins or cancel order
            if self.add_more_coins():
                self.receive_coins()
            else:
                print(f"\nOrder cancelled. Here is ${self.money_received:.2f} in refund.")
                self.money_received = 0
                return False

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True