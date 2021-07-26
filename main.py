import requests
import os
from datetime import datetime as dt

USERNAME = "tommynov1000"
TOKEN = os.environ['PIXELA_USER_KEY']
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "DevOps Studying Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

record_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

record_params = {
    "date": dt.now().strftime("%Y%m%d"),
    "quantity": "2.5",
}

# response = requests.post(url=record_endpoint, json=record_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210705"

update_params = {
    "quantity": "3",
    "optionalData": "{\"Description\": \"Testing\"}"
}

response = requests.put(url=update_endpoint, headers=headers, json=update_params)
print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
