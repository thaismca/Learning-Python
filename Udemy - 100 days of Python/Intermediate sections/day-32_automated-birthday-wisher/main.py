import smtplib
import datetime as dt
import pandas
from random import randint

NUMBER_OF_TEMPLATES = 3

# name of the remote host to which to connect
host = 'smtp.gmail.com'
# sender's authentication data
sender_email = 'thaismca.dev@gmail.com'
sender_password = 'hdnseixetwiyqtxl'

# create SMTP object to handle connection with email provider's SMTP email server
connection = smtplib.SMTP(host, port=587)
# secure connection
connection.starttls()
# login passing sender's authentication data
connection.login(user=sender_email, password=sender_password)


# get a reference for today's day and month into a tuple
now = dt.datetime.now()
today = (now.day, now.month)

# read data from birthdays.csv file
birthdays_df = pandas.read_csv('birthdays.csv')
birthdays_dict = {(row.day_of_birth, row.month_of_birth): {'email': row.email, 'name': row.nickname} for (index, row) in birthdays_df.iterrows()}


for birthdate in birthdays_dict:
    # check if the birthday matches today's date
    if birthdate == today:
        # reference to person's email and name
        recipient_name = birthdays_dict[birthdate]['name']
        recipient_email = birthdays_dict[birthdate]['email']
        # pick random template
        message_index = randint(1, NUMBER_OF_TEMPLATES)
        template_path = f'./message_templates/message_{message_index}.txt'
        # generate personalized message
        with open(template_path) as template:
            message_template = template.read()
            message_personalized = message_template.replace("[NAME]", recipient_name)
        
        #  send the message to the person's email address
        connection.sendmail(from_addr=sender_email,
                 to_addrs= recipient_email,
                 msg=f'Subject:Happy Birthday, {recipient_name}!\n\n{message_personalized}')