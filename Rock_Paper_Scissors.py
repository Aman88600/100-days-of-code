# Making rock, paper and scissors game in the shell/command prompt
from random import randint
# Asking user input
confirm = 0
user_choice = 0
# Making sure that we get the correct user input
while confirm == 0:
    user_choice = input(f"Enter 1 for rock 2 for paper and 3 for scissors : ")
    # For the intergers
    try:
        user_choice = int(user_choice)
        if user_choice == 1:
            confirm = 1
        elif user_choice == 2:
            confirm = 1
        elif user_choice == 3:
            confirm = 1
        # For any other input that is not 1, 2 or 3
        else:
            confirm = 0
    # For any other type of input
    except ValueError:
        confirm = 0
    
# Getting computer choice
computer_choice = randint(1,3)

# This function takes the number choice and prints the ASCII art of that choice
def rpc(choice):
    if choice == 1:
        # Rock
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
        print("""
            _______
        ---'   ____)____
                    ______)
                __________)
                (____)
        ---.  __(___)
        """)

# Pinting the user and computer choices
print(f"Your Choice : ")
rpc(int(user_choice))
print(f"Computer Choice : ")
rpc(int(computer_choice))

# For draw case
user_choice = int(user_choice)
computer_choice = int(computer_choice)
if user_choice == computer_choice:
    print("Draw!")
# If user choses Rock
elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
elif user_choice == 1 and computer_choice == 3:
    print("You Win!")
# If user choses Paper
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == 2 and computer_choice == 3:
    print("You Lose!")
# If user choses Scissors
elif user_choice == 3 and computer_choice == 1:
    print("You Lose!")
elif user_choice == 3 and computer_choice == 2:
    print("You Win!")