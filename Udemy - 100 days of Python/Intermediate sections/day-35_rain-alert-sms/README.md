# Weather Alert

This project implements an automated weather alert, that sends a SMS notification saying if the person should bring an umbrella or if it's going to be dry, and also sends an email with detailed hourly forecast for the next 12 hours. 

**Practice goal:** learn more about API authentication and environment variables.


## Key differences from course solution

This project was implemented as part of the day 35 of the course 100 days of Python. All implementation of features covered in the course was taken care of prior to watch the solution videos. Also, this project implements some extra features.

#### SMS are always sent

The course solution only sends a SMS when it's going to rain or snow in the next 12 hours, to remind the person to bring an umbrella. I decided to send the message notifing the person about either rainy/snowy or dry weather, so if the person doesn't get any messages we can be sure that there's something wrong.

#### Reading environment variables from a .env file

In the course solution each environment variable was set separately in the command line, since the course still didn't cover the dotenv module. I did my research and added the environment variables to a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.

#### Detailed weather report sent to email

I added the functionality to send an email with a more detailed report on the weather for the next 12 hours so I could practice more with reading from template files, replacing data on these files, generating output files and sending emails.
## Environment Variables

In order to run this program, you must replace current placeholder values for the environment variables in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```



| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `TWILIO_ACCOUNT_SID` |  your Twilio account sid |
| `TWILIO_AUTH_TOKEN` |  your Twilio auth token |
| `TWILIO_PHONE_NUMBER` |  your Twilio phone number |
| `RECEIVER_PHONE_NUMBER` |  a phone number verified on Twilio |
| `LAT` |  your latitude |
| `LONG` |  your longitude |
| `OWM_API_KEY` |  your Open Weather Map API key |
| `MAIL_HOST` |  your email host (i.e. smtp.gmail.com) |
| `SENDER_EMAIL` |  your sender email |
| `SENDER_PASSWORD` |  your sender password |
| `RECIPIENT_EMAIL` |  a receipient email |

### Notes

`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` are obtained by signing up to Twilio. This is a paid service, but you don't need to provide payment information upfront. You get an amount of trail credits that can be used to get this program running.

`RECEIVER_PHONE_NUMBER` must be a number that was already verified on Twilio. It can be the same number that you used to sign up for an account, for instance. You can check your current list of verified numbers in your Twilio Console (Phone Numbers -> Manage -> Verified Caller IDs). There, you will also be able to add more numbers to that list, as log as you are able to check the validation code you will receive on that number.

`LAT` and `LONG` will be used to get the weather for the location under these coordinates. If you don't know this information, you can access https://www.latlong.net/, type the address/city and get the corresponding coordinates.

`OWM_API_KEY` is obtained by signing up to Open Weather Map. The free subscription is enough to get this program running.

`MAIL_HOST` is obtained from your email provider. For instance, the Gmail host is gmail.smtp.com.

`SENDER_EMAIL` and `SENDER_PASSWORD` are the authentication data that you use to log in to your email account. Note that, is you use Gmail you won't be able to make this program run by using your regular password. You will need to generate a App Password. More details here: https://support.google.com/accounts/answer/185833?hl=en

`RECIPIENT_EMAIL` can be any valid email address that you want to send the weather report to. It can be the same as the sender, if you want to send an email to yourself.
## Installation and usage

There are two files in this project that will serve different purposes. If you want to run the script locally in your machine, use the *main.py file*. If you want to schedule a task in PythonAnywhere, use the *main_python_anywhere.py* file.

The only difference between these two files is how the requests to Twilio are being handled, since the Twilio API client needs to be told how to connect to the proxy server that free accounts use to access the external Internet. More details here: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

In both cases, you must sign up at Open Weather Map and Twilio, for some environment variables are related to mandatory keys/tokens/ids to use these APIs.

### External accounts
#### Required
- Sign up to Open Weather Map to genereate an API key (can use the free account).
- Sign up to Twilio and generate an account SID, auth token and Twilio phone number (can use trial credits).
#### Optional
- Sign up to PythonAnywhere, if you want to deploy this project in the cloud and schedule a task to send you a weather notification every day.

### Local execution
- clone this repository
- replace values for the environment variables in the .env file
- install dependencies
  - Twilio: https://www.twilio.com/docs/sms/quickstart/python
  - dotenv: *pip install python-dotenv*
- open the console on the main.py file directory
- execute main.py by running the command *python3 main.py*

### PythonAnywhere
- clone this repository
- replace values for the environment variables in the .env file
- upload main_python_anywhere.py, email_template.txt, hour_template.txt and .env files to PythonAnywhere (these files must me all in the same folder)
- click to open the main_python_anywhere.py file and open a bash console on that file directory
- install dotenv dependency by running the command *pip install python-dotenv*
- execute main_python_anywhere.py by running the command *python3 main_python_anywhere.py*
- if you want this script to run every morning, schedule task to run the *main_python_anywhere.py* file in PythonAnywhere

