#!/usr/bin/python3

"""Simple Flask application.

This script starts a Flask web server that listens on 0.0.0.0:5000.
It contains a two routes ('/' and '/hbnb') that returns a greeting message
"Hello HBNB!" and "HBNB" respectively.

Usage:
    Run this script to start the Flask web server.

Example:
    $ python3 1-hbnb_route.py
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
