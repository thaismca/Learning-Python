from flask import Flask

import random
number = random.randint(0,9)

# Create instance of the Flask class, that will be our WSGI application.
# The first argument is the name of the application's module or package.
app = Flask(__name__)

# route() decorator: used to define the callable object for WSGI -> tells Flask what URL should trigger our function.
# When a request is made for this URI "/", the webserver passes this to WSGI, which would then match the URI to a route
# defined in the application. The code related to that route is then executed.
@app.route("/")
def home():
    # The function returns the message we want to display in the user’s browser.
    # The default content type is HTML, so HTML in the string will be rendered by the browser.
    return '''<h1>Guess a number between 0 and 9</h1>
              <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnBpa2dqZzVyZDMzbTVkODRrcmV6cmpxdnducHAzOXRxa3Rub2M1NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKRVBGOSdSODGJa/giphy.gif" />'''


@app.route("/<int:guess>")
def result(guess):
    if guess < number:
        return '''<h1>Too low</h1>
                  <img src="https://media.giphy.com/media/2sfEg0Yv4c8E5VT7s3/giphy.gif?cid=790b7611eb230p70j2vadvwfff2qxrvwxw4i9kn5e49p17pm&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>'''
    elif guess > number:
        return '''<h1>Too high</h1>
                  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHduenFob3ZpMWFqZ2VkODNtZjljeHJ6NnphdmxoYjQ0dTJxbXQxdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEduPLmG4jUbxKxYQ/giphy.gif"/>'''
    else:
        return '''<h1>Correct!</h1>
                  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2Z3c3V1Ymx4N2pwcW92bmR6dWV4cHp0dGc4aHN0YjI1ang2eGhrOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IwAZ6dvvvaTtdI8SD5/giphy.gif"/>'''


# Conditionaly execute code in a module when it is run as a script or with 'python -m', but not when it's imported:
# __main__ is the name of the scope in which top-level code executes.
# A module's __name__ is set equal to __main__ when read from standard input, a script or from an interactive prompt.
if __name__ == "__main__":
    # run the app only if this is the current file where the app code is located, and not if it's an imported module
    app.run(debug=True)