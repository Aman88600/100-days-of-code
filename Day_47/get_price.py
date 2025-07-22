import requests
from bs4 import BeautifulSoup

def get_price() -> float:
    # Getting the entire conent of the website
    URL = "https://www.amazon.in/Acer-i7-12700H-Processor-4G-GDDR6-AN515-58/dp/B0C8YR141Q/ref=sr_1_1?nsdOptOutParam=true&sr=8-1"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url=URL, headers=headers)
    text_html = response.text

    # Scrapping the price from the text
    soup = BeautifulSoup(text_html, 'html.parser')
    price = soup.find(name='span', class_="a-price-whole")
    price_fraction = soup.find(name='span', class_="a-price-fraction")
    price = str(price.get_text())
    price_fraction = str(price_fraction.get_text())

    # Comma remover function
    def comma_remover(price: str) -> str:
        list_of_split = price.split(",")
        final_price = ""
        for i in list_of_split:
            final_price += i
        price = final_price
        return price

    # Getting total price
    price = comma_remover(price)
    total_price = float(price + price_fraction)
    return total_price