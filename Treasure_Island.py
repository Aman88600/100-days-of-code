# 1. Print the ASCII art of the Treasure

print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

# 2. Greet the User
print("Welcome to Treasure Island!")

# 3. Tell the user the objective of the game
print("Your mission is to find Treasure.")

# 4. Give the user a choice between 2 choices left and right
choice_left_or_right = input("You're at a road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if choice_left_or_right == "left":
    choice_swim_or_wait = input("You come to a lake. There is an Island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross\n").lower()
    if choice_swim_or_wait == "wait":
        chocie_door = input("You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color door do you choose?\n").lower()
        if chocie_door == "yellow":
            print("You Get the Treasure. You Win!\n")
        elif chocie_door == "red":
            print("It's a room full of fire. Game Over!\n")
        elif chocie_door == "blue":
            print("You enter a room full of beasts. Game Over!\n")
    elif choice_swim_or_wait == "swim":
        print("You met a giant Shark. Game Over!\n")
elif choice_left_or_right == "right":
    print("You fell into a hole. Game Over!\n")