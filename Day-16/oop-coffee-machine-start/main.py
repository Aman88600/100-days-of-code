from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()
# Coffee Machine will run until stopped
while True:

    # Propting user for an input
    user_input = input(f"What would you like ({menu_object.get_items()}): ")
    if user_input == "off":
        break
    # Getting the users desired drink
    elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        drink = menu_object.find_drink(user_input)
        if coffee_maker_object.is_resource_sufficient(drink):
            if money_machine_object.make_payment(drink.cost):
                coffee_maker_object.make_coffee(drink)
    # Getting report of resources
    elif user_input == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        print("Invalid Input!")



    # print(obj.is_resource_sufficient(output))
    # obj.make_coffee(output)

    # # obj1.report()
    # obj1.make_payment(output.cost)