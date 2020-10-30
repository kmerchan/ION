#!/usr/bin/python3
"""
defines Profile related API endpoints
"""

from api.views import app_views
from flask import abort, request
from flask.json import jsonify
from models import storage
from models.profile import Profile


@app_views.route('/profiles', strict_slashes=False)
@app_views.route('/profiles/<profile_id>', strict_slashes=False)
def get_profile(profile_id=None):
    """
    returns list of all profiles or specific profile if id provided
    through GET request
    """
    # if no profile id specified, expect list of all profiles
    if profile_id is None:
        result = []
        # use all method by class name to get all profile objs
        for profile in storage.all("Profile").values():
            # append dict_rep of each obj to list to jsonify
            result.append(profile.to_dict())
        return jsonify(result)

    # otherwise, profile id provided so looking for specific profile
    result = storage.get("Profile", profile_id)
    if result is not None:
        return jsonify(result.to_dict())

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles/<profile_id>', strict_slashes=False,
                 methods=['DELETE'])
def del_profile(profile_id):
    """
    deletes a specific profile object from id
    through DELETE request
    """
    # get specific object and delete from database
    result = storage.get("Profile", profile_id)
    if result is not None:
        result.delete()
        # return empty dictionary and status code 200
        return jsonify({}), 200

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles', strict_slashes=False,
                 methods=['POST'])
def create_profile():
    """
    create a new instance of Profile
    through POST request
    """
    # get JSON from POST request
    json = request.get_json(silent=True)
    # checks for missing attributes
    if json is None:
        abort(400, 'Not a JSON')
    if 'name' not in json:
        abort(400, 'Missing name attribute')
    if 'email' not in json:
        abort(400, 'Missing email attribute')
    # create new instance with **kwargs from json
    new_obj = Profile(**json)
    new_obj.save()
    # return json version of object's to_dict()
    return jsonify(new_obj.to_dict()), 201


@app_views.route('/profiles/<profile_id>', strict_slashes=False,
                 methods=['PUT'])
def update_profile(profile_id):
    """
    updates an instance of Profile with id
    through PUT request
    """
    # get JSON from PUT request
    json = request.get_json(silent=True)
    # checks for missing attributes
    if json is None:
        abort(400, 'Not a JSON')
    # gets object to update
    result = storage.get("Profile", profile_id)
    if result is not None:
        # sets attribute for all key except id or datetimes
        for key, value in json.items():
            if key != 'updated_at' and key != 'created_at' and key != 'id':
                setattr(result, key, value)
        # saves to update 'updated_at' and save in database
        result.save()
        return jsonify(result.to_dict()), 200

    # if id not in database, abort
    abort(404)
