import smtplib
import datetime as dt

# # name of the remote host to which to connect
# host = 'smtp.gmail.com'
# # sender's authentication data
# sender_email = 'thaismca.dev@gmail.com'
# sender_password = 'hdnseixetwiyqtxl'
# # recipient
# recipient_email = 'thaismca.bio@gmail.com'

# # create SMTP object to handle connection with email provider's SMTP email server
# connection = smtplib.SMTP(host, port=587)
# # secure connection
# connection.starttls()
# # login passing sender's authentication data
# connection.login(user=sender_email, password=sender_password)
# # send email message
# connection.sendmail(from_addr=sender_email,
#                     to_addrs= recipient_email,
#                     msg='Subject:Hello\n\nEmail message body here.')


# TODO: check if today matches a birthday in the birthdays.csv
# get a reference for today's day and month into a tuple
# read data from birthdays.csv file
# for each entry in the file, get a reference for day_of_birth and month_of_birth into a tuple and check agains today's date tuple

# TODO: pick random template and generate personalized message
# if that date check returns true, pick a randon letter template and replace the [NAME] with the person's nickname from birthdays.csv

# TODO: send the message to the person's email address
# create SMTP object to handle connection with email provider's SMTP email server
# secure connection
# login passing sender's authentication data
# send email message