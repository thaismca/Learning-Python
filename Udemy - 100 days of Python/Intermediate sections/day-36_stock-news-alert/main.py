import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

# companies to check
from my_settings import stocks_list, alert_threshold

# retrieving hiden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()

# endpoints
STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Twilio API data
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
receiver_phone_nuber = os.environ['RECEIVER_PHONE_NUMBER']

if(datetime.now().weekday() == 0 or datetime.now().weekday() == 6):
    pass

else:
    # dates
    yesterday = (datetime.now() - timedelta(1)).date()
    day_before_yesterday = (datetime.now() - timedelta(4 if datetime.now().weekday() == 1 else 2)).date()

    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then fetch the first 3 articles for the COMPANY_NAME.
    # fetch data from stocks API
    params_stock = {
        "symbols": ",".join([item['symbol'] for item in stocks_list]),
        "access_key": os.environ["STOCKS_API_KEY"],
        'date_from': day_before_yesterday,
        'date_to': yesterday
    }
    res = requests.get(STOCK_ENDPOINT, params=params_stock)
    res.raise_for_status()
    stock_data = res.json()["data"]

    # this API returns data all separately -> group data for each company
    stock_data_processed = []
    for company in stocks_list:
        stock_data_processed.append([item for item in stock_data if item['symbol'] == company['symbol']])

    for stock in stock_data_processed:
        # get closing price for yesterday and the day before yesterday
        yesterday_close = stock[0]["close"]
        day_before_close = stock[1]["close"]

        # check if the difference between yesterday and the day before yesterday is greater that 5%
        if abs(yesterday_close - day_before_close) > abs(day_before_close * (alert_threshold/100)):
        # fetch data from news API
            params_news = {
                "qInTitle": next(item['company'] for item in stocks_list if item['symbol'] == stock[0]['symbol']) ,
                "apiKey": os.environ["NEWS_API_KEY"],
            }
        
            res = requests.get(NEWS_ENDPOINT, params=params_news)
            res.raise_for_status()
            news_data = res.json()['articles'][:3]

            # Send a separate message with each article's title and description to your phone number.
            # Send SMS via the Twilio API
            percentage_diff = (abs(yesterday_close - day_before_close)/day_before_close) * 100.
            arrow = '🔺' if yesterday_close > day_before_close else '🔻'

            for news in news_data:
                text = f"{stock[0]['symbol']}: {arrow}{percentage_diff:.2f}%\nHeadline: {news['title']}\nBrief: {news['description']}"

                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                    body= text,
                    from_= twilio_phone_number,
                    to= receiver_phone_nuber
                )
                print(message.status) 
        

