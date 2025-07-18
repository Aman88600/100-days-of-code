# Importing beautiful soup class
from bs4 import BeautifulSoup

import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")

text = response.text
soup = BeautifulSoup(text, "html.parser")

# Getting Title and Link of the posts using anchor tags
anchor_tags = soup.find_all(name="a", class_="storylink")
# getting the upvotes of the posts
up_votes = soup.find_all(name="span", class_="score")


i = 0
name_link_vote = {}
vote_list = []
while i < len(anchor_tags):
    # print(f"name = {anchor_tags[i].string}")
    # print(f"link = {anchor_tags[i].get("href")}")
    vote_list.append(int(up_votes[i].string.split()[0]))
    # print(f"up_votes = {int(up_votes[i].string.split()[0])}")
    name_link_vote[int(up_votes[i].string.split()[0])] = [anchor_tags[i].string, anchor_tags[i].get("href")]
    i += 1  

vote_list.sort(reverse=True)
for vote in vote_list:
    print(name_link_vote[vote])