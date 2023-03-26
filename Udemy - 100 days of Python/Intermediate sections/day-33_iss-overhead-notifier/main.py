# ISS OVERHEAD NOTIFIER
# This program notifies when the ISS is passing at a given latitude and longitude during nighttime

# latitude and longitude
MY_LAT = 49.282730
MY_LONG = -123.120735
LOCAL_UTC_OFFSET = -8

# TODO: make a get request to Sunset and sunrise times API and get references to both sunrise and sunset data from the JSON file
# TODO: convert both sunrise and sunset to local time, considering the LOCAL_UTC_OFFSET
# TODO: generate a tuple for both sunrise and sunset times, containing the local hour and minutes for each one of them
# TODO: generate a tuple with the current hour and minutes
# TODO: make a request to the ISS current location API and get references to the current ISS coordinates
# TODO: check if the current ISS is close to my location considering MY_LAT and MY_LONG, and if it's currently dark
# TODO: send an email to notify that ISS is currently overhead, if conditions above are met
# TODO: run this check repeatedly at a given interval