import requests
from datetime import datetime

USERNAME = "amanbasoya"
TOKEN = "lnelAMifhe21322b"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# commit
commit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# getting date
today = datetime(year=2025 ,month=7 ,day=11)
today = today.strftime("%Y%m%d")
commit_config = {
    "date" : today,
    "quantity" : "5.65"
}
# response = requests.post(url = commit_endpoint, json=commit_config, headers=headers)
# print(response.text)

# update

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_config = {
    "quantity" : "10.00"
}

# response = requests.put(url = update_endpoint, json=update_config, headers=headers)
# print(response.text)

# Delete

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url = delete_endpoint, headers=headers)
print(response.text)