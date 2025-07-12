import requests
from bs4 import BeautifulSoup

def get_tesla_news_rss():
    url = "https://news.google.com/rss/search?q=Tesla"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="xml")

    items = soup.find_all("item")

    return_string = "\n📰 Top Tesla News:\n"
    for i, item in enumerate(items[:5], start=1):
        title = item.title.text
        link = item.link.text
        return_string += f"{i}. {title}\n"
    return return_string
