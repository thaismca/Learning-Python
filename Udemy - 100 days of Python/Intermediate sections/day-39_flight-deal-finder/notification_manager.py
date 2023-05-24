import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# Use PythonAnywhere to automate the Python Script
try:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
except:
    proxy_client = None

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_AUTH_TOKEN'), http_client=proxy_client)


    def send_sms(self, message):
        '''This function sends a message to a verified number using the Twilio API'''
        message = self.client.messages.create(
            body=message,
            from_=os.environ.get('TWILIO_PHONE_NUMBER'),
            to=os.environ.get('RECEIVER_PHONE_NUMBER'),
        )
        # Prints if successfully sent.
        print(message.sid)