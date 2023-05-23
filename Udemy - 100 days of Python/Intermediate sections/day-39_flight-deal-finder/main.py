# Program Requirements
import os
import requests

## Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
## International Air Transport Association (IATA) codes for each city.
## Most of the cities in the sheet include multiple airports, you want the city code (not the airport code).

# get data from spreadsheet
from data_manager import DataManager
data_manager = DataManager()
sheety_res_data = data_manager.get_prices_sheet_data()

## Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
## In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months time.
## We're also looking for round trips that return between 7 and 28 days in length.
## The currency of the price we get back should be in CAD.
from datetime import datetime, timedelta
ORIGIN = 'YVR'
DEPART_DATE_FROM = (datetime.now() + timedelta(1)).date()
DEPART_DATE_TO = (datetime.now() + timedelta(weeks=24)).date()
MIN_STAY = 7
MAX_STAY = 28
CURRENCY = 'CAD'

# get IATA codes for each city and add them to the respective column in the spreadsheet
from flight_search import FlightSearch
flight_search = FlightSearch()
for row in sheety_res_data:
    if row["iataCode"] == "":
        iataCode = flight_search.get_iata_code(row["city"])
        data_manager.update_iata_code(row["id"], iataCode)
    
    ## Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
    TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
    headers = {
        "apikey": os.environ.get('TEQUILA_API_KEY')
    }
    params = {
        "fly_from": ORIGIN,
        "fly_to": row["iataCode"],
        "date_from": DEPART_DATE_FROM,
        "date_to": DEPART_DATE_TO,
        "nights_in_dst_from": MIN_STAY,
        "nights_in_dst_to": MAX_STAY,
        "flight_type": "round",
        "curr": CURRENCY,
        "price_to": row["lowestPrice"]
    }

    flights_res = requests.get(f'{TEQUILA_ENDPOINT}/search', params=params,headers=headers)
    flights_res.raise_for_status()
    flights_res_data = flights_res.json()
    print(flights_res_data)








## If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
## The SMS should include the departure airport IATA code, destination airport IATA code, departure city, 
## destination city, flight price and flight dates.