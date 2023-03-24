import smtplib
import datetime as dt
import random

# the following code sends an email with a random motivational quote for each one of the recipients in the list if the hour in the day is 18 (6PM)

# name of the remote host to which to connect
HOST = 'smtp.gmail.com'
# sender's authentication data -> changed for fake data just for the commit
SENDER_EMAIL = 'testing@gmail.com'
SENDER_PASSWORD = 'fakepassword'
# recipients -> changed for fake accounts just for the commit
RECIPIENT_EMAILS = ['test1@gmail.com', 'test2@test.com']

# create SMTP object to handle connection with email provider's SMTP email server
connection = smtplib.SMTP(HOST, port=587)
# secure connection
connection.starttls()
# login passing sender's authentication data
connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

for email in RECIPIENT_EMAILS:
    #read messages from file and pick a random one
    with open('quotes.txt', 'r', encoding='utf-8') as data_file:
        quotes = data_file.readlines()
        quote_of_the_day = random.choice(quotes)

    # send email message
    connection.sendmail(from_addr=SENDER_EMAIL,
                        to_addrs= email,
                        msg=f"Subject: Daily Motivation\n\n{quote_of_the_day}")