# Amazon Price Alert

This project implements a program that automatically sends a email alert when the price of a given product at Amazon goes below a preset value.

This project was implemented as part of the day 47 of the course 100 days of Python. This lesson had no videos to explain the solution step by step.

## Key differences from course final solution

#### Environment variables

This implementation keeps all environment variables in a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.

#### requirements.txt file

In order to ensure that all developers working on a project are using the same virtual environment we use a *requirements.txt* file. This is essentially a list of the Python packages that are required to be installed inside a virtual environment for the associated application to run successfully.
## Project set up

After you clone this repository, you will need to:

- replace placeholder values in the .env file with valid ones
- define the product you want to track and the price limit in the *main.py* file


### Environment Variables

In order to run this program, you must replace current placeholder values for the environment variables in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```


#### Personal protected data

| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `HOST` |  host running your SMTP server |
| `PORT` |  port where SMTP server is listening |
| `SENDER_EMAIL` | email address to login on the SMTP server |
| `PASSWORD` | password to login on the SMTP server |
| `RECIPIENT` | email address to send the alert to |


### Defining Product and Price Threshold

This program tracks prices for products available at Amazon. In order to track the price for a specific product, simply replace the current PRODUCT_URL and PRICE_THRESHOLD in the main.py file with the url of the product you want to track and the price limit you have in mind respectively.
## Running the program locally

All the external packages used in this project, along with their versions, are listed explicitly in *requirements.txt*. At this point, you could try and run the code using Python. If you have all packages  installed globally (ideally you won’t) then the script will quite possibly run successfully. However, even if this is the case you can’t be sure that the script is running in exactly the way that the repository author intended because you might be using different versions of each package to the versions specified in *requirements.txt*.

To ensure that you have an identical setup to the one where this project was intended to work, we use a virtual environment.

- First, create and activate a virtual environment. 
- Next, you need to install the Python packages listed in the *requirements.txt* file. You do this using the command *pip install -r requirements.txt*
- The program can now be executed by running the command *python3 main.py* in the project's directory

## Deploying to PythonAnywhere

Once you finish the project setup, you can deploy this project to PythonAnywhere so the script can run automatically at a given interval (ideally once a day).

Unfortunately, free accounts on PythonAnywhere can only access sites on their whitelist. So in order to be able to deploy this script to PythonAnywhere, **you must have a paid account**.

- upload main.py, requirements.txt and .env files to PythonAnywhere (these files must me all in the same folder)
- click to open the main.py file and open a bash console on that file directory
- install dependencies by running the command *pip install -r requirements.txt*
- The program can now be executed by running the command *python3 main.py*
- If you want this script to run automatically, you can schedule a task to run the command *python3 main.py* at a given frequency and time