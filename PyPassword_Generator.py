# PyPassword Generator
import random

# Generator function
def generator(number_of_something, string_of_something):
    password = []
    letters = string_of_something
    for i in range(0, number_of_something):
        letters = list(letters)
        num = random.randint(0, len(letters) - 1)
        password.append(letters[num])
    # letters.pop(num)
    password_str = "".join(password)
    return password_str

# 1. Greet the User
print("Welcome to the PyPassword Generator!")
# 2. Ask to user to enter the number of letters he/she would like
number_of_letters = int(input("How many letter would you like?\n"))
# 3. Ask to user to enter the number of Symbols he/she would like
number_of_symbols = int(input("How many symbols would you like?\n"))
# 4. Ask to user to enter the number of number he/she would like
number_of_numbers = int(input("How many numbers would you like?\n"))


# 5. Generate the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettes_str = generator(number_of_letters, letters)
numbers = "0123456789"
numbers_str = generator(number_of_numbers, numbers)
symbols = "!@#$%^&*()[]<>?/+-"
symbols_str = generator(number_of_symbols, symbols)
# 6. Show the password to the user
print(f"Password = {lettes_str}{numbers_str}{symbols_str}")