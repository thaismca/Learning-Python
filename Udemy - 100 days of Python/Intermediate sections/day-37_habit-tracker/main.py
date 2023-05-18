import os
import requests

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# COURSE SCOPE

# STEP 1: create user in Pixela
## endpoint: 'https://pixe.la/v1/users'
## username must be unique -> if you try to create a user passing a username that already exists, you will get a 409 response
create_user_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": os.environ["USER_TOKEN"],
    "username": os.environ["USER_NAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

res = requests.post(url=create_user_endpoint, json=user_params)
print(res.text)
res.raise_for_status()


# STEP 2: create a new graph for the user
## endpoint: 'https://pixe.la/v1/users/<username>/graphs'
## must provide id, name, unit, type, and color parameters
## token must be provided in the request headers
## more details in the docs: https://docs.pixe.la/entry/post-graph
create_graph_endpoint = f'https://pixe.la/v1/users/{os.environ["USER_NAME"]}/graphs'
graph_params = {
    "id": "graph1",
    "name": "Sample Graph",
    "unit": "times",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": os.environ["USER_TOKEN"]
}

res = requests.post(url=create_graph_endpoint, json=graph_params, headers=headers)
print(res.headers)
print(res.text)
res.raise_for_status()

# STEP 3: add a pixel to the habit tracker
## endpoint: 'https://pixe.la/v1/users/<username>/graphs/<graphID>'
## must provide date and quantity in the parameters
## token must be provided in the request headers
## more details in the docs: https://docs.pixe.la/entry/post-pixel

# EXTRA CHALLENGE
## Make this as a program that runs in the terminal an can be used to create a new user and manage an user's graph(s) 