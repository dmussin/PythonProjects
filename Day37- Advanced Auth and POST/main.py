import requests
from datetime import *

# Pixela Habbit Tracker
TOKEN = "***PIXELA TOKEN***"
USERNAME = "python-musin"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# User creation
# response = requests.post(pixela_endpoint, json=params)
# print(response.text)

# Create a graph on Pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph params
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Graph",
    "unit": "Min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# Post a pixel in graph
posting_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Today's date
today = date.today()
# yyyyMMdd format
today_date = today.strftime("%Y%m%d")

# Post params
post_params = {
    "date": today_date,
    "quantity": input("How many minutes did you study today?: "),
}
# Posting
# response = requests.post(url=posting_endpoint, json=post_params, headers=headers)
# print(response.text)


# Update a pixel
update_endpoint = f"{posting_endpoint}/20230206"

update_param = {
    "quantity": "120"
}

# Updating
# response = requests.put(url=update_endpoint, json=update_param, headers=headers)
# print(response.text)


# Deleting a pixel
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
