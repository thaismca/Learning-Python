
# Cookie Clicker bot player

This project implements a bot that automatically interacts with the Cookie Clicker game.

This project was implemented as part of the day 48 of the course 100 days of Python. This lesson had no videos to explain the solution step by step.

## What this program does
This program implements a bot using Selenium Webdriver, to interact with a web-based Cookie Clicker game.

- When the program is executed, it will automatically open a Chrome window in the computer and navigate to the game's webpage (https://orteil.dashnet.org/experiments/cookie/).
- As soon as the game is loaded, the bot will start to click the cookie.
- Every 5 seconds, the bot will check the current amount of money and which of the upgrades are currently available to be purchased with that amount, and click to purchase the most expensive one that it can.
- After 5 minutes have passed since starting the game, the bot will stop clicking the cookie and print out the "cookie/second" rate in the console.

### Project goal 
- Familiarize with Selenium Webdriver
- Learn how Python can be used to interact automatically with webpages
- Practice using Python for automation purposes

## Key differences from course final solution
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

## Running the program locally

All the external packages used in this project, along with their versions, are listed explicitly in *requirements.txt*. At this point, you could try and run the code using Python. If you have all packages  installed globally (ideally you won’t) then the script will quite possibly run successfully. However, even if this is the case you can’t be sure that the script is running in exactly the way that the repository author intended because you might be using different versions of each package to the versions specified in *requirements.txt*.

To ensure that you have an identical setup to the one where this project was intended to work, we use a virtual environment.

- First, create and activate a virtual environment. 
- Next, you need to install the Python packages listed in the *requirements.txt* file. You do this using the command *pip install -r requirements.txt*
- The program can now be executed by running the command *python3 cookie-clicker-bot.py* in the project's directory
