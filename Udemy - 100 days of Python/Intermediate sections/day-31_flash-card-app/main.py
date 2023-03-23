# ----- FLASH CARD APP ----- #
from tkinter import *
from tkinter import messagebox
import csv
import os
import random

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

# -- SETTINGS
FLIP_DELAY = 4000
LANGUAGES_TO_PRACTICE = ['French', 'Portuguese', 'Spanish']


# ----------------- GLOBAL VARIABLES ---------------- #
all_words_file = ''
saved_progress_file = ''
words_to_learn = []
selected_card = {}
current_languages = []


# ----------------- CHOOSE LANGUAGE ------------------ #
def choose_language_pop_up(root):
    '''Displays a pop up where the user can select a language to practice.'''
    # pop up
    pop_up = Toplevel(root)
    pop_up.attributes('-topmost', True)
    pop_up.focus_force()
    # label and options menu
    Label(pop_up, text="Choose language to practice").grid(row=0, column=0)
    language_selected = StringVar()
    language_menu = OptionMenu(pop_up, variable=language_selected, value='')
    
    #populate language options
    menu = language_menu['menu'] 
    for language in LANGUAGES_TO_PRACTICE:
        menu.add_command(label=language, command=lambda lang=language: language_selected.set(lang))
    # language selected by default
    language_selected.set(LANGUAGES_TO_PRACTICE[0])
    language_menu.grid(row=1, column=0)
    
    # button that calls set_language passing the selected language when clicked
    Button(pop_up, text='OK', command= lambda: set_language(language_selected.get(), pop_up)).grid(row=2, column=0)



def set_language(language, pop_up):
    '''Sets the path to reach the program files for the language that was selected and calls star_app to read
    either saved or base data from the corresponding language.'''
    # tap into the global variables for saved base file paths
    global all_words_file
    global saved_progress_file

    # set the paths according to the selected language
    all_words_file = f'./data/{language.lower()}/all_words.csv'
    saved_progress_file = f'./data/{language.lower()}/words_to_know.csv'

    # close pop up and start_app
    pop_up.destroy()
    start_app()



# ------------------ READ APP DATA ------------------- #
def start_app():
    '''Reads data from a save or base file and initializes words_to_learn and languages globals.
    Calls restart_words if there are no words to learn, or generate_card to show the first card if there are words to learn.
    Displays an error message if no file can be found.'''
    # tap into the global variables for words to learn and languages
    global words_to_learn
    global current_languages
    try:
        # check for progress when open the app
        # try to read from the save file to dictionary
        with open(saved_progress_file, mode='r', encoding='utf-8-sig') as data_file:
            words_to_learn = list(csv.DictReader(data_file))
    except:
        try:
            # try to read from a base data csv file with all the words to dictionary
            with open(all_words_file, mode='r', encoding='utf-8-sig') as data_file:
                words_to_learn = list(csv.DictReader(data_file))
        except:
            # no file to load data from was found -> program data corrupted
            messagebox.showerror(title='Error', message='There was an issue loading the program data.\nPlease contact support.')
            window.destroy()

    # force focus on the main window of the application 
    window.focus_force()
    # no data in words_to_learn   
    if len(words_to_learn) <= 0:
        restart_words()
    # at least one entry in words_to_learn
    else:
        # get a reference to the name of the languages
        current_languages = [language for language in words_to_learn[0].keys()]
        generate_card()



# ------------------ SAVE PROGRESS ------------------ #
def is_known_word():
    '''Removes current selected card from the list of words to know before rendering the next card.
    Called when the user clicks the right_button.'''
    # tap into the global variables for list of words to learn and selected card
    global words_to_learn
    global selected_card
    # remove the value that corresponds to the selected card from the list of words to learn
    words_to_learn.remove(selected_card)
    # generate next card 
    generate_card()



def save_progress_on_close():
    '''Saves the current list of words to know to a save file and closes the app. Called when the user clicks to close the app'''
     # tap into the global variables for list of words to learn and languages
    global words_to_learn
    global current_languages
    try:
        # save data to a save file csv
        with open(saved_progress_file, 'w', newline='', encoding='utf-8-sig') as save_file:
            save_data = csv.DictWriter(save_file, fieldnames=[current_languages[0], current_languages[1]])
            save_data.writeheader()
            save_data.writerows(words_to_learn)
    except:
        # no language selected
        pass

    # close window
    window.destroy()



def restart_words():
    '''Notifies the user that there's no new words to learn in the saved progress, and asks if they want to restart.'''
    # show messabox asking if user wants to restart
    restart = messagebox.askyesno(title='You nailed it!', message='There are no new words to learn. Restart list to practice more?')
    # yes
    if restart:
        try:
            # delete save file with user's progress
            os.remove(saved_progress_file)
        except:
            # no save file -> to cover when user checked all words in the first go and don't generate a save before trigerring restart
            pass
        # call start_app to load the app again and read from the base file, since save no longer exists
        start_app()
    # no
    else:
        # notification to let user know that the app is being closed, since there are no further possible actions
        messagebox.showinfo(title='Game Over', message='Thanks for playing!\nThis app will be now closed.')
        # update the save and close the app
        save_progress_on_close()



# -------------- GENERATE / FLIP CARDS -------------- #
def generate_card():
    '''It selects a random dictionary in the list of words_to_know and generates the front of a flash card.
    Calls flip_card to show the back of the card after the amount of time defined in the FLIP_DELAY constant.'''
    try:
        # try to cancel a previous delay, if there is one
        window.after_cancel(flip)
    except:
        pass

    # tap into the global variables for list of words to learn, selected card and languages
    global words_to_learn
    global selected_card
    global current_languages
    # check if there are no more words to learn
    if len(words_to_learn) <= 0:
        restart_words()
    # there are still words to learn
    else:
        # get a random dict from the list and assign it to the global selected_card
        selected_card = random.choice(words_to_learn)
        # change card_language text with the first language in the languages list
        card.itemconfig(card_language, text=current_languages[0], fill='#000')
        # change card_word text to the value in selected_card at the key that corresponds to the first language in the languages list
        card.itemconfig(card_word, text=selected_card[current_languages[0]], fill='#000')
        # change card background image
        card.itemconfig(card_bg, image=card_front_bg)
        # disable buttons so they cannot be clicked while the front of the card is being displayed
        right_button.config(state='disabled')
        wrong_button.config(state='disabled')

        #after a delay of FLIP_DELAY miliseconds, flip the card to display the back with the translation
        flip = window.after(FLIP_DELAY, func=flip_card)



def flip_card():
    '''Shows the back of a flash card for the current selected card.
    Called by generate_card after some amount of time defined in the FLIP_DELAY constant.'''
    # tap into the global variables for selected card and languages
    global selected_card
    global current_languages
    # change card_language text with the second language in the languages list
    card.itemconfig(card_language, text=current_languages[1], fill='#FFF')
    # change card_word text to the value in selected_card at the key that corresponds to the second language in the languages list
    card.itemconfig(card_word, text=selected_card[current_languages[1]], fill='#FFF')
    # change card backgroud image
    card.itemconfig(card_bg, image=card_back_bg)
    # enable buttons so they can be clicked while back of the card is being displayed
    right_button.config(state='normal')
    wrong_button.config(state='normal')



# -------------------- UI SETUP --------------------- #
#create UI using Tkinter
# create window
window = Tk()
window.title('Flash Card App')
window.config(bg=BG_COLOR, padx=50, pady=50)

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
right_button = Button(image=right_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR, command=is_known_word, state='disabled')
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file=WRONG_BUTTON_IMG)
wrong_button = Button(image=wrong_img, highlightthickness=0, relief=FLAT, bg=BG_COLOR, command=generate_card, state='disabled')
wrong_button.grid(row=1, column=1)

# save progress on close
window.protocol("WM_DELETE_WINDOW", save_progress_on_close)

# ----- ON PROGRAM START -> show pop up to select language
choose_language_pop_up(window)

window.mainloop()