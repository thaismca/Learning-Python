from flask import Flask

# Create instance of the Flask class, that will be our WSGI application.
# The first argument is the name of the application's module or package.
app = Flask(__name__)

# route() decorator: used to define the callable object for WSGI -> tells Flask what URL should trigger our function.
# When a request is made for this URI "/", the webserver passes this to WSGI, which would then match the URI to a route
# defined in the application. The code related to that route is then executed.
@app.route("/")
def hello_world():
    # The function returns the message we want to display in the user’s browser.
    # The default content type is HTML, so HTML in the string will be rendered by the browser.
    return "<p>Hello, World!</p>"


# Conditionaly execute code in a module when it is run as a script or with 'python -m', but not when it's imported:
# __main__ is the name of the scope in which top-level code executes.
# A module's __name__ is set equal to __main__ when read from standard input, a script or from an interactive prompt.
if __name__ == "__main__":
    # run the app only if this is the current file where the app code is located, and not if it's an imported module
    app.run()