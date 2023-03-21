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

# -- SETTINGS
FLIP_DELAY = 3000


# ----------------- GLOBAL VARIABLES ---------------- #
words_to_learn = []
selected_card = {}
languages = []


# ----------------- READ APP DATA ------------------ #
def read_app_data():
    from csv import DictReader
    # read from the csv file to dictionary
    with open(DATA_FILE, mode='r', encoding='utf-8-sig') as data_file:
        global words_to_learn
        global languages
        words_to_learn = list(DictReader(data_file))
        # get a reference to the name of the languages
        languages = [language for language in words_to_learn[0].keys()]
    

# -------------- GENERATE / FLIP CARDS -------------- #
import random
# TODO: create new flash cards
# create a card front with a random word in the first column
# generate a new card every time a right or wrong button is pressed
# show the front of the card whenever a new card is generated
def generate_card(dict_list):
    '''Receives a list of dictionaties, where each dictionary has a word in two different languages in the format
    {language1: word, language2:translation}. It selects a random dictionary in the list and generates the front of a flash card.
    Calls flip_card to show the back of the card after the amount of time defined in the FLIP_DELAY constant.'''
    try:
        # try to cancel a previous delay, if there is one
        window.after_cancel(flip)
    except:
        pass
    # select random word/translation dict
    global selected_card
    global languages
    selected_card = random.choice(dict_list)
    # change card label text for current language
    card.itemconfig(card_language, text=languages[0], fill='#000')
    # change card label text for current language
    card.itemconfig(card_word, text=selected_card[languages[0]], fill='#000')
    # change card background image
    card.itemconfig(card_bg, image=card_front_bg)
    # disable buttons so they cannot be clicked while the front of the card is being displayed
    right_button.config(state='disabled')
    wrong_button.config(state='disabled')

    flip = window.after(FLIP_DELAY, func= lambda: flip_card(selected_card))



# TODO: after a delay of n seconds, flip the card to display the back with the translation
# change card bg image
# change card language label
# change card word label
# change both labels fg color
def flip_card(selected_card):
    '''Shows the back of a flash card. Called by generate_card after some amount of time defined in the FLIP_DELAY constant.'''
    # change card label text for current language
    card.itemconfig(card_language, text=languages[1], fill='#FFF')
    # change card label text for current language
    card.itemconfig(card_word, text=selected_card[languages[1]], fill='#FFF')
    # change card backgroud image
    card.itemconfig(card_bg, image=card_back_bg)
    # enable buttons so they can be clicked while back of the card is being displayed
    right_button.config(state='normal')
    wrong_button.config(state='normal')


# -------------------- UI SETUP --------------------- #
# TODO: create UI using Tkinter
from tkinter import *
# create window
window = Tk()
window.title('Flash Card App')
window.config(bg=BG_COLOR, padx=50, pady=50)

# read app data
read_app_data()

# create card with bg image, one label for the language name, and one label for the word
card = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_front_bg = PhotoImage(file=CARD_FRONT_IMG)
card_back_bg = PhotoImage(file=CARD_BACK_IMG)
card_bg = card.create_image(400, 263, image=card_front_bg)
card_language = card.create_text(400, 150, text='Language', font=LANGUAGE_LABEL_FONT)
card_word = card.create_text(400, 263, text='Word', font=WORD_LABEL_FONT)
card.grid(row=0, column=0, columnspan=2)

# create the buttons for right and wrong answer
right_img = PhotoImage(file=RIGHT_BUTTON_IMG)
right_button = Button(image=right_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR, command= lambda: generate_card(words_to_learn))
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file=WRONG_BUTTON_IMG)
wrong_button = Button(image=wrong_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR, command= lambda: generate_card(words_to_learn))
wrong_button.grid(row=1, column=1)

# generate first card
generate_card(words_to_learn)

window.mainloop()



# TODO: save progress
# remove word from list of words that might come up, if right button is pressed
# save filtered list of words in a words_to_learn.csv file

# TODO: check for progress when open the app
# when the app is launched, check if there's a words_to_learn.csv and retrieve the list and read from this csv file to dataframe
# if no words_to_learn.csv file exists, open the file with all the words