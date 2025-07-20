from bs4 import BeautifulSoup
import requests

def get_songs(date):
    headers = { 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
    url = f'https://www.billboard.com/charts/hot-100/{date}/'

    response = requests.get(url=url, headers = headers)

    text = response.text
    print(url)

    # Making a object of the BeautifulSoup class
    soup = BeautifulSoup(text, 'html.parser')

    # Find all h3 tags with id="title-of-a-story"
    titles = soup.find_all('h3', id='title-of-a-story')


    refined_list_1 = []
    for title in titles:
        if ":" in str(title.string):
            pass
        else:
            new_string = str(title.string)[14:]
            new_string = new_string[0:len(new_string) - 5]
            refined_list_1.append(new_string)

    refined_list_2 = []
    for item in refined_list_1:
        if len(item) == 0:
            pass
        elif str(item) == 'Gains in Weekly Performance':
            pass
        elif str(item) == 'Additional Awards':
            pass
        else:
            refined_list_2.append(item)
            if len(refined_list_2) == 100:
                print(f"Its 100 at {item}")
                break
    return refined_list_2
