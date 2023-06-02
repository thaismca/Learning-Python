# Billboard Hot 100 Spotify Playlist

This project implements a program that automatically geneartes a new Spotify playlist for an user by scrapping the list of the Top 100 songs at a given week, based on a date entered by the user.

This project was implemented as part of the day 46 of the course 100 days of Python. This lesson had no videos to explain the solution step by step.

## Key differences from course final solution

#### Date validation

The course solutions does not validate the date entered by the user. In this implementation, the program asks for the date and validates its format and chcks if it's within the acceptable range (from August 04, 1958 to yesterday). It keeps asking the user to input the date again, if the validation fails. The program will only continue with further execution after user enters a valid date.

#### Scrapping both the song and the respective artist

The course solution only scrapes the song name from the Billboard website, and uses the year of the date entered by the user to try and filter the song version. Problem is that the accuracy is not ideal (for instance, some really old Christmas songs come back to the Top 100 almost every year). In this implementation, I added the ability to scrape the artist name for each of the songs in the list. This was a bit challenging, since there were no unique css selectors that could be used in order to select this data. The only way to get the respective artist for each song was selecting the first sibling for each h3 element that represented a song name.

#### Refined and broad serches for tracks

In this implementation, the artist name was also used to make a more refined search for a given song in Spotify. If the song could not be found by passing the artist name in the refining criteria, another attempt is done to search only for the song name.

#### Environment variables

This implementation keeps all environment variables in a .env file. This makes thigs easier if someone else wants to use this program (they only need to fill the .env with the proper data once), or if I want to run it from another computer or cloud service.

#### requirements.txt file

In order to ensure that all developers working on a project are using the same virtual environment we use a *requirements.txt* file. This is essentially a list of the Python packages that are required to be installed inside a virtual environment for the associated application to run successfully.
## Project set up

After you clone this repository, you will need to:

- set up your account with Spotify
- go to the developer dashboard and create a new Spotify App
- copy the Client ID and Client Secret into the .env file

### Environment Variables

In order to run this program, you must replace current placeholder values for the environment variables in the .env file with valid ones.

All variables must be in the following format:
```NAME_OF_THE_VARIABLE=value_of_the_variable```


#### Personal protected data

| Variable   |  Description                           |
| :---------- |  :---------------------------------- |
| `SPOTIFY_CLIENT_ID` |  your Spotify Client ID |
| `SPOTIFY_CLIENT_SECRET` |  your Spotify Client Secret |


Both `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` are obtained by signing up and creating an app in Spotify.


### Authentication with Spotify

**1.** In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

**2.** Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/

**3.** Once you've created a Spotify app, copy the Client ID and Client Secret into the .env file of your clone of this Python project.
## Running the project and creating a playlist

Once you finish the environment variables setup, you can execute the main.py file to create a new playlist.

- The program will first ask user to enter a date in the format *YYYY-MM-DD*. This is the date that will be used to get the list of the Top 100 songs for that week from the Billboard website.

    For instance, let's say the user enters the date *2000-08-02*. The program will make a request to the Billboard Hot 100 passing this date in the URL: *https://www.billboard.com/charts/hot-100/2000-08-12*.
    
    The program will then use *BeautifulSoup* to scrape the name of each song and the respective artist from the list of songs displayed in the webpage.

    **DATE VALIDATION**: The program expects a date that is between *August 04, 1958* and yesterday, and the format must be exactly *YYYY-MM-DD*. If user enters a date that is not within the expected range and/or it's not in the expected format, the user will be prompted to enter a new date until the date entered passes all the validations.

- After user enters a valid date, the program will try and authenticate with Spotify, using the *Client ID* and *Client Secret* from the *.env* file.

    If this is the first time that the program is being executed, a tab will be open in the default browser, so user can confirm the Spotify sign in. In order to proceed, user must click the *Accept* button when this tab opens.

    If authentication is successful, a *token.txt* file will be added to the project's directory. If the program is executed again and the token is still valid, this confirmation in the browser won't be required. It will only be required again after the token expires, or if the *token.txt* file is deleted or corrupted.

- Upon a successful authentication, the program will go through the list of songs that were scrapped from the Billboard Top 100, search for each one of them in Spotify and add the URI for the ones that can be found in a list of URIs.

    First, the program will try to search for the song using both the song title and the artist that were listed in the Billboard website. If no song can be found using both criteria, it will try and serach using only the song title.

    In some cases, the song won't be found in Spotify at all, therefore it will be skipped.

- Once program finishes the process of getting the list of tracks URIs, a new private playlist will be created for the authenticated user, and the list of URIs will be used to populate that plylist with the respective tracks.

    The playlist will be named *Billboard Hot 100 - {date entered by user}*.

- After program finishes it execution, the user can open the Spotify app and see the new Playlist in the Library.
