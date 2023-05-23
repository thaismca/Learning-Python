# Program Requirements

## Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
## International Air Transport Association (IATA) codes for each city.
## Most of the cities in the sheet include multiple airports, you want the city code (not the airport code).

import requests
import os

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# get data from spreadsheet
from data_manager import DataManager
data_manager = DataManager()
sheety_res_data = data_manager.get_prices_sheet_data()

# get IATA codes for each city and add them to the respective column in the spreadsheet
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
for row in sheety_res_data:
    if row["iataCode"] == "":
        headers = {
            "apikey": os.environ.get('TEQUILA_API_KEY')
        }
        params = {
            "term": row["city"],
            "location_types": "city"
        }
        location_res = requests.get(f'{TEQUILA_ENDPOINT}/locations/query', params=params,headers=headers)
        location_res.raise_for_status()
        location_res_data = location_res.json()["locations"]
        
        sheety_edit_row_endpoint=f'https://api.sheety.co/ecd388c9c56d18a14d531a5e0532f1b9/flightDeals/prices/{row["id"]}'
        sheety_req_headers = {
            "Authorization": "Basic " + os.environ.get('SHEETY_AUTH'),
        }
        sheety_edit_row_req_body = {
                "price": {
                    "iataCode": location_res_data[0]["code"]
                }
        }
        sheety_post_res = requests.put(url=sheety_edit_row_endpoint, json=sheety_edit_row_req_body, headers=sheety_req_headers)
        sheety_post_res.raise_for_status()



## Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

## If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
## The SMS should include the departure airport IATA code, destination airport IATA code, departure city, 
## destination city, flight price and flight dates.