#!/usr/bin/python3

"""Simple Flask application.

This script starts a Flask web server that listens on 0.0.0.0:5000.
It contains multiple routes for different functionalities.

Routes:
    /: Displays “Hello HBNB!”
    /hbnb: Displays “HBNB”
    /c/<text>: Displays “C ” followed by the value of the text
                variable (replace underscore _ symbols with a space)
    /python/<text>: Displays “Python ” followed by the value of the text
                    variable (replace underscore _ symbols with a space)
                    The default value of text is “is cool”
    /number/<n>: Displays “n is a number” only if n is an integer

Usage:
    Run this script to start the Flask web server.

Example:
    $ python3 4-number_route.py
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Displays “n is a number” only if n is an integer.

    Args:
        n (int): The number parameter obtained from the URL.

    Returns:
        str: A string containing 'n is a number' if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer.

    Args:
        n (int): The number parameter obtained from the URL.

    Returns:
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_even_or_odd(n):
    """Displays an HTML page showing whether n is even or odd.

    Args:
        n (int): The number parameter obtained from the URL.

    Returns:
        str: Rendered HTML template displaying whether the number
             is even or odd inside an H1 tag.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
