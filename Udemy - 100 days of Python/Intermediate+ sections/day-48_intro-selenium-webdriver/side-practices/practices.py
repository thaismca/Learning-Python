from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# setting up the selenium webdriver to work with Chrome using chromedriver
chromedriver_path = '/Users/thaismca/Development/Chromium/chromedriver'
service = Service(executable_path=chromedriver_path)
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

# # PRACTICE 1: automated price check on Amazon
# # open the product page using the webdriver
# driver.get('https://www.amazon.ca/Instant-Pot-Duo-Multi-Use-Programmable/dp/B00FLYWNYQ/ref=sr_1_3?crid=25ED8OV1FQ8DG&keywords=instant+pot&qid=1690073702&sprefix=instant+po%2Caps%2C154&sr=8-3')
# # get the price of the item using the class of the element
# price_by_class = driver.find_element(by=By.CLASS_NAME, value='a-offscreen')
# print(price_by_class.get_attribute('innerHTML'))
# # get the title of the first review of the item using XPath
# review_by_xpath = driver.find_element(by=By.XPATH, value='//*[@id="customer_review-R3RJ8LHFT5TTDG"]/div[2]/a/span[2]')
# print(review_by_xpath.text) 
# # quit the browser
# # close -> closes a tab, quit -> closes all tabs and quits the browser entirely
# driver.quit()



# # PRACTICE 2: upcoming events from python.org
# # open the python.org page using the webdriver
# driver.get('https://www.python.org/')
# # get the list of events using css selector
# events = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li')
# # loop through the list of events to create nested dictionary
# events_dict = {}
# for index, event in enumerate(events):
#     time = event.find_element(by=By.TAG_NAME, value='time').get_attribute('datetime').split('T')[0]
#     name = event.find_element(by=By.TAG_NAME, value='a').text
#     events_dict[index] = {'time': time, 'name': name}
# print(events_dict)
# # quit the browser
# # close -> closes a tab, quit -> closes all tabs and quits the browser entirely
# driver.quit()



# # PRACTICE 3: interacting with wikipedia
# # open the python.org page using the webdriver
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# # find the link with the number of articles in english and print that number
# articles_number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(articles_number.text)
# # find the link to the Content Portals and click it to open the page
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # need to workaround an annoying popup that is being displayed before clicking the Content Portals link
# annoying_popup = driver.find_element(By.CSS_SELECTOR, ".frb-close")
# annoying_popup.click()
# content_portals.click() 
# # find the searchbar inside of the Contents Page Intro and type a subject to be searched
# search = driver.find_element(By.CSS_SELECTOR, ".contentsPage__intro input")
# search.send_keys("Ancient Egypt")
# # submit the search query
# search.send_keys(Keys.ENTER)



# PRACTICE 4: interacting with forms
# open the App Brewery form page example using the webdriver
driver.get('https://secure-retreat-92358.herokuapp.com/')
# find each of the inputs in the form and fill them with some testing data
# first name
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Tony")
# last name -> find inout and send keys all in one line
driver.find_element(By.NAME, "lName").send_keys("Stark")
# email
driver.find_element(By.NAME, "email").send_keys("iamironman@avengers.com")
# find the submit button and click it
driver.find_element(By.CSS_SELECTOR, "form button").click()
