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

# ---------------------------- SAVE PASSWORD ------------------------------ #
def save_password():
    '''Saves the data entered in the password manager form to a data.txt file.
    The entries in the data.txt file will be sorted alphabetically.'''
    # get data from inputs
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # form the new data entry
    new_data = f"{website} | {username} | {password}\n"
    
    data_list = []
    try:
        # try to open an existing data file and read data from it
        with open("data.txt", "r") as file:
            data_list = file.readlines()
    except:
        pass
    
    # add the new data to the existing list
    data_list.append(new_data)
    data_list.sort()

    # overwrite the file with the updated list
    with open("data.txt", "w") as file:
        file.writelines(data_list)
        

# ------------------------------ UI SETUP --------------------------------- #
# create a window where the program will run
window = Tk()
window.config(padx=30, pady=30)

# add logo image
logo_canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=LOGO_IMAGE)
logo_canvas.create_image(100, 100, image=logo_image)
logo_canvas.grid(row=0, column=1)

# website name
website_label = Label(text='Website:', pady=5)
website_entry = Entry()
website_entry.focus()
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

# username
username_label = Label(text='Email/Username:', pady=5)
username_entry = Entry()
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# password
password_label = Label(text='Password:', pady=5)
password_entry = Entry()
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, sticky="EW")

# generate password
gen_password_button = Button(text='Generate Password')
gen_password_button.grid(row=3, column=2, sticky="EW")

# add -> submit
add_button = Button(text='Add', width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()