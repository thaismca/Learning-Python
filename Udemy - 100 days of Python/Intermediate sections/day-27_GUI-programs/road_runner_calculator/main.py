# course project: create program that converts miles to kilometers
# this project: converts units for a value based on user selection -> made for road runners
# options available:
# distance - miles and kilometers
# speed - miles per hour and kilometers per hour
# pace - minutes per mile and minutes per kilometer

from tkinter import *
# TODO: create a tkinter window
window = Tk()
window.title("The road runner conversion calculator")
window.minsize(width=600, height=100)
window.config(pady=10)

# create instance of the running program
from app_components import App_Components
app = App_Components(window)


# keep the window open and listening for user interactions
window.mainloop()
