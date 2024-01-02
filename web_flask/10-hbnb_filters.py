#!/usr/bin/python3
"""
This script starts a Flask web server that listens on 0.0.0.0:5000.

Routes:
    /states_list: Renders a template that displays the states present
                    in the DBStorage sorted by name (`A-Z`)
    /cities_by_states: Renders a template that displays the cities by states
                        in the DBStorage sorted by name (`A-Z`)
    /states: Renders a template similar to the `/states_list` route
    /states/<int:id>: Renders a template that displays the cities in a state
                        if the `id` is valid
    /hbnb_filters: Renders a template like 6-index.html which was done
                    during the project "0x01. AirBnB clone - Web static"
Usage:
    Run this script to start the Flask web server.

Example:
    $ python3 10-hbnb_filters.py
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    """
        removes the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
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


@app.route("/states/<string:id>", strict_slashes=False)
def states(id):
    """
        Renders an html template with the state and its cities fetched
        from thne DBStorage if `id` is valid, "Not found!" otherwise
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
        Renders a template like 6-index.html which was done
        during the project "0x01. AirBnB clone - Web static"
    """
    # Fetch states
    states = sorted(
        [state for state in storage.all(State).values()],
        key=lambda state: state.name
    )

    amenities = sorted(
        [amenity for amenity in storage.all(Amenity).values()],
        key=lambda amenity: amenity.name
    )

    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
