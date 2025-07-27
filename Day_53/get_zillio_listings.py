# To gee the zillo url
from dotenv import load_dotenv
import os
# To do the webscraping
import requests
from bs4 import BeautifulSoup

load_dotenv()
zillo_url = os.getenv("ZILLO_CLONE_URL")

response = requests.get(url=zillo_url)
text = response.text

def get_values() -> list:
    '''
    This fucntion returns the list of lists like this [clean_addresses, clean_prices, clean_links]
    '''
    soup = BeautifulSoup(text, 'html.parser')
    addresses = soup.find_all(name="img", class_="Image-c11n-8-84-listing")
    links = soup.find_all(name="a", class_="property-card-link")
    prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

    clean_addresses = []
    clean_links = []
    clean_prices = []
    for address in addresses:
        clean_addresses.append(address.get("alt"))
    for price in prices:
        clean_prices.append(price.text)
    for link in links:
        clean_links.append(link.get("href"))

    def cleaner(un_clean:list) -> list:
        '''
        This function basically cleans the strings by removing un wanter symbols such as "|"
        '''
        new_list = []
        for i in un_clean:
            new_j = i.replace('|', '')
            new_list.append(new_j)
        return new_list

    clean_addresses = cleaner(clean_addresses)
    return [clean_addresses, clean_prices, clean_links]