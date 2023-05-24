from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# creating instances of the external classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# get data from spreadsheet
sheety_res_data = data_manager.get_prices_sheet_data()

try:
    for row in sheety_res_data:
        ## Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with IATA Codes for each city that doesn't have one
        iataCode = row["iataCode"] if row["iataCode"] != "" else flight_search.get_iata_code(row["city"])
        if row["iataCode"] == "":
            data_manager.update_iata_code(row["id"], iataCode)
        
        ## Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
        found_flight = flight_search.find_flights(iataCode, row["lowestPrice"])

        ## If search returned at least one result, send SMS to a verified phone number with the Twilio API
        if len(found_flight) > 0:
            final_message = 'Low price alert!\n'
            for flight in found_flight:
                ## The SMS should include the departure airport IATA code, destination airport IATA code, departure city, 
                ## destination city, flight price and flight dates.
                final_message += f'''\nOnly {flight_search.currency}{flight.price} to fly from {flight.departure_city}-{flight.departure_airport}
to {flight.destination_city}-{flight.destination_airport}, {flight.departure_date} to {flight.return_date}\n'''

            notification_manager.send_sms(final_message)
   
except KeyError:
    print('Spreadsheet data is corrupted. Cannot proceed with operation.')    


