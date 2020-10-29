#!/usr/bin/python3
"""
defines skills from profile related API endpoints
"""

from api.views import app_views
from flask import abort, request
from flask.json import jsonify
from models import storage


@app_views.route('/profiles/<profile_id>/skills', strict_slashes=False)
def get_skills_by_profile(profile_id=None):
    """
    returns list of all skills for specific profile from profile_id
    through GET request
    """
    # get profile object
    profile = storage.get("Profile", profile_id)
    if profile is not None:
        result = []
        # use relationship to get all skills for that profile
        for skills in profile.skills:
            # append each skill's dictionary
            result.append(skills.to_dict())
        return jsonify(result.to_dict())

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles/<profile_id>/skills/<skills_id>',
                 strict_slashes=False, methods=['DELETE'])
def remove_skills_from_profile(profile_id=None, skills_id=None):
    """
    removes specific skill from specific profile with their ids
    through DELETE request
    """
    # get specific objects
    profile = storage.get("Profile", profile_id)
    skills = storage.get("Skills", skills_id)
    if profile is not None and skills is not None:
        # check every skill in profile
        for profile_skill in profile.skills:
            # if the given skill matches skill in profile, remove it
            if profile_skill.id == skills.id:
                profile.skills.remove(skills)
                # save to update database
                profile.save()
                return jsonify({}), 200

    # if id not in database, abort
    abort(404)


@app_views.route('/profiles/<profile_id>/skills/<skills_id>',
                 strict_slashes=False, methods=['POST'])
def add_skills_to_profile():
    """
    links specific skills to specific profile through ids
    through POST request
    """
    # get specific objects
    profile = storage.get("Profile", profile_id)
    skills = storage.get("Skills", skills_id)
    if profile is not None and skills is not None:
        # check every skill in profile
        for profile_skill in profile.skills:
            # if the given skill is already linked to profile, return
            if profile_skill.id == skills.id:
                return jsonify(skills.to_dict()), 200
        # if skill is not in profile, append skill and save
        profile.skills.append(skills)
        profile.save()
        return jsonify(skills.to_dict()), 201

    # if id not in database, abort
    abort(404)
