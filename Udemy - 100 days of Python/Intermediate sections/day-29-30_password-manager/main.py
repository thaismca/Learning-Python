# --- PASSWORD MANAGER --- #
# create a window where the program will run
# add logo image
# create entry for website name
# create entry for username
# create entry for password
# create generate password button and implement generate password functionality
# create add button to submit the form
# implement submit form where it checks for empty inputs and display either error message or confirmation message in pop up
# create error message pop up -> error message label and ok button to dismiss the pop up and return to the main window
# create confirmation pop up -> data label, cancel button that simply closes the pop up with no further actions, and save button
# implement behaviour for save button in the confirmation pop up -> save data to a data file and clear the form in the main window 

from tkinter import *

LOGO_IMAGE = 'logo.png'

# ------------------------------ UI SETUP --------------------------------- #
# create a window where the program will run
window = Tk()
window.config(padx=20)

# add logo image
logo_canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=LOGO_IMAGE)
logo_canvas.create_image(100, 100, image=logo_image)
logo_canvas.pack()


window.mainloop()