# Stock Trading News Alert

This project implements an automated stock trading news alert, that sends a SMS notification with the latest news headlines related to companies that user is tracking, if the company's stock closing price increases/decreases by a significant amount.

**Practice goal:** work with different APIs


## Key differences from course solution

This project was implemented as part of the day 36 of the course 100 days of Python. All implementation of features covered in the course was taken care of prior to watch the solution videos. Also, this project implements some extra features.

#### Using Market Stack API

This implementation gets stocks data from a different API, since the one suggested in the course is more limited in terms of endpoints with free access. The endpoint used in the course was free at the time that the lesson was recorded, but that is no longer the case.

The *End-of-Day Data* endpoint in the Market Stack API is available for users in the free plan tier. Besides, it allows passing a date interval to narrow down the search, and it's possible to search data for multiple companies in the same request.

#### Covering for market closed on weekends

In the course solution, the market being closed on weekends is not being taken into account.

This means that the code implemented in the course will break if the user tries to execute it from Sunday to Tuesday. This implementation checks for the current weekday and does not run the API requests on Sundays and Mondays. Also, when executed on Tuesdays, it will consider the last Friday as "day before yesterday".

#### Can follow multiple stocks

The course solution runs a check for only one hard-coded stock symbol.

This implementation can check data for multiple companies. All the user needs to do is to add a new dictionary to the *stocks_list* in the *my_settings.py* file, using the following format:

`{"symbol": "STOCK_SYMBOL",  "company": "COMPANY_NAME"}`

#### Can set a different alert threshold

The percentage that triggers the alert is hard-coded in the course solution.

In this implementation, the user can set this percentage by changing the value for *alert_threshold* in the *my_settings.py* file. By default, the alert is triggered when there's a increase or decrease in the stock prices that is greater than 5%.

#### Reading environment variables from a .env file

In the course solution each environment variable was set separately in the command line, since the course still didn't cover the dotenv module. I did my research and added the environment variables to a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.
## Personalized Settings

The user can set a list of companies to track the closing prices for their stocks, and also the alert threshold. Both are set by editing the *my_settings.py* file.

#### stocks_list

The *stocks_list* represents a list of companies that are being tracked. Each item in this list must be a dictionary in the following format:

`{"symbol": "STOCK_SYMBOL", "company": "COMPANY_NAME"}`

`STOCK_SYMBOL` is an abbreviation used to uniquely identify publicly traded shares of a particular stock on a particular stock market. You can check a list of all stock ticker symbols here: https://stockanalysis.com/stocks/

`COMPANY_NAME` is the name of the company, that will be used in the query to search for news about that company.

#### alert_threshold

The *alert_threshold* is a number that represents the percentage that triggers the alert. For instance, if the *alert_threshold* is set to 5, then the alert will be sent if the closing price for stocks at a given company increased or decreased by at least 5% in the last two days.
## Environment Variables

In order to run this program, you must replace current placeholder values for the environment variables in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```



| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `NEWS_API_KEY` |  your key for the News API |
| `STOCKS_API_KEY` |  your key for the Market Stack API |
| `TWILIO_ACCOUNT_SID` |  your Twilio account sid |
| `TWILIO_AUTH_TOKEN` |  your Twilio auth token |
| `TWILIO_PHONE_NUMBER` |  your Twilio phone number |
| `RECEIVER_PHONE_NUMBER` |  a phone number verified on Twilio |

### Notes

`NEWS_API_KEY` is obtained by signing up to the News API (https://newsapi.org/). The free subscription is enough to get this program running.

`STOCKS_API_KEY` is obtained by signing up to the Market Stack API (https://marketstack.com/). The free subscription is enough to get this program running.

`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` are obtained by signing up to Twilio. This is a paid service, but you don't need to provide payment information upfront. You get an amount of trail credits that can be used to get this program running.

`RECEIVER_PHONE_NUMBER` must be a number that was already verified on Twilio. It can be the same number that you used to sign up for an account, for instance. You can check your current list of verified numbers in your Twilio Console (Phone Numbers -> Manage -> Verified Caller IDs). There, you will also be able to add more numbers to that list, as log as you are able to check the validation code you will receive on that number.
## Installation and usage

There are two files in this project that will serve different purposes. If you want to run the script locally in your machine, use the *main.py file*. If you want to schedule a task in PythonAnywhere, use the *main_python_anywhere.py* file.

The only difference between these two files is how the requests to Twilio are being handled, since the Twilio API client needs to be told how to connect to the proxy server that free accounts use to access the external Internet. More details here: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

In both cases, you must sign up at News API, Market Stack and Twilio, for some environment variables are related to mandatory keys/tokens/ids to use these APIs.

### External accounts
#### Required
- Sign up to News API (https://newsapi.org/) to genereate an API key (can use the free account).
- Sign up to Market Stack API (https://marketstack.com/) to genereate an API key (can use the free account).
- Sign up to Twilio (https://www.twilio.com/en-us) and generate an account SID, auth token and Twilio phone number (can use trial credits).
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
- upload main_python_anywhere.py, my_settings.py and .env files to PythonAnywhere (these files must me all in the same folder)
- click to open the main_python_anywhere.py file and open a bash console on that file directory
- install dotenv dependency by running the command *pip install python-dotenv*
- execute main_python_anywhere.py by running the command *python3 main_python_anywhere.py*
- if you want this script to run every morning, schedule task to run the *main_python_anywhere.py* file in PythonAnywhere

