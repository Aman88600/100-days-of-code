from random import randint
for i in range(1,11):
    card1 = randint(1,11)
    card2 = randint(1,10)
    user_sum = card1 + card2
    computer_card1 = randint(1,11)
    computer_card2 = randint(1,10)
    computer_sum = computer_card1 + computer_card2
    print(f"Your cards = [{card1},{card2}] sum = {user_sum}")
    print(f"Computer Cards = [{computer_card1}, {computer_card2}] sum = {computer_sum}")
    if user_sum >= computer_sum:
        print("You Win")
    else:
        print("Computer Wins")
