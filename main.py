from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    # Take user input
    user_option = input("What would you like? (espresso/latte/cappuccino): ")

    if user_option == "report":
        coffee_maker.report()
    elif user_option == "off":
        break
    else:
        # Get ordered drink object
        ordered_drink = menu.find_drink(user_option)

        # Check if resources are enough
        is_resources = coffee_maker.is_resource_sufficient(ordered_drink)

        is_paid = False

        if is_resources:
            # Process payments
            is_paid = money_machine.make_payment(ordered_drink.cost)

        if is_resources and is_paid:
            # Update resources
            coffee_maker.make_coffee(ordered_drink)
