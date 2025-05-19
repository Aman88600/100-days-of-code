from random import randint
print('Welcome to PyPassword Generator!')
letters = int(input('How many letters would you like in your password '))
symbols = int(input('How Many symbols would you like in your password '))
numbers = int(input('How many numbers would you like in your password '))

all_letters = "abcdefghijklmnopqustuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_numbers = "01234567890"
all_symbols = '!@#$%^&*()-_+=[]{}|?/'

letters_str = ''
repeated_letters_len = len(all_letters) - 1
# Getting letters
for i in range(letters):
    random_letter_num = randint(0, repeated_letters_len)
    random_letter = all_letters[random_letter_num]
    letters_str += random_letter

number_str = ''
repeated_numbers_len = len(all_numbers) - 1
for i in range(numbers):
    random_number_num = randint(0, repeated_numbers_len)
    random_number = all_numbers[random_number_num]
    number_str += random_number


symbol_str = ''
repeated_symbols_len = len(all_symbols) - 1
for i in range(symbols):
    random_symbol_num = randint(0, repeated_symbols_len)
    random_symbol = all_symbols[random_symbol_num]
    symbol_str += random_symbol

semi_final_password = letters_str + number_str + symbol_str
password = list(semi_final_password)
pass_len = len(password)

# We shuffel the password using insert() and randint and for loop
new_password = []
new_password.insert(0, password[0]) # we put in 1 element to avoid error in the randint()
for i in range(1, pass_len):
    new_len = len(new_password)
    pos = randint(0, new_len - 1) # we get random number then insert the element in the next line
    new_password.insert(pos, password[i])

password_string = ''
for i in new_password:
    password_string += i

print(f"Your Password is : {password_string}")
    