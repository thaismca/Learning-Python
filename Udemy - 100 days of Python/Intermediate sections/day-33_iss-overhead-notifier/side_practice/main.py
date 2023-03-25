'''This side practice implements a tkinter GUI program that displays a random quote after clicking a button, based on
what is returned from a GET request made to the kanye rest API. The goal is to get practice with the requests HTTP library'''

from tkinter import *
# import requests HTTP library
import requests


def get_quote():
    '''Makes a request to the kanye rest api and replaces the text in the canvas by the quote that is returned in the response.'''
    # make a get request 
    response = requests.get('https://api.kanye.rest')
    # raise exception if no success
    response.raise_for_status()
    # get a reference to the quote in the JSON file
    quote = response.json()['quote']
    # replace quote_text in the canvas passing the quote 
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
# whenever the button is clicked, a new quote is displayed in the canvas
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()