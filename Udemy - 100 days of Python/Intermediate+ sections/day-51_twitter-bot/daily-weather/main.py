from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

# get access to environment variables
load_dotenv()
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')
TWITTER_USER = os.environ.get('TWITTER_USER')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
OWM_API_KEY = os.environ.get('OWM_API_KEY')
LAT = os.environ.get('LAT')
LON = os.environ.get('LON')
LOCATION_NAME = os.environ.get('LOCATION_NAME')

# today's date
date = datetime.today().strftime('%a, %b %-d %Y')

# get weather info
req_url = f'https://api.openweathermap.org/data/2.8/onecall?lat={LAT}&lon={LON}&exclude=currently,hourly,minutely&appid={OWM_API_KEY}&units=metric'
request_data = requests.get(url=req_url)
request_data.raise_for_status()

daily_forecast = request_data.json()['daily'][0]
summary = daily_forecast['summary']
min = daily_forecast['temp']['min']
max = daily_forecast['temp']['max']

tweet = f'Weather in {LOCATION_NAME} for {date}: {summary}. Min of {int(min)}°C. Max of {int(max)}°C.'

# setting up the selenium webdriver to work with Chrome using chromedriver
service = Service(executable_path=CHROMEDRIVER_PATH)
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# accessing twitter and posting
driver.get('https://www.twitter.com/')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
time.sleep(2)
driver.find_element(By.TAG_NAME, 'input').send_keys(TWITTER_USER + Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD + Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div').click()