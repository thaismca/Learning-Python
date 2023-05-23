import requests
import os

SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_prices_sheet_data(self):
    # get data from spreadsheet
        sheety_req_headers = {
            "Authorization": "Basic " + os.environ.get('SHEETY_AUTH'),
        }
        sheety_get_rows_endpoint= SHEETY_ENDPOINT
                        
        sheety_res = requests.get(url=sheety_get_rows_endpoint, headers=sheety_req_headers)
        sheety_res.raise_for_status()
        return sheety_res.json()['prices']
