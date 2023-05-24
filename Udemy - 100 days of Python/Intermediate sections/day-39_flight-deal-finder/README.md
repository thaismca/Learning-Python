# Flight Deal Finder

This project implements a program that run daily checks for flights to pre-defined destinations that are cheaper than the user's cut-off price. It sends an SMS to the user if it can find flights in the next six months that match the destination and price criteria.

This project was implemented as part of the days 39 and 40 of the course 100 days of Python. This lesson had no videos to explain the solution step by step.

## Key differences from course final solution

#### Get only the cheap flights from the Tequila Flight Search API

The course solutions does the check for the cut-off price after the travel search API returs the data for all flights from the origin to a given destination. By using this approach, a large amount of unecessary data is transferred over the network, consuming more bandwidth and taking more time. My implementation passes the cut-off price in the request body as one of the parameters, so the response only contains the flights that match the max price criteria. This significantly reduces the amount of data that is transferred and the time that the request takes to be fulfilled.

#### Send SMS with all flights that meet the search criteria

Also, the course solution only sends a message with the first flight that matches the search criteria, and discards all the other possibilities. My implementation generates a message containing all the flights that matches the criteria, and sends all in one SMS, to avoid overcharges that can happen if multiple messages are sent.

#### Environment Variables in .env file

Another difference is that this implementation keeps all environment variables in a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service. In this .env file, the user can not only add their protected data for API keys and tokens, but they can also inform the personalized settings for their own search criteria.

#### Account for spreadsheet with corrupted data

If user messes up with keys and data in the spreadsheet, this version will not simply crash. It will print a message in the logs to let user know about the issue instead. 

## How to use it

After you clone this repository, you will need to:

- set up your Google Spreadsheet
- set up your accounts on the external APIs
- set the Environment Variables in the .env file
- upload the project to PythonAnywhere
- schedule a task to execute the main.py script once every day

### Google Spreadsheet

This program pulls destinations and tickets cut-off prices data from a Google Spreadsheet that follows the same structure as the one in [this link](https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit#gid=0). So the first thing the new user needs to do is to visit the link and create a copy of the *Flight Deals*. You may need to login/register.


### External APIs
This program makes HTTP requests to the following APIs:
- Google Sheet Data Management - https://sheety.co/

- Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

- Twilio SMS API - https://www.twilio.com/docs/sms

In order to run this program, user must set the environment variables in the .env file using the credential obtained from all these APIs.

#### Setup Your Google Sheet with Sheety
- Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1). Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again. Under your Google Account Security settings, you should see that Sheety has access. Double-check that you see Sheety listed as an authorized app. Otherwise, your Python code can't access your spreadsheet.
- In your project page, click on "New Project" and create a new project in Sheety with the name "Flight Deals Finder" and paste in the URL of your own "Flight Deals" Google Sheet.
- Click on the *prices* API endpoint and enable GET and PUT.
- Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it. 
- Update the environment variable ***SHEETY_AUTH*** with either the token or the base64 string that is generated from you authentication input data that you got from Sheety. NOTE: no need to add the "Basic", only the string after it. 

#### Register with the Kiwi Partners Flight Search API
- Follow the steps to create an account. There is no need to provide a credit card or billing information.
- After you confirm your email and log into your account, click the *My solutions* option in the left-side menu, then click to create a *New solution*.
- Choose Meta Search as your product type, then choose One-Way and Return.
- If the website prompts you for the type of partnership you can either choose "Book with Kiwi.com" or the affiliate program. Both should work for this project.
- Once this is done, you can click on the name of your new solution to manage it. Here you have access to your ***AffilID*** and ***API Key***.

#### Sign up to use the Twilio API
- Sign up to Twilio (https://www.twilio.com/en-us) and generate your account SID, auth token and Twilio phone number.
- You can use your trial credits to run and test this application.
### Environment Variables

In order to run this program, you must replace current placeholder values for the environment variables in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```


#### Personal protected data

| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `SHEETY_ENDPOINT` |  your personalized endpoint for the Sheety API |
| `SHEETY_AUTH` |  token or the base64 string to authenticate at Sheety |
| `TEQUILA_API_KEY` | your key to the Tequila Flight Search API |
| `TWILIO_ACCOUNT_SID` |  your Twilio account sid |
| `TWILIO_AUTH_TOKEN` |  your Twilio auth token |
| `TWILIO_PHONE_NUMBER` |  your Twilio phone number |
| `RECEIVER_PHONE_NUMBER` |  a phone number verified on Twilio |

#### Personal search criteria

| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `ORIGIN` |  IATA code for city of departure |
| `MIN_STAY` |  min number of days at the destination |
| `MAX_STAY` | max number of days at destination |
| `CURRENCY` |  currency that you want to work with |


### Notes

`SHEETY_ENDPOINT` and `SHEETY_AUTH` are obtained by signing up and linking your spreadsheet to the Sheety API (https://sheety.co/). The free tier is enough to get this program running.

`TEQUILA_API_KEY` is obtained by signing up to the Tequila Flight Search API (https://tequila.kiwi.com/portal/docs/tequila_api). The free tier is enough to get this program running.

`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` are obtained by signing up to Twilio. This is a paid service, but you don't need to provide payment information upfront. You get an amount of trail credits that can be used to get this program running.

`RECEIVER_PHONE_NUMBER` must be a number that was already verified on Twilio. It can be the same number that you used to sign up for an account, for instance. You can check your current list of verified numbers in your Twilio Console (Phone Numbers -> Manage -> Verified Caller IDs). There, you will also be able to add more numbers to that list, as log as you are able to check the validation code you will receive on that number.
## Deploying to PythonAnywhere

Once you finish the environment variables setup, you can deploy this project to PythonAnywhere.

- upload main.py, data_manager.py, flight_data.py, flight_search.py, notification_manager.py and .env files to PythonAnywhere (these files must me all in the same folder)
- click to open the main.py file and open a bash console on that file directory
- install dotenv dependency by running the command _pip install python-dotenv_

The program can now be executed by running the command _python3 main.py_

If you want this script to run automatically, you can schedule a task to run the command _python3 main.py_ at a given frequency and time in PythonAnywhere.