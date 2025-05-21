# This is the coffee machine code

parameters = {
"water" : 300,
"milk" : 200,
"coffee" : 100,
"money" : 0
}
coffees = {
    "espresso" : {"water" : 50,"milk" : 0, "coffee" : 18, "money" : 1.50},
    "latte" : {"water" : 200, "milk": 150, "coffee" : 24, "money" : 2.50},
    "cappuccino" : {"water" : 250, "milk" : 100, "coffee" : 24, "money" : 3.00}
}

# Get money funciton
def get_money():
    total_money = 0
    print("Please Insert Coins.")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many Dimes : "))
    nickels = int(input("How many nickels : "))
    penny = int(input("How many pennies : "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (penny * 0.01)
    return total_money

def make_coffee(money, coffee):
    coffee_name = coffee
    coffee = coffees[coffee]
    # Accessing global parameters to update them
    global parameters
    # Checks
    if coffee["money"] > money:
        return f"Not Enough money your ${money} refunded"
    elif coffee["coffee"] > parameters["coffee"]:
        return f"Not Enough Coffee your ${money} refunded"
    elif coffee["milk"] > parameters["milk"]:
        return f"Not Enough  your ${money} refunded"
    elif coffee["water"] > parameters["water"]:
        return f"Not Enough Water your ${money} refunded"
    else:
        # Adding money to machine
        parameters["money"] += coffee["money"]
        # Making coffee using resources
        parameters["coffee"] -= coffee["coffee"]
        parameters["milk"] -= coffee["milk"]
        parameters["water"] -= coffee["water"]
        money -= coffee["money"]
        return f"Here is ${money} in change\nHere is Your {coffee_name} ☕ Enjoy!"
    return coffee

# Loop to repeadely ask
while True:
    user_input = input("What would you like? (espresso/latte/cappuccino) : ")
    if user_input == 'off':
        break
    elif user_input == 'report':
        for parameter in parameters:
            print(f"{parameter} : {parameters[parameter]}")
    
    elif user_input == 'espresso':
        money = get_money()
        print(make_coffee(money, user_input))
    elif user_input == 'latte':
        money = get_money()
        print(make_coffee(money, user_input))
    elif user_input == 'cappuccino':
        money = get_money()
        print(make_coffee(money, user_input))
    else:
        print("Invalid Input!")   