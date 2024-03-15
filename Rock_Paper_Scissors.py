# Making a rock, paper, Scissors game in 

import random
computer_choice = random.randint(1,3)
user_input = input(f"Enter your choice 1 rock 2 paper 3 Scissors : ")
#printing computer choice
def choice(choice):
    if choice == 1:
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    elif choice == 2:
        # Paper
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    elif choice == 3:
        # Scissors
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
        
print(f"Your choice {choice(user_input)}\n\n\n computer choice = {choice(computer_choice)}")