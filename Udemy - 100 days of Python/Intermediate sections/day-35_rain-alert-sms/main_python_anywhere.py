import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import *
import smtplib

# Use PythonAnywhere to automate the Python Script
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# email sender
host = os.environ['MAIL_HOST']
sender_email = os.environ['SENDER_EMAIL']
sender_password = os.environ['SENDER_PASSWORD']
# email recipient
recipient_email = os.environ['RECIPIENT_EMAIL']

# Twilio authentication data
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
receiver_phone_nuber = os.environ['RECEIVER_PHONE_NUMBER']

# Open Weather Map API
api_key = os.environ['OWM_API_KEY']
my_lat = os.environ['LAT']
my_long = os.environ['LONG']
unit = 'metric'


# Retrieve weather data for a given location from the Open Weather API
request_data = requests.get(url=f"https://api.openweathermap.org/data/2.8/onecall?lat={my_lat}&lon={my_long}&exclude=current,minutely,daily&appid={api_key}&units={unit}")
request_data.raise_for_status()


# Check if it will rain in that location in the next 12 hours
# rain weather ids are all <600 and snow are the 6xx -> this implementation will include snow in the alert
twelve_hours_forecast = request_data.json()['hourly'][:12]
message = 'No need to bring an umbrella today. Check for more details on the next 12 hours forecast in your email.'
for hour in twelve_hours_forecast:
    if (hour['weather'][0]['id'] < 700):
        message = 'Keep yourself dry today. Bring an umbrella! Check for more details on the next 12 hours forecast in your email.'
        break
        

# Send SMS via the Twilio API
client = Client(account_sid, auth_token, http_client=proxy_client)
message = client.messages \
    .create(
        body= message,
        from_= twilio_phone_number,
        to= receiver_phone_nuber
    )
print(message.status)


# Send email with next 12 hours forecast
# email header
today = str(datetime.date(datetime.now()))

with open("./email_template.txt") as email_template:
    email_header = email_template.read()
with open("./output.txt", mode="w") as output:
    output.write(email_header.replace('[DATE]', today) + '\n\n')
     

# get information about each hour
with open("./hour_template.txt") as hour_template:
        hour_forecast = hour_template.read()

for hour in twelve_hours_forecast:
    # get hour from timestamp
    dt_hour = datetime.fromtimestamp(hour['dt']).hour
    # get all weather descriptions for the hour
    description = ",".join([hour['weather'][i]['description'] for i in range(len(hour['weather']))])

    curr_hour_forecast = hour_forecast.replace("[TIME]", str(dt_hour)).replace("[DESCRIPTION]", description).replace("[TEMP]", str(round(hour['temp'])) + '°C').replace("[FEELS_LIKE]", str(round(hour['feels_like'])) + '°C' + '\n\n')

    with open("./output.txt", mode="a") as output:
        output.write(curr_hour_forecast)
    

# send email message with final text in the output file
with open("./output.txt") as output: 
    email_message = output.read().encode('utf-8')
# create SMTP object to handle connection with email provider's SMTP email server
connection = smtplib.SMTP(host, port=587)
# secure connection
connection.starttls()
# login passing sender's authentication data 
connection.login(user=sender_email, password=sender_password)
connection.sendmail(from_addr=sender_email,
                 to_addrs= recipient_email,
                 msg=f'Subject:Next 12 hours forecast, {email_message}')
