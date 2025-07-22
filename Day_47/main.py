from get_price import get_price
from notification import tell_user
from time import sleep

# Giving the notification
i = 0
while i < 3:
    # Getting the price
    price = get_price()
    print(f"Price is {price}")
    if price < float(1_000_000):
        tell_user(price)
    sleep(10)
    i += 1