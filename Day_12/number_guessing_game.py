from random import randint
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
    attempts = 5
else:
    attempts = 10

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Guess the number"))
    if guess == number:
        print(f'You got it number is {number}')
        break
    elif guess > number:
        print('Too high')
        attempts -= 1
    else:
        print('Too low')
        attempts -= 1
    
if attempts == 0:
    print("You've run out of guesses.")