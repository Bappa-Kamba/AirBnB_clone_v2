#!/usr/bin/python3
"""
This script starts a Flask web server that listens on 0.0.0.0:5000.

Routes:
    /states_list: Renders a template that displays the states present
                    in the DBStorage sorted by name (`A-Z`)
    /cities_by_states: Renders a template that displays the cities by states
                        in the DBStorage sorted by name (`A-Z`)
Usage:
    Run this script to start the Flask web server.

Example:
    $ python3 8-cities_by_states.py
"""
import os
import sys
from flask import Flask, render_template
from models import storage
from models.state import State

# Get the parent directory path
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
# sys.path.append(parent_dir)

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    """
        removes the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
        display html page
        fetch sorted states to insert into html in UL tag
    """

    states = [state for state in storage.all(State).values()]
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
        Renders an html template with the states and cities fetched from the
        DBStorage
    """
    # Fetch states
    states = sorted(
        [state for state in storage.all(State).values()],
        key=lambda state: state.name
    )
    return render_template(
            "8-cities_by_states.html",
            states=states
            )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
