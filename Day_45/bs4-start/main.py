# Importing beautiful soup class
from bs4 import BeautifulSoup

import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")

text = response.text
soup = BeautifulSoup(text, "html.parser")
anchor_tags = soup.find_all(name="a", class_="storylink")

for anchor_tag in anchor_tags:
    print(anchor_tag.string)