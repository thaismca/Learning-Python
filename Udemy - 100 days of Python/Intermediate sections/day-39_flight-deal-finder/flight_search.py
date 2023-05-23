import requests
import os

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city):
        '''This function returns the IATA code for a given city'''
        headers = {
            "apikey": os.environ.get('TEQUILA_API_KEY')
        }
        params = {
            "term": city,
            "location_types": "city"
        }
        location_res = requests.get(f'{TEQUILA_ENDPOINT}/locations/query', params=params,headers=headers)
        location_res.raise_for_status()
        location_res_data = location_res.json()["locations"]
        
        return location_res_data[0]["code"]