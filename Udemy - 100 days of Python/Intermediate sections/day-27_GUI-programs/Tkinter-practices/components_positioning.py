# the sole purpose of the code below is to get practice with tkinter and see how to set the position of components in the program window using grid

import tkinter

# create a window where the program will run
window = tkinter.Tk()
window.title("Program name")
window.minsize(width=500, height=300)
# adds padding around the window
window.config(padx=30, pady=50)

# add components
# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# grid layout -> is always relative to other components in the window
my_label.grid(column=1, row=0)
# adds padding around the label
my_label.config(padx=15, pady=25)

# entry -> input
input = tkinter.Entry(width=25)
input.grid(column=0, row=1)

# button
def button_clicked():
    my_label.config(text=input.get())
    my_label["foreground"] = "#617"

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)


# keep this window open and listens for what user will do to interact with the program
window.mainloop()