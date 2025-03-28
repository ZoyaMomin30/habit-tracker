import requests
from datetime import datetime
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# STEP 1 : CREATE ACCOUNT ON PIXELA

token = os.getenv('token')
username = os.getenv('username')
pixela_endpoint = os.getenv('pixela_endpoint')

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# we have set up a user account on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP 2 : step is to create graph

# the endpoint is this way "/v1/users/<username>/graphs"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_id = "graph2"

graph_params = {
    "id" : graph_id,
    "name" : "Productive Coding Hours",
    "unit" : "hours",
    "type" : "int",
    "color" : "kuro"
}


headers = {
    "X-USER-TOKEN" : token
}

# we've already created our graph
# graph_response = requests.post(url = graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# STEP 3 is to add one color on that

post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"


# today = datetime.now()
# if  we want to color pixel of some other day
today = datetime(year=2025, month=3, day=21)

# see strftime library
# today.strftime("%Y%m%d")
color_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

pixel_color_response = requests.post(url=post_endpoint, json=color_param, headers=headers)
print(pixel_color_response.text)

# do update and delete seeing the documentation and all

#STEP 4 : update

# update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"

# new_param = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "4",
# }

# update_pixel_response = requests.put(url=update_endpoint, json=new_param, headers=headers)
# print(update_pixel_response.text)

#step 5 : delete

# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"
# delete_pixel_response = requests.delete(url=update_endpoint,  headers=headers)
