# ---- Flask Hello Word ---- #

# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function which returns a string
def hello_world():
    return "Hello, World!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

# Start the development server using the run() method
if __name__ == "__main__":
    app.run()

