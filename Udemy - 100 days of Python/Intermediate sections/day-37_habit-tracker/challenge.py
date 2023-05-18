import requests
import json

# EXTRA CHALLENGE
## Make this as a program that can be used to create a new user and manage an user's graph(s)

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_user_action():
    '''Function that asks for user input to trigger one of the available actions in the program, and calls the function that 
    executes the action based on user's choice.'''
    action = input('''Select an action:
    1 - Create Pixela User
    2 - Create new Graph
    3 - Create a Pixel in a Graph
    4 - Update a Pixel in a Graph
    5 - Delete a Pixel in a Graph
    ''')

    if action == '1':
        create_user()
    elif action == '2':
        create_graph()
    elif action == '3':
        create_pixel()
    elif action == '4':
        update_pixel()
    elif action == '5':
        delete_pixel()
    else:
        print('Invalid Action')
        get_user_action()



def next_action():
    '''Function that asks for user input to either continue program execution or close it. It calls get_user_action again if user
    wants to continue the program execution.'''
    next = input('Continue to perform more actions: yes or no? ').lower()
    if next == 'yes':
        clear()
        get_user_action()
    elif next == 'no':
        exit()
    else:
        print('Invalid option')
        next_action()



def after_request(res_data, action):
    '''Function that handles steps that happen after a request to Pixela returns a response.
    It receives the response data and the action that was being performed to generate that response.'''
    if res_data['isSuccess'] == True:
        next_action()
    else:
        try_again = input('Try again: yes or no? ').lower()
        if try_again == 'yes':
            action()
        elif try_again == 'no':
            next_action()
        else:
            print('Invalid option')
            after_request(res_data, action)



def create_user():
    '''Function that asks for user input and get that data to generate a new user in Pixela.'''
    print('\nCreating a new user in Pixela')
    username = input('Username: ')
    token = input('Token: ')
    agree_terms = input('Agree to Terms of Service: yes or no? ').lower()
    not_minor = input('Not Minor: yes or no? ').lower()

    if username == '' or token == '' or agree_terms == '' or not_minor == '':
        print('All inputs are mandatory. Try again.')
        create_user()

    create_user_endpoint = 'https://pixe.la/v1/users'
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_terms,
        "notMinor": not_minor
    }

    res = requests.post(url=create_user_endpoint, json=user_params)
    try:
        res_data = json.loads(res.text)
        print(res_data['message']+ '\n')
        after_request(res_data, create_user)
    except ValueError:
        print('An error occured. Please try again.')
        create_graph()
    


def create_graph():
    '''Function that asks for user input and get that data to generate a new graph for an user in Pixela.'''
    print('\nCreating a new graph in Pixela')
    username = input('Username: ')
    token = input('Token: ')
    graph_id = input('Graph Id: ')
    graph_name = input('Graph Name: ')
    graph_unit = input('Graph Unit: ')
    unit_type = input('Unit type: int or float? ').lower()
    graph_color = input('Graph color: shibafu, momiji, sora, ichou, ajisai or kuro? ').lower()

    create_graph_endpoint = f'https://pixe.la/v1/users/{username}/graphs'
    graph_params = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": unit_type,
        "color": graph_color
    }
    headers = {
        "X-USER-TOKEN": token
    }

    if username == '' or token == '' or graph_id == '' or graph_name == '' or graph_unit == '' or unit_type == '' or graph_color == '':
        print('All inputs are mandatory. Try again.')
        create_graph()

    res = requests.post(url=create_graph_endpoint, json=graph_params, headers=headers)
    try:
        res_data = json.loads(res.text)
        print(res_data['message']+ '\n')
        after_request(res_data, create_graph)
    except ValueError:
        print('An error occured. Please try again.')
        create_graph()



def create_pixel():
    '''Function that asks for user input and get that data to generate a new pixel in a user's Graph in Pixela.'''
    print('\nCreating a new pixel in Pixela')
    username = input('Username: ')
    token = input('Token: ')
    graph_id = input('Graph Id: ')
    date = input('Date (format yyyyMMdd - only numbers): ')
    quantity = input('Quantity: ')

    if username == '' or token == '' or graph_id == '' or date == '' or quantity == '':
        print('All inputs are mandatory. Try again.')
        create_pixel()

    create_pixel_endpoint = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}'
    pixel_params = {
        "date": date,
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": token
    }

    res = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
    try:
        res_data = json.loads(res.text)
        print(res_data['message']+ '\n')
        after_request(res_data, create_pixel)
    except ValueError:
        print('An error occured. Please try again.')
        create_pixel()



def update_pixel():
    '''Function that asks for user input and get that data to update a existing pixel in a user's Graph in Pixela.'''
    print('\nUpdating a pixel in Pixela')
    username = input('Username: ')
    token = input('Token: ')
    graph_id = input('Graph Id: ')
    date = input('Date (format yyyyMMdd - only numbers): ')
    quantity = input('Quantity: ')

    if username == '' or token == '' or graph_id == '' or date == '' or quantity == '':
        print('All inputs are mandatory. Try again.')
        update_pixel()

    update_pixel_endpoint = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}'
    update_pixel_params = {
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": token
    }

    res = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
    try:
        res_data = json.loads(res.text)
        print(res_data['message']+ '\n')
        after_request(res_data, update_pixel)
    except ValueError:
        print('An error occured. Please try again.')
        update_pixel()



def delete_pixel():
    '''Function that asks for user input and get that data to delete a existing pixel in a user's Graph in Pixela.'''
    print('\nDeleting a pixel in Pixela')
    username = input('Username: ')
    token = input('Token: ')
    graph_id = input('Graph Id: ')
    date = input('Date (format yyyyMMdd - only numbers): ')

    if username == '' or token == '' or graph_id == '' or date == '':
        print('All inputs are mandatory. Try again.')
        delete_pixel()

    delete_pixel_endpoint = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}'
    headers = {
        "X-USER-TOKEN": token
    }

    res = requests.delete(url=delete_pixel_endpoint, headers=headers)
    try:
        res_data = json.loads(res.text)
        print(res_data['message']+ '\n')
        after_request(res_data, delete_pixel)
    except ValueError:
        print('An error occured. Please try again.')
        delete_pixel()



## run program
get_user_action()