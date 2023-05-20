import os
import requests
import json
import datetime as dt

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# to clear console
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_user_action():
    '''Function that asks for user input to trigger one of the available actions in the program, and calls the function that 
    executes the action based on user's choice.'''
    action = input('''Select an action:
        1- Add workout
        2- Manage personal settings
        ''')

    if action == '1':
        add_workout()
    elif action == '2':
        manage_settings()
    else:
        print('Invalid action. Try again.')
        get_user_action()



def next_action():
    '''Function that asks for user input to either continue program execution or close it. It calls get_user_action again if user
    wants to continue the program execution.'''
    next = input('\nContinue to perform more actions: yes or no? ').lower()
    if next == 'yes':
        clear()
        get_user_action()
    elif next == 'no':
        exit()
    else:
        print('Invalid option')
        next_action()



def try_again(action):
    try_again = input('\nTry again: yes or no? ').lower()
    if try_again == 'yes':
        action()
    elif try_again == 'no':
        next_action()
    else:
        print('Invalid option')
        try_again(action)



def manage_settings():
    '''Function that allows user to input values for the personal settings, to be stored in the settings.json file.'''
    print("\nManaging settings")
    gender = input("Gender: male or female? ")
    weight = input("Weight (Kg): ")
    height = input("Height (cm): ")
    age = input("Age: ")

    if gender == '' or weight == '' or  height == '' or age == '':
        print('All inputs are mandatory. Try again.')
        manage_settings()
    else:
        new_settings = {
            "gender": gender,
            "weight": weight,
            "height": height,
            "age": age
        }
        with open("settings.json", "w") as file:
            json.dump(new_settings, file, indent=4)
    
    next_action()



def add_workout():
    '''Function that allows user to add a new workout to the spreadsheet. The data is save with current date and time.'''
    print("\nAdding workout")
    # get user's settings -> if file is corrupted, use default settings
    try:
        # try to open an existing data file and read data from it
        with open("settings.json", "r") as file:
            # read old data to a settings variable
            settings = json.load(file)
    except FileNotFoundError:
        #default settings
        settings = {
            "gender": "male",
            "weight": "85",
            "height": "180",
            "age": "30"
        }
        
    # today's date
    today = dt.datetime.now()

    # get user's query
    query = input('What exercise(s) did you do today? ')

    # Get Exercise Stats with Natural Language Queries
    nutritionix_exercise_endpoint= 'https://trackapi.nutritionix.com/v2/natural/exercise'
    nutritionix_exercise_req_headers = {
        "x-app-id": os.environ.get('NUTRITIONIX_APP_ID'),
        "x-app-key": os.environ.get('NUTRITIONIX_API_KEY'),
        "Content-Type": "application/json"
    }
    nutritionix_exercise_req_body = {
        "query": query,
        "gender": settings['gender'],
        "weight_kg": settings['weight'],
        "height_cm": settings['height'],
        "age": settings['age']
    }

    nutritionix_res = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_exercise_req_body, headers=nutritionix_exercise_req_headers)
    try:
        nutritionix_res_data = json.loads(nutritionix_res.text)

        try:
            if len(nutritionix_res_data['exercises']) <= 0:
                print("Invalid query")
                try_again(add_workout)
            
            else:
                # Use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that comes back from the Nutritionix API
                sheety_add_row_endpoint= 'https://api.sheety.co/ecd388c9c56d18a14d531a5e0532f1b9/workoutTracking/workouts'
                sheety_add_row_req_headers = {
                    "Authorization": "Basic " + os.environ.get('SHEETY_AUTH'),
                }
                
                for exercise in nutritionix_res_data['exercises']:
                    exercise_seconds = exercise['duration_min']
                    td = str(dt.timedelta(seconds=exercise_seconds)).split(".")[0]
                    sheety_add_row_req_body = {
                        "workout": {
                            "date": today.strftime("%d/%m/%Y"),
                            "time": today.strftime("%H:%M"),
                            "exercise": exercise['name'].capitalize(),
                            "duration": td,
                            "calories": exercise['nf_calories']
                        }
                    }

                    sheety_res = requests.post(url=sheety_add_row_endpoint, json=sheety_add_row_req_body, headers=sheety_add_row_req_headers)
                    sheety_res.raise_for_status()
                    if sheety_res.status_code == 200:
                        print('Workout added: ' + exercise['name'])    

        except KeyError:
            print('An error occured. Please try again.')

    except ValueError:
        print('An error occured. Please try again.')
    
    # get user next action
    next_action()



# execute program
get_user_action()