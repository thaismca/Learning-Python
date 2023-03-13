from tkinter import *
# create a tkinter window
window = Tk()
window.title("The road runner conversion calculator")
window.minsize(width=600, height=100)
window.config(pady=10)

# create instance of the running program
from app_components import Runner_Conversion_Calculator
app = Runner_Conversion_Calculator(window)


# keep the window open and listening for user interactions
window.mainloop()
