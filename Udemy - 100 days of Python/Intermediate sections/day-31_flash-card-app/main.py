# ----- FLASH CARD APP ----- #

# TODO: create UI using Tkinter
# create window
# create card with bg image, one label for the language name, and one label for the word
# create the buttons for right and wrong answer

# TODO: create new flash cards
# read from the csv file to dataframe
# create a card front with a random word in the first column
# create a card back with the respective translation for that word
# show the front of the card whenever a new card is generated
# generate a new card every time a right or wrong button is pressed

# TODO: after a delay of n seconds, flip the card to display the back with the translation
# change card bg image
# change card language label
# change card word label
# change both labels fg color

# TODO: save progress
# remove word from list of words that might come up, if right button is pressed
# save filtered list of words in a words_to_learn.csv file

# TODO: check for progress when open the app
# when the app is launched, check if there's a words_to_learn.csv and retrieve the list and read from this csv file to dataframe
# if no words_to_learn.csv file exists, open the file with all the words