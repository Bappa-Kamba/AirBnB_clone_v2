#!/usr/bin/python3

"""Simple Flask application.

This script starts a Flask web server that listens on 0.0.0.0:5000.
It contains multiple routes for different functionalities.

Routes:
    /: Displays “Hello HBNB!”
    /hbnb: Displays "HBNB"
    /c/<text>: Displays “C ” followed by the value of the text variable
                (replace underscore _ symbols with a space)
    /python/<text>: Displays “Python ” followed by the value of the text
                    variable (replace underscore _ symbols with a space)
                    The default value of text is “is cool”

Usage:
    Run this script to start the Flask web server.

Example:
    $ python3 3-python_route.py
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Returns a greeting message.

    Returns:
        str: A string containing the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns the string HBNB.

    Returns:
        str: A string "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns 'C ' followed by the value of the text variable.

    Args:
        text (str): The text parameter obtained from the URL.

    Returns:
        str: A string containing 'C ' +  value of the text variable.
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Returns 'C ' followed by the value of the text variable.
    Args:
        text (str): The text parameter obtained from the URL.

    Returns:
        str: A string containing 'C ' +  value of the text variable.
    """
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
