import requests

# TODOS:
# Retrieve weather data for a given location from the Open Weather API
api_key = "a099ba2c15bd323e64db8198dd5febdb"
my_lat = 49.282730
my_long = -123.120735

request_data = requests.get(url=f"https://api.openweathermap.org/data/2.8/onecall?lat={my_lat}&lon={my_long}&exclude=current,minutely,daily&appid={api_key}")
request_data.raise_for_status()

# Check if it will rain in that location in the next 12 hours
# rain weather ids are all <600 and snow are the 6xx -> this implementation will include snow in the alert
twelve_hours_forecast = request_data.json()['hourly'][:12]
for hour in twelve_hours_forecast:
    if (hour['weather'][0]['id'] < 700):
        print('Bring an umbrella')
        break

# Send SMS via the Twilio API
# Use PythonAnywhere to automate the Python Script
# Hide API Keys -> Environment Variables