#!/usr/bin/python3
"""
Python script to start Flask web application and
uses storage to fetch data and render HTML template
"""

from flask import Flask, render_template
from models import storage
from operator import attrgetter
app = Flask(__name__)


@app.route('/identities_list', strict_slashes=False)
def identities_list():
    """
    fetches data from storage engine and renders HTML page
    """
    identities = storage.all("Identity").values()
    identities_result = sorted(identities, key=attrgetter('name'))
    return render_template('identities_list.html',
                           identities_result=identities_result)


@app.teardown_appcontext
def teardown(self):
    """
    closes current SQLAlchemy Session after each request
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
