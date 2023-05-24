import requests
import os

# retrieving hidden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        # sheety endpoint
        self.endpoint = os.environ.get('SHEETY_ENDPOINT')
        
        # request headers
        self.headers = {
            "Authorization": f"Basic {os.environ.get('SHEETY_AUTH')}"
        }

    def get_prices_sheet_data(self):
        '''This function retrieves and returns all data from the Flight Deals spreadsheet.'''    
        sheety_res = requests.get(url=self.endpoint, headers=self.headers)
        sheety_res.raise_for_status()
        
        return sheety_res.json()['prices']

    
    def update_iata_code(self, id, iataCode):
        '''This function updates the IATA code at a given row (id) in the Flight Deals spreadsheet.'''
        sheety_edit_row_req_body = {
            "price": {
                "iataCode": iataCode
            }
        }
        sheety_post_res = requests.put(url=f'{self.endpoint}/{id}', json=sheety_edit_row_req_body, headers=self.headers)
        sheety_post_res.raise_for_status()

