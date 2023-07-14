# 1. Get the URL from product on Amazon that is going to have its price tracked.
# 2. Use the requests library to request the HTML page of the Amazon product using the URL from 1.
# It's going to be necessary to pass along some headers in order for the request to return the actual website HTML.
# At minimum "User-Agent" and "Accept-Language" values must go in the request header.
# 3. Use BeautifulSoup to make soup with the web page HTML that is returned in the request.
# Use the "lxml" parser instead of the "html.parser" for this to work.
# 4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
# 5. Set a threshold for the price of the item.
# 6. When the price is below the threshold, use the smtp module to send an email.
# In the email, include the title of the product, the current price and a link to buy the product.

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

# get access to environment variables
load_dotenv()

#-- PRODUCT DETAILS -> replace with any desired Amazon product URL and price threshold -----------------------------#
PRODUCT_URL = 'https://www.amazon.ca/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=zg_bs_g_electronics_sccl_4/133-4231630-2799038?psc=1'
PRICE_THRESHOLD = 190.00


#-- Use BeautifulSoup to Scrape the Product Price -----------------------------#
# request headers
HEADERS = {
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# request the HTML page and make soup with what is returned
res = requests.get(PRODUCT_URL, headers=HEADERS)
soup = BeautifulSoup(res.text, 'lxml')
# scrape the price as float
price = soup.find(class_="a-offscreen").get_text().split("$")[1]
price_float = float(price)


#-- Email Alert When Price Below Preset Value -----------------------------#
if price_float <= PRICE_THRESHOLD:
    # get hold of product's name
    product_name = soup.find(id="productTitle").get_text().strip()
    # create message
    message = f"{product_name} is now ${price}\n{PRODUCT_URL}"
    
    # send email to list of recipients
    connection = smtplib.SMTP(os.environ.get('HOST'), os.environ.get('PORT'))
    connection.starttls()
    connection.login(os.environ.get('SENDER_EMAIL'), os.environ.get('PASSWORD'))
    connection.sendmail(from_addr=os.environ.get('SENDER_EMAIL'),
                        to_addrs= os.environ.get('RECIPIENT'),
                        msg=f'Subject:Amazon Price Alert: {product_name}\n\n{message}')