# ISS OVERHEAD NOTIFIER
# This program notifies when the ISS is passing at a given latitude and longitude during nighttime
import requests
import datetime as dt
import smtplib

# ------------------------------------ CONSTANTS ------------------------------------ #
# latitude and longitude
MY_LAT = 49.282730
MY_LONG = -123.120735
# local utc offset
LOCAL_UTC_OFFSET = -8
# ISS visibility range
VISIBILITY_RANGE = 5

# calculating max and min for latitude and longitude considering MY_LAT, MY_LONG and VISIBILITY_RANGE
MAX_LAT = MY_LAT + VISIBILITY_RANGE if MY_LAT + VISIBILITY_RANGE < 90 else (MY_LAT + VISIBILITY_RANGE - 90) - 90
MIN_LAT = MY_LAT - VISIBILITY_RANGE if MY_LAT - VISIBILITY_RANGE > -90 else (MY_LAT - VISIBILITY_RANGE + 90) + 90
MAX_LONG = MY_LONG + VISIBILITY_RANGE if MY_LONG + VISIBILITY_RANGE < 180 else (MY_LONG + VISIBILITY_RANGE - 180) -180
MIN_LONG = MY_LONG - VISIBILITY_RANGE if MY_LONG - VISIBILITY_RANGE > -180 else (MY_LONG - VISIBILITY_RANGE + 180) +180

# email notification -> fake data just for the commit (replace with actual data if you want to test)
HOST = "smtp.gmail.com"
PORT = 587
SENDER_EMAIL = "testing@gmail.com"
PASSWORD = "fakepassword"
RECIPIENTS = ["test1@gmail.com", "test2@gmail.com"]



# ---------------- FUNCTIONS TO CHECK CONDITIONS TO SEND NOTIFICATION --------------- #

# TODO: check if the current ISS is close to my location considering MY_LAT and MY_LONG, and if it's currently dark
def is_iss_overhead(iss_lat, iss_long):
    '''Receives ISS current latitude and longitude and returns true if the current ISS location is within the VISIBILITY_RANGE,
    considering MY_LAT and MY_LONG as point of reference. It returns false if the ISS current location is not within this range.'''
    if MIN_LAT <= iss_lat <= MAX_LAT and MIN_LONG <= iss_long <= MAX_LONG:
        return True
    else:
        return False



def is_dark(curr_time, sunrise, sunset):
    '''Checks if current time is within the time frame between the hour after the sunset and the hour before the sunrise.'''
    if sunset < curr_time < 23 or 0 < curr_time < sunrise:
        return True
    else:
        return False
        


# ------------------ FUNCTIONS GET THE LOCAL HOUR FROM API RESPONSE ----------------- #

# TODO: convert both sunrise and sunset to local time, considering the LOCAL_UTC_OFFSET
def utc_to_local(utc_hour):
    '''Converts an integer that represents the UTC hour to the local hour, considering the LOCAL_UTC_OFFSET.'''
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour



# TODO: get a reference to the hour for both sunrise and sunset times
def get_local_hour(time):
    '''Receives a time string expressed following ISO 8601 and returns a tuple containing the local hour and minutes.'''
    utc_hour = int(time.split("T")[1].split(":")[0])
    local_hour = utc_to_local(utc_hour)

    return local_hour



# ---------------------------------- API REQUESTS ----------------------------------- #

# TODO: make a request to the ISS current location API and get references to the current ISS coordinates
# make a get request to Sunset and sunrise times API
response = requests.get("http://api.open-notify.org/iss-now.json")
# raise exception if no success
response.raise_for_status()
# get a reference to the response data in JSON format
data = response.json()
# get references to ISS current latitude and longitude
iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])



# TODO: make a get request to Sunset and sunrise times API and get references to both sunrise and sunset data from the JSON file
# parameters object that will be passed to the get request made to Sunset and sunrise times API
parameters = {
    # latitude and longitude in decimal degrees. Both are required.
    "lat": MY_LAT,
    "lng": MY_LONG,
    # time formatter -> set to one so we can have it expressed following ISO 8601
    "formatted": 0
}

# make a get request to Sunset and sunrise times API
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
# raise exception if no success
response.raise_for_status()
# get a reference to the response data in JSON format
data = response.json()
# get references to both sunrise and sunset data from the JSON file
sunrise = get_local_hour(data["results"]["sunrise"])
sunset = get_local_hour(data["results"]["sunset"])



# ---------------------- CHECK CONDITIONS - SEND NOTIFICATION ----------------------- #

# TODO: get a reference to the current hour
now = dt.datetime.now()
time_now = now.hour

# TODO: send an email to notify that ISS is currently overhead, if conditions above are met
if is_dark() and is_iss_overhead():
    connection = smtplib.SMTP(HOST, PORT)
    connection.starttls()
    connection.login(SENDER_EMAIL, PASSWORD)

    for email in RECIPIENTS:
        connection.sendmail(from_addr=SENDER_EMAIL,
                 to_addrs= email,
                 msg=f'Subject:ISS Overhead Notification\n\nLook up! 👆\nThe ISS is above you in the sky!')
        
# TODO: run this check repeatedly at a given interval