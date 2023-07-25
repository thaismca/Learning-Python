from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# setting up the selenium webdriver to work with Chrome using chromedriver
chromedriver_path = '/Users/thaismca/Development/Chromium/chromedriver'
service = Service(executable_path=chromedriver_path)
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

# open the product page using the webdriver
driver.get('https://www.amazon.ca/Instant-Pot-Duo-Multi-Use-Programmable/dp/B00FLYWNYQ/ref=sr_1_3?crid=25ED8OV1FQ8DG&keywords=instant+pot&qid=1690073702&sprefix=instant+po%2Caps%2C154&sr=8-3')
# get the price of the item using the class of the element
price_by_class = driver.find_element(by=By.CLASS_NAME, value='a-offscreen')
print(price_by_class.get_attribute('innerHTML'))
# get the title of the first review of the item using XPath
review_by_xpath = driver.find_element(by=By.XPATH, value='//*[@id="customer_review-R3RJ8LHFT5TTDG"]/div[2]/a/span[2]')
print(review_by_xpath.text) 
# quit the browser
# close -> closes a tab, quit -> closes all tabs and quits the browser entirely
driver.quit()