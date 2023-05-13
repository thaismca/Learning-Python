import os
import requests
from datetime import datetime, timedelta

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# endpoints
STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# company data
STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"

# dates
yesterday = (datetime.now() - timedelta(1)).date()
day_before_yesterday = (datetime.now() - timedelta(2)).date()

## STEP 1: Use http://api.marketstack.com/v1/eod
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# fetch API data
params_stock = {
    "symbols": STOCK_SYMBOL,
    "access_key": os.environ["STOCKS_API_KEY"],
    'date_from': day_before_yesterday,
    'date_to': yesterday
}
res = requests.get(STOCK_ENDPOINT, params=params_stock)
res.raise_for_status()
stock_data = res.json()["data"]

# get closing price for yesterday and the day before yesterday
yesterday_close = stock_data[0]["close"]
day_before_close = stock_data[1]["close"]

# check if the difference between yesterday and the day before yesterday is greater that 5%
if abs(yesterday_close - day_before_close) > abs(day_before_close * 0.05):
    print("get news")






## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

