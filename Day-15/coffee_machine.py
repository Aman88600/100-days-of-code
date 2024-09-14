coffee_emoji = '☕'
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(user_input):
    # Condition to check espresso
    if user_input != "espresso":
        if (resources["milk"] < MENU[user_input]["ingredients"]["milk"]):
            return "Sorry there is not enough milk"
    if (resources["water"] < MENU[user_input]["ingredients"]["water"]):
        return "Sorry ther is not enough water"
    elif (resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]):
        return "Sorry there is not enough cofee"
    else:
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        if user_input != "espresso":
            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        return f"Here is your {user_input} {coffee_emoji} Enjoy!"


# The coffee machine will run until stopped
while True:
    user_input = input("What would you like?(espresso/latte/cappuccino):")
    # Turn off feature
    if user_input == "off":
        break
    # report feature
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
    # latte feature
    elif user_input == "latte":
        print(check_resources(user_input))
    # espresso feature
    elif user_input == "espresso":
        print(check_resources(user_input))
    elif user_input == "cappuccino":
        print(check_resources(user_input))
    else:
        print(f"{user_input} is a invalid Input")