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
window.minsize(width=500, height=250)

# TODO: create a radiobutton selection for the conversion types options (distance = default selection, speed or pace)
conversion_type_state = StringVar(None, "distance")
distance = Radiobutton(text="Distance", value="distance", variable=conversion_type_state)
speed = Radiobutton(text="Speed", value="speed", variable=conversion_type_state)
pace = Radiobutton(text="Pace", value="pace", variable=conversion_type_state)

distance.grid(row=0, column=0)
speed.grid(row=0, column=1)
pace.grid(row=0, column=2)


# keep the window open and listening for user interactions
window.mainloop()


# TODO: create a selection for the base unit that changes its options based on conversion type selecion
# TODO: create input for base value to be converted
# TODO: implement conversion calculation formulas
# TODO: create button that applies calculation formula based on conversion options selected
# TODO: create result label that displayes result when button is clicked 