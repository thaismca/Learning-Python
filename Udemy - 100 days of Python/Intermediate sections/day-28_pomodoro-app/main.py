from tkinter import *
from settings import *

# ------------------------------------ CONSTANTS ----------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BG_IMAGE = './Intermediate sections/day-28_pomodoro-app/tomato.png'

# ------------------------------------- SETTINGS ------------------------------------- #
settings = Settings()

# --------------------------------- GLOBAL VARIABLES --------------------------------- #
reps = 0
work_sessions_counter = ''
running_timer = None

# ---------------------------------- TIMER MECHANISM --------------------------------- #
def start_timer():
    '''This function starts a pomodoro timer, taking the session times from th eprogram constants work_min, short_break_min and long_break_min.
    It runs a certain number of work sessions, defined in work_sessions_block, before entering a long break.'''
    # disable the start and settings buttons, so they cannot be clicked when there's a timer running
    start_button.config(state='disabled')
    settings_button.config(state='disabled')
    # set different timer sessions and values -> based on app constants
    work_sec = settings.work_min * 60
    short_break_sec = settings.short_break_min * 60
    long_break_sec = settings.long_break_min * 60
    global reps
    reps += 1

    # reps matches a multiple of (work_sessions_block * 2) -> end of a block = long break
    if reps % (settings.work_sessions_block * 2) == 0:
        # start long break session timer and show "BREAK" label
        countdown(long_break_sec)
        session_label.config(text="BREAK", fg=RED)
    
    # reps does not match a multiple of (work_sessions_block * 2) -> not the end of a block
    else:
        # odd means work
        if reps % 2 != 0:
            # start work session timer and show "work" label
            countdown(work_sec)
            session_label.config(text="WORK", fg=GREEN)
        # even means break
        else:
            #start long break session timer and show "break" label
            countdown(short_break_sec)
            session_label.config(text="BREAK", fg=PINK)
    


# -------------------------------- COUNTDOWN MECHANISM ------------------------------- #
import datetime

def countdown(seconds):
    '''This function displays the current time remaining in the format MM:SS, based on the number of seconds passed as argument.
    If there are still time remaining (seconds > 0), the function calls itself after one second, passing (seconds - 1) as argument.'''
    # display timer in the MM:SS format, passing the number of seconds
    time_remaining = str(datetime.timedelta(seconds=seconds))[-5:]
    canvas.itemconfig(timer_text, text=time_remaining)

    #if seconds is greater than 0, call this function again after one second, passing (seconds - 1) as argument
    if seconds > 0:
        global running_timer
        running_timer = window.after(1000, countdown, seconds - 1)
    else:
        pop_up_window()
        # check if the session that just ended was a work session
        if reps % 2 != 0:
            # add checkmark for work session completed
            global work_sessions_counter
            work_sessions_counter += '✔'
            work_sessions_counter_label.config(text=work_sessions_counter)

        #start timer again
        start_timer()
        

def pop_up_window():
    '''This function makes the app emit a sound notification, opens the app window if it's currently minimized,
    and brings the app window to the front.'''
    window.bell()
    window.deiconify()
    window.attributes('-topmost',True)
    window.after_idle(window.attributes,'-topmost',False)



# ------------------------------------- RESET MECHANISM ---------------------------------- #
def reset_app():
    '''This function resets the whole application.'''
    # cancel running timer
    window.after_cancel(running_timer)
    # get all global variables back to values on launch
    global reps
    global work_sessions_counter
    reps = 0
    work_sessions_counter = ''
    # set screen element back to state on lanch
    canvas.itemconfig(timer_text, text='00:00')
    session_label.config(text='click start', fg=GREEN)
    work_sessions_counter_label.config(text=work_sessions_counter)
    start_button.config(state='normal')
    settings_button.config(state='normal')
    


# ------------------------------------- CAHNGE SETTINGS ---------------------------------- #
def change_settings():
    '''This function resets the whole application.'''
    settings.dialog_get_user_input(window)
    
    

# --------------------------------------- UI SETUP --------------------------------------- #
# create app window
window = Tk()
window.title("Pomodoro")
window.config( padx=50, pady=50, bg=YELLOW)

# session label (break/work)
session_label = Label(text='click start', font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, pady=20)

#create a canvas with the size of the image
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
# use the PhotoImage widget to display the image
tomato_image = PhotoImage(file=BG_IMAGE)
# add background image to the canvas in the passed coordinates (anchor point in the center of the item)  
canvas.create_image(102, 112, image=tomato_image)
# add timer text to the canvas in the passed coordinates -> order matters, later goes on top
timer_text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 24, 'bold'))

# start and reset buttons
start_button = Button(text='start', command=start_timer)
reset_button = Button(text='reset', command=reset_app)

#change settings button
settings_button = Button(text='settings', command=change_settings)

# work sessions counter (checkmarks)
work_sessions_counter_label = Label(text=work_sessions_counter, font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW, pady=20)

# place items on screen
session_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
work_sessions_counter_label.grid(row=2, column=1)
start_button.grid(row=3, column=0)
settings_button.grid(row=3, column=1)
reset_button.grid(row=3, column=2)

window.mainloop()