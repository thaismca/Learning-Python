import os
import requests
import datetime as dt

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

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
print(nutritionix_res.text)
nutritionix_res.raise_for_status()