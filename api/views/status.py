#!/usr/bin/python3
"""
creates route /status for blueprint object app_views
"""

from api.views import app_views
from flask.json import jsonify


# defines API route that gives status of API
@app_views.route('/status', strict_slashes=False)
def show_status():
    """
    returns status 'OK' if API is working
    """
    return jsonify(status='OK')
