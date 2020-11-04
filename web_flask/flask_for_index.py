#!/usr/bin/python3
"""
Python script to start Flask web application and
uses storage to fetch data and render HTML template
"""

from flask import Flask, render_template
from models import storage
from operator import attrgetter
# creates instance of Flask, app is bound to gunicorn when running app server
app = Flask(__name__)


@app.route('/ION_filters', strict_slashes=False)
def render_filters():
    """
    fetches data from storage engine and renders filters on HTML page
    """
    # fetches all skills objects from storage (current database)
    skills = storage.all("Skills").values()
    # sorts all skills objects by name
    skills_result = sorted(skills, key=attrgetter('name'))
    # fetches all identity objects from storage (current database)
    identities = storage.all("Identity").values()
    # sorts all identities objects by name
    identities_result = sorted(identities, key=attrgetter('name'))
    # sends skills_result and identities_result to be rendered with
    # Jinja in HTML template
    return render_template('index_from_database.html',
                           skills_result=skills_result,
                           identities_result=identities_result)


@app.teardown_appcontext
def teardown(self):
    """
    closes current SQLAlchemy Session after each request
    """
    # closes the current session during teardown
    storage.close()

if __name__ == '__main__':
    # runs the Flask application through port 5000 from local host
    app.run(host='127.0.0.1', port='5000')
