#!/usr/bin/python3
"""
creates instance of Flask and registers blueprint to instance
"""

from api.views import app_views
from flask import Flask
from flask_cors import CORS
from flask.json import jsonify
from models import storage
from os import getenv
# creates instance of Flask, app is bound to gunicorn when running app server
app = Flask(__name__)
# connects app to app_views (see /api/views/__init__.py) and flask_cors
app.register_blueprint(app_views)
CORS(app, origins="0.0.0.0")
# gets requested API host from env variables or sets to home by default
ION_API_HOST = getenv('ION_API_HOST')
if ION_API_HOST is None:
    ION_API_HOST = '0.0.0.0'
# gets requested API port from env variables or sets to 5000 by default
ION_API_PORT = getenv('ION_API_PORT')
if ION_API_PORT is None:
    ION_API_PORT = '5000'


@app.teardown_appcontext
def teardown(self):
    """
    closes the current session through close method
    """
    # closes the current session during teardown
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """
    returns JSON formatted error
    """
    # returns JSON string 'Not found' if error occurs
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    # runs the Flask application through specified or default port and host
    app.run(host=ION_API_HOST, port=ION_API_PORT, threaded=True)
