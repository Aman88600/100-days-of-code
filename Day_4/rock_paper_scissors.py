# In this game we take user choice and generate computer response with random module
from random import randint # since I only need randint

image_list = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
# Computer choice
computer_choice = randint(0,2)
# User choice
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

print('Your Choice:')
print(image_list[user_choice])
print('Computer Choice')
print(image_list[computer_choice])
if user_choice == 0:
    if computer_choice == 2:
        print('You Win')
    elif computer_choice == 1:
        print('You Lose')
    else:
        print('Draw')
elif user_choice == 1:
    if computer_choice == 0:
        print('You Win')
    elif computer_choice == 2:
        print('You Lose')
    else:
        print('Draw')
elif user_choice == 2:
    if computer_choice == 1:
        print('You Win')
    elif computer_choice == 0:
        print('You Lose')
    else:
        print("Draw")
