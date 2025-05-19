# This is a secreat bid app
from os import system

bidders = {}
logo = r"""
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
"""
keep_going = 'yes'
print(logo)
while keep_going == 'yes':
    name = input('Enter Your Name : ')
    bid = float(input('Enter Your Bid $'))
    bidders[name] = bid
    keep_going = input('Are there any other bidders "yes" or "no" : ').lower()
    system('cls')

highest_bid = 0
highest_bidder = ''
for bidder in bidders:
    bid = bidders[bidder]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(f"highest bidder = {highest_bidder} highest_bid = {highest_bid}")
