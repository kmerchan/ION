#!/usr/bin/python3
"""
defines identities from profile related API endpoints
"""

from api.views import app_views
from flask import abort, request
from flask.json import jsonify
from models import storage


@app_views.route('/profiles/<profile_id>/identities', strict_slashes=False)
def get_identities_by_profile(profile_id=None):
    """
    returns list of all identities for specific profile from profile_id
    through GET request
    """
    # get profile object
    profile = storage.get("Profile", profile_id)
    if profile is not None:
        result = []
        # use relationship to get all identities for that profile
        for identity in profile.identities:
            # append each identity's dictionary
            result.append(identity.to_dict())
        return jsonify(result.to_dict())

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles/<profile_id>/identities/<identity_id>',
                 strict_slashes=False, methods=['DELETE'])
def remove_identity_from_profile(profile_id=None, identity_id=None):
    """
    removes specific identity from specific profile with their ids
    through DELETE request
    """
    # get specific objects
    profile = storage.get("Profile", profile_id)
    identity = storage.get("Identity", identity_id)
    if profile is not None and identity is not None:
        # check every identity in profile
        for profile_identity in profile.identities:
            # if the given identity matches identity in profile, remove it
            if profile_identity.id == identity.id:
                profile.identities.remove(identity)
                # save to update database
                profile.save()
                return jsonify({}), 200

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles/<profile_id>/identities/<identity_id>',
                 strict_slashes=False, methods=['POST'])
def add_identity_to_profile():
    """
    links specific identity to specific profile through ids
    through POST request
    """
    # get specific objects
    profile = storage.get("Profile", profile_id)
    identity = storage.get("Identity", identity_id)
    if profile is not None and identity is not None:
        # check every identity in profile
        for profile_identity in profile.identities:
            # if the given identity is already linked to profile, return
            if profile_identity.id == identity.id:
                return jsonify(identity.to_dict()), 200
        # if identity is not in profile, append identity and save
        profile.identities.append(identity)
        profile.save()
        return jsonify(idenity.to_dict()), 201

    # if id not in database, abort
    abort(404)
