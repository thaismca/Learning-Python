
# ISS OVERHEAD NOTIFICATION

The code implements an automated email sender that sends a notification to a list of recipients when the ISS is passing at a given latitude and longitude range during nighttime.

Implemented as part of the capstone project from day 33 of the course *100 days of Python*. All implementation was taken care of prior to watch the solution videos.

Note: all sensitive data were changed to a fake placeholder, just for the sake of sharing this code more safely on GitHub. Code was verified as working with real testing data, and can be used by replacing this data with valid ones.
## Key differences from course solution

 - Course solution work with hard coded values for the latitude and longitude ranges when checking if the ISS is overhead. This implementation calculates those ranges based on the MY_LAT, MY_LONG and VISIBILTY_RANGE constants, making it easier to make changes to customize the location.

 - Course solution only work with UTC time zone, since they don't convert the time received in the response from the Sunset and sunrise times API. This implementation converts all times to local, depending on the value of the constant LOCAL_UTC_OFFSET, aloowing for easy customization.
 
 - Course solution sends several emails, one for each time the loop runs and it's night time and ISS is within the visibility range. In this implementation, once the first email is sent, the loop won't run again, so no more than one email per night can be sent to each person in the list.
## Implementation notes

**CONSTANTS**

 - MY_LAT -> float that represents the latitude of the main reference point
 - MY_LONG -> float that represents the longitude of the main reference point
 - LOCAL_UTC_OFFSET -> integer that represents the local utc offset
 - VISIBILITY_RANGE -> float that represents the visibility range, considering the main reference point
 - MAX_LAT, MIN_LAT, MAX_LONG, MIN_LONG -> floats that represent max and min for latitude and longitude, automatically calculated considering MY_LAT, MY_LONG and VISIBILITY_RANGE

 - HOST, PORT -> email sender data required to estabilish a SMTP connection
 - SENDER_EMAIL, PASSWORD -> sender's authentication data
 - RECIPIENTS = list of email addresses to send the notification

-------

**FUNCTIONS TO CHECK CONDITIONS TO SEND NOTIFICATION**

 - is_iss_overhead(iss_location): Receives a tuple with ISS current latitude and longitude and returns true if the current ISS location is within the VISIBILITY_RANGE, considering MY_LAT and MY_LONG as point of reference. It returns false if the ISS current location is not within this range.

 - is_dark(curr_time, sunrise, sunset): Receives the current hour, the sunrise hour and the sunset hour, and checks if current time is within the time frame between the hour after the sunset and the hour before the sunrise.


-------
**FUNCTIONS TO GET THE LOCAL HOUR FROM API RESPONSE**

 - utc_to_local(utc_hour): Receives an integer that represents the UTC hour and converts it to the local hour, considering the LOCAL_UTC_OFFSET.

 - get_local_hour(time): Receives a time string expressed following ISO 8601 (the format of the response from the Sunrise and sunset times API) and returns and integer that represents the local hour.


-------
**FUNCTION TO GET THE CURRENT ISS LOCATION**

- get_iss_position(): Makes a request to the ISS current location API and returns a tuple with the current ISS latiitude and longitude.

-------
**GET LOCAL SUNRISE AND SUNSET TIMES**

This part of the code handles the get request to Sunset and sunrise times API, and get references to both sunrise and sunset data from the JSON file, converted to local time.

The parameters object that will be passed to the get request made to Sunset and sunrise times API contains the required parameters of latitude and longitude (passing MY_LAT and MY_LONG constants), and the optional time formatter set to 0 so we can have time expressed following ISO 8601.


-------
**CHECK CONDITIONS - SEND NOTIFICATION**

This part of the code handles the check of the conditions and email sending.

The check is ran repeatedly at a given interval (initially set to 60 seconds).

- Every 60 seconds:
	- get a reference to the current hour using datetime library;
	- check if it's currently dark passing the current hour and the sunrise/sunset hours retrieved from the Sunrise and sunset times API;
	- if both conditions are true, estabilish a SMTP connection with the host, authenticate using sender's login data and send an email to each address in the recipients list notifying them that the ISS is currently overhead;
	- once one email is sent, break from loop.

