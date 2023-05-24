import os
from twilio.rest import Client

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))


    def send_sms(self, message):
        '''This function sends a message to a verified number using the Twilio API'''
        message = self.client.messages.create(
            body=message,
            from_=os.environ.get('TWILIO_PHONE_NUMBER'),
            to=os.environ.get('RECEIVER_PHONE_NUMBER'),
        )
        # Prints if successfully sent.
        print(message.sid)