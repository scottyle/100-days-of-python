import requests
from datetime import datetime
USERNAME = ""
TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token" : "",
    "username" : "",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Running Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2025, month = 11 , day =28)

todays = today.strftime("%Y%m%d")

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "4.2"
}

# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)

update = f"{pixel_endpoint}/{todays}"
update_body = {
    "quantity" : "3.0"
}

response = requests.delete(url=update,headers=headers)
print(response.text)