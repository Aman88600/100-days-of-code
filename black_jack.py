from random import randint
card1 = randint(1,11)
card2 = randint(1,10)
user_sum = card1 + card2
computer_card1 = randint(1,11)
computer_card2 = randint(1,10)
computer_sum = computer_card1 + computer_card2
print(f"Your Cards = [{card1}, {card2}]")
print(f"Computer 1 card = {computer_card1}")

choice = 'y'
while choice == 'y':
    choice = input("Press 'y' for another card 'n' to stop : ")
    if choice == 'y':
        new_card = randint(1,11)
        print(f"New card is {new_card}")
        user_sum += new_card
        if user_sum > 21:
            print("You Lose Sum is more than 21")
            break

if user_sum > computer_sum:
    print("You Win!")
else:
    print("You Lose!")