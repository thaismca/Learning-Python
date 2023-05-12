import requests
import os
from twilio.rest import Client

# Hide sensitive insformation -> Environment Variables
# twilio authentication data
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
receiver_phone_nuber = os.environ['RECEIVER_PHONE_NUMBER']

# Retrieve weather data for a given location from the Open Weather API
api_key = os.environ['OWM_API_KEY']
my_lat = os.environ['LAT']
my_long = os.environ['LONG']

request_data = requests.get(url=f"https://api.openweathermap.org/data/2.8/onecall?lat={my_lat}&lon={my_long}&exclude=current,minutely,daily&appid={api_key}")
request_data.raise_for_status()

# Check if it will rain in that location in the next 12 hours
# rain weather ids are all <600 and snow are the 6xx -> this implementation will include snow in the alert
twelve_hours_forecast = request_data.json()['hourly'][:12]
message = 'No need to bring an umbrella today.'
for hour in twelve_hours_forecast:
    if (hour['weather'][0]['id'] < 700):
        message = 'Keep yourself dry today. Bring an umbrella!'
        break
        

# Send SMS via the Twilio API
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
        body= message,
        from_= twilio_phone_number,
        to= receiver_phone_nuber
    )
print(message.status)

