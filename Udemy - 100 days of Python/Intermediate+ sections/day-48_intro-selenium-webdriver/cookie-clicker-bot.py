from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

# get access to environment variables
load_dotenv()

# setting up the selenium webdriver to work with Chrome using chromedriver
chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
service = Service(executable_path=chromedriver_path)
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

# open the game page
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# set timers
five_minutes_lap = (time.time() + 60*5)
five_seconds_lap = (time.time() + 5)

# get a reference to the cookie element
cookie = driver.find_element(By.ID, "cookie")
# get a reference to the store elements
store_items_container_div = driver.find_elements(By.CSS_SELECTOR, "#store div")
# create a list containing the ids of the items in the store
store_items_ids = [item.get_attribute("id") for item in store_items_container_div]
    
# start loop
while True:
    # keep clicking the cookie for as long as the loop is active
    cookie.click()

    # every 5 seconds
    if time.time() > five_seconds_lap:
        # create a list with the current cost of all upgrades
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        store_items_costs = [int(item.text.split("-")[1].strip().replace(",", "")) for item in store_items if item.text != ""]
        
        # create a dictionary correlating each store item id with the respective price
        all_upgrades = {}
        for n in range(len(store_items_costs)):
            all_upgrades[store_items_ids[n]] = store_items_costs[n]

        # check the current amount of money
        money = int(driver.find_element(By.ID, "money").text)
        # check which items can be purchased with the current amount of money
        affordable_items = {k:v for k,v in all_upgrades.items() if money >= v}
        
        # only if there are any items that can be purchased
        if affordable_items:
            # get a refence to the id of the most expensive of the available items
            most_expensive_available_id = max(affordable_items, key=all_upgrades.get)
            print(most_expensive_available_id)
            # click the element which id corresponds to the most expensive and available item
            driver.find_element(By.ID, most_expensive_available_id).click()
        
        # update the five seconds lap tracker
        five_seconds_lap += 5
    
    # when the 5min mark is reached
    if time.time() > five_minutes_lap:
        # print the current number of the cookies per second
        cookies_per_second = driver.find_element(By.ID, "cps").text
        print(cookies_per_second)
        # end the loop
        break
    
    time.sleep(0.1)

