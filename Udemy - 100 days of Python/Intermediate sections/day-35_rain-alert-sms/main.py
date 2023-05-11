import requests

# TODOS:
# Retrieve weather data for a given location from the Open Weather API
api_key = "a099ba2c15bd323e64db8198dd5febdb"
my_lat = 49.282730
my_long = -123.120735

request_data = requests.get(url=f"https://api.openweathermap.org/data/2.8/onecall?lat={my_lat}&lon={my_long}&appid={api_key}")
print(request_data.json())


# Check if it will rain in that location in the next 12 hours
# Send SMS via the Twilio API
# Use PythonAnywhere to automate the Python Script
# Hide API Keys -> Environment Variables