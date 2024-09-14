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

# Function to check if we have enough resources to make coffee
def check_resources(user_input):
    if user_input != "espresso":
        if (resources["milk"] < MENU[user_input]["ingredients"]["milk"]):
            return ["Sorry there is not enough milk", False]
    if (resources["water"] < MENU[user_input]["ingredients"]["water"]):
        return ["Sorry ther is not enough water", False]
    elif (resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]):
        return ["Sorry there is not enough cofee", False]
    else:
        return [f"Here is your {user_input} {coffee_emoji} Enjoy!", True]        
    

# Insert coin function
def insert_coin(user_input):
    print("Please insert coins.")
    quarter = float(input("How many quarters?: "))
    dime = float(input("How many dimes?: "))
    nickel = float(input("How many nickles?: "))
    penny = float(input("How many pennies?: "))
    total_value = (COIN_VALUES["quarter"] * quarter) + (COIN_VALUES["dime"] * dime) + (COIN_VALUES["nickel"] * nickel) + (COIN_VALUES["penny"] * penny) 
    if MENU[user_input]["cost"] <= total_value:
        # Adding money to machine
        resources["money"] += MENU[user_input]["cost"]
        # Giving user change back
        amount = total_value - MENU[user_input]["cost"] 
        formatted_price = "{:.2f}".format(amount)
        print(f"Here is ${formatted_price} in change") 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(user_input):
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
        function_output = check_resources(user_input)
        if function_output[1]:
            if insert_coin(user_input):
                print(make_coffee(user_input))
        else:
            print(function_output[0])
    # espresso feature
    elif user_input == "espresso":
        function_output = check_resources(user_input)
        if function_output[1]:
            if insert_coin(user_input):
                print(make_coffee(user_input))
        else:
            print(function_output[0])
    # cappuccino feature
    elif user_input == "cappuccino":
        function_output = check_resources(user_input)
        if function_output[1]:
            if insert_coin(user_input):
                print(make_coffee(user_input))
        else:
            print(function_output[0])
    else:
        print(f"{user_input} is a invalid Input")