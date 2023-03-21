# ----- FLASH CARD APP ----- #

# -------------------- CONSTANTS -------------------- #
# -- BACKGROUNDS
BG_COLOR = '#B1DDC6'
CARD_FRONT_IMG = './images/card_front.png'
CARD_BACK_IMG = './images/card_back.png'
RIGHT_BUTTON_IMG = './images/right.png'
WRONG_BUTTON_IMG = './images/wrong.png'

# -- FONTS
LANGUAGE_LABEL_FONT = ('Arial', 30, 'italic')
WORD_LABEL_FONT = ('Arial', 60, 'bold')

# -- DATA FILE
DATA_FILE = './data/french_words.csv'

# TODO: create new flash cards
from csv import DictReader
import random
# read from the csv file to dictionary
with open(DATA_FILE, mode='r', encoding='utf-8-sig') as data_file:
    words_dict = list(DictReader(data_file))


# create a card front with a random word in the first column
# generate a new card every time a right or wrong button is pressed
# show the front of the card whenever a new card is generated
def generate_card(dict_list):
    '''Receives a list of dictionaties, where each dictionary has a word in two different languages in the format
    {language1: word, language2:translation}. It selects a randon dictionary in the list and generates the front of a flash card.'''
    # select random word/translation dict
    selected = random.choice(dict_list)
    # get a reference to the name of the languages
    languages = [language for language in selected.keys()]
    # change card label text for current language
    card.itemconfig(current_language, text=languages[0])
    # change card label text for current language
    card.itemconfig(current_word, text=selected[languages[0]])



# -------------------- UI SETUP --------------------- #
# TODO: create UI using Tkinter
from tkinter import *
# create window
window = Tk()
window.title('Flash Card App')
window.config(bg=BG_COLOR, padx=50, pady=50)

# create card with bg image, one label for the language name, and one label for the word
card = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_front_bg = PhotoImage(file=CARD_FRONT_IMG)
card.create_image(400, 263, image=card_front_bg)
current_language = card.create_text(400, 150, text='Language', font=LANGUAGE_LABEL_FONT)
current_word = card.create_text(400, 263, text='Word', font=WORD_LABEL_FONT)
card.grid(row=0, column=0, columnspan=2)

# create the buttons for right and wrong answer
right_img = PhotoImage(file=RIGHT_BUTTON_IMG)
right_button = Button(image=right_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR, command= lambda: generate_card(words_dict))
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file=WRONG_BUTTON_IMG)
wrong_button = Button(image=wrong_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR)
wrong_button.grid(row=1, column=1)


window.mainloop()



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