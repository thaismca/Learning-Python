# --- PASSWORD MANAGER --- #

from tkinter import *
from tkinter import messagebox

LOGO_IMAGE = 'logo.png'
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ----------------------------- SAVE PASSWORD ------------------------------- #
def submit_entries():
    '''Get the values from the form entries and check if they are not empty.
     If any entry is empty, displays error message. If no empty entries, display save confirmation.'''
    website = website_entry.get().capitalize()
    username = username_entry.get()
    password = password_entry.get()

    if website.strip() == '' or username.strip() == '' or password.strip() == '':
        messagebox.showerror(title='Error', message="Please make sure you haven't left any fields empty!")
    else:
        confirm_save(website, username, password)



def confirm_save(website, username, password):
    '''Displays a messagebox to confirm save containing the data submitted in the form so user can confer. Saves the data only if user clicks 'yes'.'''
    confirm_message = f"Website: {website}\nUsername/Email: {username}\nPassword: {password}\n\nConfirm save?"
    confirmation = messagebox.askyesno(title='Confirm save', message=confirm_message)
    if confirmation:
        save_password(website, username, password)
        clear_form_entries()



import json
def save_password(website, username, password):
    '''Saves the data entered in the password manager form to a data.json file.'''
    # create a dictionary for the new data
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    
    try:
        # try to open an existing data file and read data from it
        with open("data.json", "r") as file:
            # read old data to a data_dict variable
            data_dict = json.load(file)
    
    except FileNotFoundError:
        # if file does not exist create a file and write the only new_data to it
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)

    else:
        # could read from a data.json file 

        # check for pre existing data for that website
        if website in data_dict:
            # found website in data_dict
            username = data_dict[website]['username']
            password = data_dict[website]['password']
            # check if user wants to overwrite exisitng data
            overwrite = messagebox.askyesno(title='Warning', message=f"There's already an username and password saved for {website}!"
                                f"\nUsername: {username}\nPassword: {password}\n\nDo you want to overwrite the existing data?")
            if overwrite:
                # user wants to overwrite -> replace existing data
                data_dict[website]['username'] = username
                data_dict[website]['password'] = password
            else:
                # user doesn't want to overwrite -> return fro function without saving any new data
                return

        # update old data with new_data
        data_dict.update(new_data)
        # open file in write mode -> write the updated data to the file
        with open("data.json", "w") as file:
            json.dump(data_dict, file, indent=4)



def clear_form_entries():
    website_entry.delete(0, END)
    username_entry.delete(0,END)
    password_entry.delete(0, END)
        


# --------------------------- PASSWORD GENERATOR ---------------------------- #
from random import randint, choice, shuffle
import pyperclip
def generate_password():
    '''Generates a new random password, adds it to the password entry in the form, and copies the generated password to the clipboard.'''
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    # display generated password in password entry
    password_entry.insert(0, password)
    # copy generated password to clipboard
    pyperclip.copy(password)



# ---------------------------- SEARCH PASSWORD ------------------------------ #
def search_data_for_website():
    '''Searches username and password data for a website that the user enters in the website entry.'''
    # get a reference to the website entered by the user
    website = website_entry.get().capitalize()

    # get a reference to a dictionary containing the existing data saved for this user
    try:
     # try to open an existing data file and read data from it
        with open("data.json", "r") as file:
            # read old data to a data_dict variable
            data_dict = json.load(file)
    
    except FileNotFoundError:
        # if file does not exist -> show messagebox with appropriated error message
        messagebox.showerror(title='Error', message="No data file found!\n\nThere are no saved passwords.")

    else:
        # could read from a data.json file -> try to find the website in the keys
        if website in data_dict:
            # found website in data_dict
            username = data_dict[website]['username']
            password = data_dict[website]['password']

            # show messagebox with the respective username and password data
            messagebox.showinfo(title=website, message=f'Username: {username}\nPassword: {password}\n\nPassword copied to clipboard')
            # copy password to clipboard
            pyperclip.copy(password)
        else:
            # cannot find website in data_dict -> show messagebox with appropriated error message
            messagebox.showerror(title='Error', message=f"No exising data for the website {website}!")
        


# -------------------------------- UI SETUP --------------------------------- #
# create a window where the program will run
window = Tk()
window.title('Password Manager')
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

# search button
add_button = Button(text='Search', command=search_data_for_website)
add_button.grid(row=1, column=2, sticky="EW")

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
gen_password_button = Button(text='Generate Password', command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="EW")

# add -> submit
add_button = Button(text='Add', width=35, command=submit_entries)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()