#!/usr/bin/python3
"""
Python script to start Flask web application and
uses storage to fetch data and render HTML template
"""

from flask import Flask, render_template
from models import storage
from operator import attrgetter
app = Flask(__name__)


@app.route('/ION_filters', strict_slashes=False)
def render_filters():
    """
    fetches data from storage engine and renders filters on HTML page
    """
    skills = storage.all("Skills").values()
    skills_result = sorted(skills, key=attrgetter('name'))
    identities = storage.all("Identity").values()
    identities_result = sorted(identities, key=attrgetter('name'))
    return render_template('index_from_database.html',
                           skills_result=skills_result,
                           identities_result=identities_result)


@app.teardown_appcontext
def teardown(self):
    """
    closes current SQLAlchemy Session after each request
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
