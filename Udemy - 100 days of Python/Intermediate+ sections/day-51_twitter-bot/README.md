
# Twitter Bots

This project implements bots that automatically interacts with Twitter.

This project was implemented as part of the day 51 of the course 100 days of Python. This lesson had no videos to explain the solution step by step, and only the internet speed complaint bot was part of the course scope.

Two bots were implemented within the scope of this project:

- Internet speed complaint
- Daily weather alert

## What this project implements
This project implements two bot using Selenium Webdriver, to interact with Twitter and post a tweet.

### Internet speed complaint

- When the program is executed, the bot will automatically open a Chrome window in the computer and navigate to the Speedtest webpage (https://speedtest.net/).
- As soon as the page is loaded, the bot will click to start the speed test.
- After 60 seconds, the bot will get the information about both download and upload speeds.
- If any of these speeds is below the minimun set in the PROMISSED_UP and PROMISSED_DOWN constants, the bot will open Twitter, log into the bot's account and post a tweet complaining about the internet speed, mentioning the provider that is set in the PROVIDER_TAG constant.

### Daily weather alert

- When the program is executed, it will request data from the Open Weather Map API on the daily weather for the location set in the LAT and LONG constants.
- The prgram will get the data return from the API to compose a tweet with the the daily weather summary, minimum and maximum temperatures.
- The bot will open Twitter, log into the bot's account and post the tweet.

### Project goal 
- Familiarize with Selenium Webdriver
- Learn how Python can be used to interact automatically with webpages
- Practice using Python for automation purposes

## Key differences from course final solution
### Course scope
Only the internet speed complaint bot was part of the course scope.

### Selenium Webdriver version
This section of the course was recorded using a previous version of the Selenium Webdriver, so not everything was working the same way as described during the tutorials of the side practices. Some extra research was required in order to work with the current version.

### Environment variables
This implementation keeps all environment variables in a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.

### requirements.txt file
In order to ensure that all developers working on a project are using the same virtual environment we use a requirements.txt file. This is essentially a list of the Python packages that are required to be installed inside a virtual environment for the associated application to run successfully.

## Requirements
To be able to run this project, you must have Chrome and chromedriver installed in your machine.

## Project set up

After you clone this repository, you will need to:

- go to https://chromedriver.chromium.org/downloads and download the version of chomedriver that is compatible with your version of chrome
- once the download is completed, extract the file to a folder in your computer
- copy the path for the chromedriver file in your computer and paste it to replace placeholder value in the .env file with a valid one

### .ENV FILE 

In order to run this program, you must replace current placeholder values in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```

#### All bots
| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `CHROMEDRIVER_PATH` |  path of the chromedriver in your machine |
| `TWITTER_USER` |  your bot's Twitter username |
| `TWITTER_PASSWORD` |  your bot's Twitter password |

#### Daily Weather Alert 
| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `LAT` |  your latitude |
| `LONG` |  your longitude |
| `OWM_API_KEY` |  your Open Weather Map API key |
| `LOCATION_NAME` |  your location name to compose the tweet |

#### Daily Weather Alert 
| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `PROMISSED_UP` |  your provider's promissed upload speed |
| `PROMISSED_DOWN` |  your provider's promissed download speed |
| `PROVEIDER_TAG` |  your internet provider tag on Twitter |


## Running the program locally

All the external packages used in this project, along with their versions, are listed explicitly in *requirements.txt*. At this point, you could try and run the code using Python. If you have all packages  installed globally (ideally you won’t) then the script will quite possibly run successfully. However, even if this is the case you can’t be sure that the script is running in exactly the way that the repository author intended because you might be using different versions of each package to the versions specified in *requirements.txt*.

To ensure that you have an identical setup to the one where this project was intended to work, we use a virtual environment.

- First, create and activate a virtual environment. 
- Next, you need to install the Python packages listed in the *requirements.txt* file. You do this using the command *pip install -r requirements.txt*
- The programs can now be executed by running the proper command for each bot: 
    - Internet speed complaint: *python3 ./internet-speed/main.py*
    - Daily weather alert: *python3 ./internet-speed/main.py*


