import re
import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# get access to environment variables
load_dotenv()

## HELPER FUNCTIONS
def get_user_date() -> str:
    '''Creates an input prompt that asks what year the user would like to travel to in YYYY-MM-DD format. Returns the data from the input.'''
    date = input("Enter a date to travel back in time and create a playlist with the 100 most played songs of the week.\nDate must be in format YYYY-MM-DD.\n")
    return date

def validate_date(date) -> bool:
    '''Validades a string date, checking if it's in the expected format (YYYY-MM-DD) and if it's in the range from August 4, 1958 to yesterday'''
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


## RUN PROGRAM
# Get a valid date from the user
valid_date = False
while not valid_date:
    date = get_user_date()
    valid_date = validate_date(date)
        
# Scrape the top 100 song titles on that date, and the respective artists, into a Python List using BeautifulSoup
song_titles_list = []
artists_list = []

res = requests.get('https://www.billboard.com/charts/hot-100/' + date)
soup = BeautifulSoup(res.text, 'html.parser')
songs = soup.select('li h3.c-title')
for title in songs:
    song_titles_list.append(title.get_text().strip())
    artist = title.find_next_sibling()
    artists_list.append(artist.get_text().strip())


# Authenticate with Spotify using your unique Client ID/ Client Secret
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                            redirect_uri="http://localhost:8888/callback",
                                            client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                            client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                            show_dialog=True,
                                            cache_path="token.txt"))

user_id = sp.current_user()["id"]

# Create a list of Spotify song URIs for the list of song names that were found from by scraping billboard 100
song_uris = []
for song in song_titles_list:
    song_artist = artists_list[song_titles_list.index(song)].replace("Featuring", "")
    # refined search passing song name and artist
    search_result = sp.search(q=f"track:{song} artist:{song_artist}", type="track")
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # broad search passing only song name
        backup_search_result = sp.search(q=f"track:{song}", type="track")
        try:
            uri = backup_search_result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            # both searches failed
            print(f"{song} by {artists_list[song_titles_list.index(song)]} doesn't exist in Spotify. Skipped.")


# Create a new private playlist and add each of the songs to the new playlist
playlist_name = f'Billboard Hot 100 - {date}'
playlist_desc = f'Top songs in {date}, according to the Billboard Hot 100'
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False, description=playlist_desc)
sp.user_playlist_add_tracks(user=user_id, playlist_id=new_playlist["id"], tracks=song_uris)