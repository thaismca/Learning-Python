import re
import datetime as dt
# Create an input prompt that asks what year the user would like to travel to in YYYY-MM-DD format
def get_user_date():
    date = input("Enter a date to travel back in time and create a playlist with the 100 most played songs of the week.\nDate must be in format YYYY-MM-DD.\n")
    return date

def validate_date(date):
    valid_pattern = "^\d{4}-\d{2}-\d{2}$"
    # validate date format
    if not re.match(valid_pattern, date):
        print("Date must be in format YYYY-MM-DD.\n")
        return False
    else:
        # validate date
        try: 
            date_to_datetime = dt.datetime.strptime(date, '%Y-%m-%d').date()
        except:
            print("Invalid date!\n")
            return False

        # validate date from Aug 4, 1958 to yesterday
        today = dt.datetime.now().date()
        if date_to_datetime >= today:
            print("Must be a date in the past!\n")
            return False

        elif dt.datetime(1958, 8, 4).date() > date_to_datetime:
            print("Cannot be a date before August 4, 1958!\n")
            return False
    
    return True

valid_date = False
while not valid_date:
    date = get_user_date()
    valid_date = validate_date(date)

        
# Scrape the top 100 song titles on that date into a Python List using BeautifulSoup
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.billboard.com/charts/hot-100/' + date)
soup = BeautifulSoup(res.text, 'html.parser')
songs = soup.select('li h3.c-title')
song_titles_list = [title.get_text().strip() for title in songs]
print(song_titles_list)

# Authenticate with Spotify using your unique Client ID/ Client Secret

# Create a list of Spotify song URIs for the list of song names that were found from by scraping billboard 100
# Create a new private playlist and each of the songs to the new playlist