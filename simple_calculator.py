import os
def add(num1, num2):
    '''
    This is a simple add function that returns the sum of two numbers.
    '''
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2


choice = 'n'
while True:
    if choice == "n":
        os.system("cls")
        first_number = float(input("What's the first number : "))
    operation = input('''
    +
    -
    /
    *
    Pick an operation :''')
    print()
    next_number = float(input("What's the next number : "))

    if operation == "+":
        result = add(first_number, next_number)
    elif operation == "-":
        result = sub(first_number, next_number)
    elif operation == "*":
        result = mul(first_number, next_number)
    elif operation == "/":
        result = div(first_number, next_number)

    print(f"{first_number} {operation} {next_number} = {result}")
    first_number = result
    choice = input(f"To continue the calculation with {result} type 'y' to start a new calcuation type 'n'.")