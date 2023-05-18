# COURSE SCOPE

# STEP 1: create user in Pixela
## endpoint: 'https://pixe.la/v1/users'
## username must be unique -> if you try to create a user passing a username that already exists, you will get a 409 response

# STEP 2: create a new graph for the user
## endpoint: 'https://pixe.la/v1/users/<username>/graphs'
## must provide id, name, unit, type, and color parameters
## token must be provided in the request headers
## more details in the docs: https://docs.pixe.la/entry/post-graph

# STEP 3: add a pixel to the habit tracker
## endpoint: 'https://pixe.la/v1/users/<username>/graphs/<graphID>'
## must provide date and quantity in the parameters
## token must be provided in the request headers
## more details in the docs: https://docs.pixe.la/entry/post-pixel

# EXTRA CHALLENGE
## Make this as a program that runs in the terminal an can be used to create a new user and manage an user's graph(s) 