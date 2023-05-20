# Workout Tracking using Google Sheets

This project implements a program that runs in the terminal an can be used to add data to a workout tracker in Google Sheets.

This project was implemented as part of the day 37 of the course 100 days of Python. This lesson had no videos to explain the solution. The challenge was to create a program that would receive a query and add the workout data to the spreadsheet. 

I implemented a program where the user can perform two different actions:

- add a workout to their spreadsheet
- manage their personal settings (gender, weight, height and age)

The user settings are saved in a json file, and are retrieved to be sent in the request that is made to the Nutritionix API, when the user adds a workout.

Besides, the user can perform more than one action every program execution. It also validates user inputs and API responses, and allows user to try again if anything goes wrong, no need to execute the program again.

Another difference is that this implementation keeps all environment variables in a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.

## How to use it

After you clone this repository, before you run it, you will need to set up your Google Spreadsheet and the Environment Variables in the .env file.

### Google Spreadsheet

This program adds workout data to a Google Spreadsheet that follows the same structure as the one in [this link](https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit#gid=0). So the first thing the new user needs to do is to visit the link and create a copy of the *My Workouts Spreadsheet*. You may need to login/register.


### External APIs
This program makes HTTP requests to two different APIs:
- Nutritionix: https://www.nutritionix.com/business/api
- Sheety: https://sheety.co/

In order to run this program, user must set the environment variables in the .env file using the credential obtained from both APIs.

#### Setup Nutritionix API Credentials 
- Go to the Nutritionix API website and select "Get Your API Key" to sign up for a free account. Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email. Once logged in, you should be able to access your API key and App id.
- Update the environment variables with the ***NUTRITIONIX_APP_ID*** and ***NUTRITIONIX_API_KEY*** that you got from Nutritionix.

#### Setup Your Google Sheet with Sheety
- Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1). Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again. Under your Google Account Security settings, you should see that Sheety has access. Double-check that you see Sheety listed as an authorized app. Otherwise, your Python code can't access your spreadsheet.
- In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
- Click on the workouts API endpoint and enable GET and POST.
- Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it. 
- Update the environment variable ***SHEETY_AUTH*** with either the token or the base64 string that is generated from you authentication input data that you got from Sheety. NOTE: no need to add the "Basic", only the string after it. 

## How it works

Once you finish the project setup, you can execute the main.py file in your terminal.

It will prompt you to choose one of the following actions:

    1- Add workout
    2- Manage personal settings

You can type the number corresponding to the action you want to perform. If you type anything other than 1 or 2, the program you keep prompting you until you select a valid option.

### Add workout
To add a workout, simply type the activity that you've done using natural language. The program will pass this query in the body of the request that will be made to the Nutritionix API. If there are no exercise in your query, you will be prompted to try again.

The data returned from the request will be used to make a follow-up request to the Sheety API, so the data can be registered in your workout tracking spredsheet.

- Your query can include multiple activities, and each one will be added in a separate row in the spreadsheet.
- If your query has a distance, but it does not include a duration, the duration will be estimated.
- If your query has no distance nor duration, the duration will default to 30 minutes.
- Calories will be estimated considering the type of activity, the duration and your personal settings for gender, weight, height and age.
- The date and time for the activity that are saved to the spreadsheet will correspond to the current date and time when the workout is being added.

### Manage personal settings
This options allows you to manage your personal settings for the following:
- gender
- weight (kg)
- height (cm)
- age
This data is all saved to a json file in this project directory *settings.json*. If this file is corrupted or cannot be found in the directory during program execution, the values for these settings will default to the following:
- gender: male
- weight (kg): 85
- height (cm): 180
- age: 30

#### Program being executed
![add workout](https://github.com/thaismca/Python-Practices/blob/279e0a7e1cfb6c0c889226fefe6853c8c57a4808/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-38_workout-tracker/add_workout.PNG?raw='true')

![manage settings](https://github.com/thaismca/Python-Practices/blob/279e0a7e1cfb6c0c889226fefe6853c8c57a4808/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-38_workout-tracker/manage_settings.PNG?raw='true')

#### Data saved to spreadsheet
![spreadsheet](https://github.com/thaismca/Python-Practices/blob/3780738efcfca90d790fb475389fba5b160b867a/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-38_workout-tracker/spreadsheet_data.PNG?raw='true')



