import os
print("Welcome to the blind auction program.")

bids = {}
user_chioce = "yes"
while user_chioce == "yes":
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    bids[name] = bid
    print("Are there any other bidders? : Type 'yes' or 'no'.")
    user_chioce = input()
    os.system("cls")

highest_bid = 0
highest_bidder = ""
for key in bids:
    if int(bids[key]) > int(highest_bid):
        highest_bid = bids[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")