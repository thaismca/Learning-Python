import requests
import os
from twilio.rest import Client

# NOTE: fake values must be replaced with valid ones -> fake ones are put in here for security reasons

# twilio authentication data
account_sid = "fake_sid"
auth_token = "fake_token"
twilio_phone_number = "fake_twilio_number"
receiver_phone_nuber = "fake_receiver_number"

# TODOS:
# Retrieve weather data for a given location from the Open Weather API
api_key = "fake_api_key"
my_lat = 49.282730
my_long = -123.120735

request_data = requests.get(url=f"https://api.openweathermap.org/data/2.8/onecall?lat={my_lat}&lon={my_long}&exclude=current,minutely,daily&appid={api_key}")
request_data.raise_for_status()

# Check if it will rain in that location in the next 12 hours
# rain weather ids are all <600 and snow are the 6xx -> this implementation will include snow in the alert
twelve_hours_forecast = request_data.json()['hourly'][:12]
for hour in twelve_hours_forecast:
    if (hour['weather'][0]['id'] < 700):
        # Send SMS via the Twilio API
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="Keep yourself dry today. Bring an umbrella!",
                     from_= twilio_phone_number,
                     to= receiver_phone_nuber
                 )
        print(message.status)
        break


# Use PythonAnywhere to automate the Python Script
# Hide API Keys -> Environment Variables