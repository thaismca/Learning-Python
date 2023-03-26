# ISS OVERHEAD NOTIFIER
# This program notifies when the ISS is passing at a given latitude and longitude during nighttime
import requests
import datetime as dt

# latitude and longitude
MY_LAT = 49.282730
MY_LONG = -123.120735
LOCAL_UTC_OFFSET = -8

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

print(iss_lat)
print(iss_long)


# TODO: make a get request to Sunset and sunrise times API and get references to both sunrise and sunset data from the JSON file
# parameters object that will be passed to the get request made to Sunset and sunrise times API
parameters = {
    # latitude and longitude in decimal degrees. Both are required.
    "lat": MY_LAT,
    "lng": MY_LONG,
    # time formatter -> set to one so we can have it expressed following ISO 8601
    "formatted": 0
}

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

# TODO: generate a tuple for both sunrise and sunset times, containing the local hour and minutes for each one of them
def get_local_hour_minutes(time):
    '''Receives a time string expressed following ISO 8601 and returns a tuple containing the local hour and minutes.'''
    utc_hour = int(time.split("T")[1].split(":")[0])
    local_hour = utc_to_local(utc_hour)
    minutes = int(time.split("T")[1].split(":")[1])

    return(local_hour, minutes)


# make a get request to Sunset and sunrise times API
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
# raise exception if no success
response.raise_for_status()
# get a reference to the response data in JSON format
data = response.json()
# get references to both sunrise and sunset data from the JSON file
sunrise = get_local_hour_minutes(data["results"]["sunrise"])
sunset = get_local_hour_minutes(data["results"]["sunset"])

print(sunrise)
print(sunset)

# TODO: generate a tuple with the current hour and minutes
now = dt.datetime.now()
time_now = (now.hour, now.minute)

print(time_now)

# TODO: check if the current ISS is close to my location considering MY_LAT and MY_LONG, and if it's currently dark
# TODO: send an email to notify that ISS is currently overhead, if conditions above are met
# TODO: run this check repeatedly at a given interval