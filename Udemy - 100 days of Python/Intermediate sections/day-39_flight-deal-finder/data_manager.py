import requests
import os

SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_REQ_HEADERS = {
            "Authorization": "Basic " + os.environ.get('SHEETY_AUTH'),
        }

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_prices_sheet_data(self):
        '''This function retrieves and returns all data from the Flight Deals spreadsheet.'''    
        sheety_res = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_REQ_HEADERS)
        sheety_res.raise_for_status()
        
        return sheety_res.json()['prices']

    
    def update_iata_code(self, id, iataCode):
        '''This function updates the IATA code at a given row (id) in the Flight Deals spreadsheet.'''
        sheety_edit_row_req_body = {
            "price": {
                "iataCode": iataCode
            }
        }
        sheety_post_res = requests.put(url=f'{SHEETY_ENDPOINT}/{id}', json=sheety_edit_row_req_body, headers=SHEETY_REQ_HEADERS)
        sheety_post_res.raise_for_status()

