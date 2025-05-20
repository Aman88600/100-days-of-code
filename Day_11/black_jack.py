# This is a black jack or 21 game.

# Importing randint from random module to get random numbers from 1 to 11
from random import randint
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/   
"""
print(logo)
keep_going = input('y to play n to stop : ')
while keep_going == 'y':
    # Player Cards
    player = []
    # Dealer Cards
    dealer  = []


    def card_sum(cards):
        sum = 0
        for card in cards:
            sum += card
        return sum
    # Getting Player's first 2 cards
    player_card = randint(1,10)
    player.append(player_card)
    player_card = randint(1,11)
    player.append(player_card)

    # Getting dealer's cards until => 17, according to rules
    dealer_sum = 0
    while dealer_sum < 17:
        dealer_card = randint(1,11)
        dealer.append(dealer_card)
        dealer_sum = card_sum(dealer)




    print(f'Dealer\'s first card {dealer[0]}')
    draw = ''
    while True:
        print("Your Cards = ")
        print(player)
        if card_sum(player) == 21:
            print('You Win!')
            break
        elif card_sum(player) > 21:
            print("Bust, You Lose")
            break
        draw = input("y to draw n to pass")
        if draw == 'y':
            player.append(randint(1,11))
        elif draw == 'n':
            break

    if draw == 'n':
        if card_sum(dealer) > 21:
            print(dealer)
            print('You win dealer bust')
        else:
            if (card_sum(dealer) > card_sum(player)):
                print(f"Dealer cards = {dealer} Your cards = {player}")
                print("dealer wins")
            else:
                print(f"Dealer cards = {dealer} Your cards = {player}")
                print("you win")
    keep_going = input('y to play n to stop : ')