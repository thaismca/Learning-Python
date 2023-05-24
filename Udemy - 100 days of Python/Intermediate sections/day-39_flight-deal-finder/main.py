# Program Requirements
import os
import requests


# get data from spreadsheet
from data_manager import DataManager
data_manager = DataManager()
sheety_res_data = data_manager.get_prices_sheet_data()

# get IATA codes for each city and add them to the respective column in the spreadsheet
from flight_search import FlightSearch
flight_search = FlightSearch()
try:
    for row in sheety_res_data:
        ## Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with IATA Codes for each city that doesn't have one
        if row["iataCode"] == "":
            iataCode = flight_search.get_iata_code(row["city"])
            data_manager.update_iata_code(row["id"], iataCode)
        
        ## Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
        print(flight_search.find_flights(row["iataCode"], row["lowestPrice"]))

except KeyError:
    print('Spreadsheet data is corrupted. Cannot proceed with operation.')








## If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
## The SMS should include the departure airport IATA code, destination airport IATA code, departure city, 
## destination city, flight price and flight dates.