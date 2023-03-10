# the sole purpose of the code below is to get practice with tkinter and see how to create some different basic components

import tkinter

# create a window where the program will run
window = tkinter.Tk()

# program code goes between window creation and loop that keeps it open

# define program title - appears in the window title
window.title("Program name")

# window scales to fit all components you add to it, but you can set a min size when it loads
# this won't prevent user from resizing the window to a smaller size though
window.minsize(width=500, height=300)

# add components
# in Tkinter, you first create the component and then specify how that component sould be laid out on the screen
# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

# entry -> input
input = tkinter.Entry(width=25)
input.pack()
# in order to access the data entered in the input -> input.get()

# button
# I can have a function that will be attached to a component, to be called upon user interaction
def button_clicked():
    # altering component attributes
    # can be done using the config method
    my_label.config(text=input.get())
    # or passing the name of the attribute using the following syntax
    my_label["foreground"] = "#617"

# this function is attached by passing the name of the function to the command attribute
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# text box -> input that allows multiple lines (height -> number of lines)
text = tkinter.Text(height=5, width=30)
#put the cursor in the text box
text.focus()
# add placeholder text
text.insert(tkinter.END, "Placeholder text in the textbox")
# get current value of the text box at line 1 character 0
text.get("1.0", tkinter.END)
# add text box to the window
text.pack()

# spinbox -> number input where we can optionally set a range and increment step
spinbox = tkinter.Spinbox(from_=0, to=10, increment=2, width=5)
spinbox.pack()

# scale -> range input where we can optionally set a range and increment step
scale = tkinter.Scale(from_= 0, to=100)
scale.pack()

# checkbutton -> input that can be checked on (1) and off (0) by tying the checkbox to a variable that will hold on to checked state
# variable that will hold on to checked state
checked_state = tkinter.IntVar()
# checkbutton
checkbutton = tkinter.Checkbutton(text="Is on?", variable=checked_state)
checkbutton.pack()

# radiobutton -> input that allows picking one out of different options
# all options from a same selection need to be tied to the same variable that will hold on to the selected state
# variable that will hold on to the selected state of selection_1
radio_state_selection_1 = tkinter.IntVar()
#radiobuttons in one selection
radio_1_selection_1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state_selection_1)
radio_2_selection_1 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state_selection_1)
# variable that will hold on to the selected state of selection_2
radio_state_selection_2 = tkinter.IntVar()
#radiobuttons in one selection
radio_1_selection_2 = tkinter.Radiobutton(text="Option A", value="A", variable=radio_state_selection_2)
radio_2_selection_2 = tkinter.Radiobutton(text="Option B", value="B", variable=radio_state_selection_2)
# display all radiobuttons on the window
radio_1_selection_1.pack()
radio_2_selection_1.pack()
radio_1_selection_2.pack()
radio_2_selection_2.pack()

# listbox -> list of options rendered from a python list
# function that will be bound to be called when user selects an item
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
# list of items to generate listbox options
colors = ["Red", "Yellow", "Purple", "Blue"]
for color in colors:
    listbox.insert(colors.index(color), color)
# bind function to the triggered when user selects an item from list
listbox.bind("<<ListboxSelect>>", listbox_used)
# display listbox on the window
listbox.pack()





# keep this window open and listens for what user will do to interact with the program
window.mainloop()