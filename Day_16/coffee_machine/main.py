from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    user_input = input(f"What coffee do you want({menu.get_items()}) : ")
    if user_input == 'off':
        break
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink= menu.find_drink(user_input)
        if drink: # Do we have the drink
            if coffee_maker.is_resource_sufficient(drink): # Do we have enough resources to make the drink
                if money_machine.make_payment(drink.cost): # Does the buyer have enough moeny for the drink
                    coffee_maker.make_coffee(drink)
