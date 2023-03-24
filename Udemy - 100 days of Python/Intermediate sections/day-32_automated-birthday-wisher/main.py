import smtplib
import datetime as dt
import pandas

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



# get a reference for today's day and month into a tuple
now = dt.datetime.now()
today = (now.day, now.month)

# read data from birthdays.csv file
birthdays_df = pandas.read_csv('birthdays.csv')
birthdays_dict = {(row.day_of_birth, row.month_of_birth): {'email': row.email, 'name': row.nickname} for (index, row) in birthdays_df.iterrows()}

for birthdate in birthdays_dict:
    # check if the birthday matches today's date
    if birthdate == today:
        print(birthdays_dict[birthdate])




# TODO: pick random template and generate personalized message
# if that date check returns true, pick a randon letter template and replace the [NAME] with the person's nickname from birthdays.csv

# TODO: send the message to the person's email address
# create SMTP object to handle connection with email provider's SMTP email server
# secure connection
# login passing sender's authentication data
# send email message