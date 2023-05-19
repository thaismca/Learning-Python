import os
import requests
import json
import datetime as dt

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# get today's date
today = dt.datetime.now()

# Get Exercise Stats with Natural Language Queries
nutritionix_exercise_endpoint= 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutritionix_exercise_req_headers = {
    "x-app-id": os.environ.get('NUTRITIONIX_APP_ID'),
    "x-app-key": os.environ.get('NUTRITIONIX_API_KEY'),
    "Content-Type": "application/json"
}
nutritionix_exercise_req_body = {
    "query": "ran 10 kilometers in 50 minutes and cycled 30km",
    "gender": "female",
    "weight_kg": "56",
    "height_cm": "157",
    "age": "35"
}

nutritionix_res = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_exercise_req_body, headers=nutritionix_exercise_req_headers)
try:
    nutritionix_res_data = json.loads(nutritionix_res.text)

    # Use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that comes back from the Nutritionix API
    sheety_add_row_endpoint= 'https://api.sheety.co/ecd388c9c56d18a14d531a5e0532f1b9/workoutTracking/workouts'
    sheety_add_row_req_headers = {
        "Authorization": "Basic " + os.environ.get('SHEETY_AUTH'),
    }

    for exercise in nutritionix_res_data['exercises']:
        sheety_add_row_req_body = {
            "workout": {
                "date": today.strftime("%d/%m/%Y"),
                "time": today.strftime("%H:%M"),
                "exercise": exercise['name'],
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }

        sheety_res = requests.post(url=sheety_add_row_endpoint, json=sheety_add_row_req_body, headers=sheety_add_row_req_headers)
        sheety_res.raise_for_status()

except ValueError:
    print('An error occured. Please try again.')