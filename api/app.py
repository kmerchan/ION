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
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins="0.0.0.0")
ION_API_HOST = getenv('ION_API_HOST')
if ION_API_HOST is None:
    ION_API_HOST = '0.0.0.0'
ION_API_PORT = getenv('ION_API_PORT')
if ION_API_PORT is None:
    ION_API_PORT = '5000'


@app.teardown_appcontext
def teardown(self):
    """
    closes the current session through close method
    """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """
    returns JSON formatted error
    """
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app.run(host=ION_API_HOST, port=ION_API_PORT, threaded=True)
