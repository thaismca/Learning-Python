class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": {
                "quantity": 600,
                "unit": 'mL',
                'min': 300
            },
            "milk": {
                "quantity": 380,
                "unit": 'mL',
                'min': 120
            },
            "coffee": {
                "quantity": 100,
                "unit": 'mg',
                'min': 50
            },
        }

    def report(self):
        """Prints a report of all resources."""
        print("\nCoffee Machine resources:\n")
        # iterate through the resources dictionary
        for k, v in self.resources.items():
        # print the resource and the qauntity available
            print(f"{k.capitalize()}: {v['quantity']:,} {v['unit']}")

    # check for low resources
    def check_low_resources(self):
        '''It checks there are resources below the minimum amount and prints them'''
        # get a copy of all resources that are below min
        low = {k: v for k, v in self.resources.items() if v['quantity'] < v['min']}
        # if there are items in low
        if low.keys():
            print("ALERT!!! Low resources:")
            # for each item in low, print the item and the quantity
            for k, v in low.items():
                print(f"-> {k.capitalize()}: {v['quantity']} {v['unit']}")        
            print("\n")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for ingredient, quantity in drink['ingredients'].items():
            if self.resources[ingredient]['quantity'] < quantity:
                can_make = False
        return can_make
    
    def get_available_drinks(self, drinks):
        """Prints and returns a list of the drinks that can be made from a list of drinks, based on the amount of the available resources."""
        available = []
        print("::: COFFEE MACHINE MENU :::")
        for drink in drinks:
            if self.is_resource_sufficient(drink):
                available.append(drink)
                print(f"-> {drink['name'].capitalize()}")
        
        return available

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for ingredient, quantity in order['ingredients'].items():
            self.resources[ingredient]['quantity'] -= quantity
        print(f"\n:: Here is your {order['name']} :: ☕ :: Enjoy! ::")
