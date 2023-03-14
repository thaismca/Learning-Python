
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SESSIONS_PER_BLOCK = 4
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BG_IMAGE = './Intermediate sections/day-28_pomodoro-app/tomato.png'

# TODO: set up UI with:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# session label (break/work)
session_label = Label(text='SESSION', font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, pady=20)

# a background image
# countdown label
#create a canvas with the size of the image
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
# use the PhotoImage widget to display the image
tomato_image = PhotoImage(file=BG_IMAGE)
# add image to the canvas in the passed coordinates (anchor point in the center of the item)  
canvas.create_image(102, 112, image=tomato_image)
# add text to the canvas in the passed coordinates -> order matters, later goes on top
canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

# start and reset buttons
start_button = Button(text='start')
reset_button = Button(text='reset')

# work sessions counter (checkmarks)
sessions_counter_label = Label(text='✔ ✔ ✔ ✔', font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW, pady=20)

# pace items on screen
session_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
sessions_counter_label.grid(row=3, column=1)


window.mainloop()

# TODO: add countdown mechanism

# TODO: set different timer sesisons and values

# TODO: display checkmarks when each work session is done
# TODO: reset the work sessions counter when the block reaches a number of work sessions
# (pomodoro applies blocks with 4 work sessions, but here it can be customized)

# TODO: add functionality to reset the whole application when clicking the reset button