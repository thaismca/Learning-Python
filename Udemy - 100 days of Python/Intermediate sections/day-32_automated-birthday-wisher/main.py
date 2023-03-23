import smtplib

# name of the remote host to which to connect
host = 'smtp.gmail.com'
# sender's authentication data
sender_email = 'thaismca.dev@gmail.com'
sender_password = 'hdnseixetwiyqtxl'
# recipient
recipient_email = 'thaismca.bio@gmail.com'

# create SMTP object to handle connection with email provider's SMTP email server
connection = smtplib.SMTP(host, port=587)
# secure connection
connection.starttls()
# login passing sender's authentication data
connection.login(user=sender_email, password=sender_password)
# send email message
connection.sendmail(from_addr=sender_email,
                    to_addrs= recipient_email,
                    msg='Subject:Hello\n\nEmail message body here.')