class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure_airport, departure_city, destination_airport, destination_city, price, departure_date, return_date ):
        self.departure_airport = departure_airport
        self.departure_city = departure_city
        self.destination_airport = destination_airport
        self.destination_city = destination_city
        self.price = price
        self.departure_date = departure_date
        self.return_date = return_date 