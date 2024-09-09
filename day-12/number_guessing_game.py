from random import randint
# This is a number guessing game, with 2 difficulty levels, easy and hard
# Easy is 10 attempts
# Hard is 5 attempts

# This is the number the user needs to predict
number = randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a Number between 1 and 100")
difficulty = input("Choose Difficulty hard or easy : ")

attempts = 0
if difficulty == 'easy':
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} Attempts left")
        attempts -= 1
else:
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} Attempts left")
        attempts -= 1
