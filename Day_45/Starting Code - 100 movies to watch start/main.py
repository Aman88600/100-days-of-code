import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
text = response.text

soup = BeautifulSoup(text, 'html.parser')

movies = soup.find_all(name="h3", class_="title")

for movie in reversed(movies):
    # Write all the movies to the file(movies.txt)

    # If there is nothing in the file
    with open("movies.txt", "r") as file:
        text = file.read()
    if len(text) == 0:        
        with open("movies.txt", "w") as file:
            try:
                file.write(f"{movie.string}\n")
            except UnicodeEncodeError:
                print("Error")    
    else:
         with open("movies.txt", "a", encoding="utf-8") as file:
            try:
                file.write(f"{movie.string}\n")
            except UnicodeEncodeError:
                print("Error") 
    print(movie.string)
