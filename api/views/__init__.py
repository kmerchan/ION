#!/usr/bin/python3
"""
creates app_views, an instance of Blueprint
"""

from flask import Blueprint
# connects app_views with Blueprint instance
# sets /api/ url prefix for easy routing
app_views = Blueprint('app_views', __name__, url_prefix='/api/')
# imports all API routes from files in /api/views/
from api.views.identity import *
from api.views.profile import *
from api.views.profile_skills import *
from api.views.profile_identities import *
from api.views.skills import *
from api.views.status import *
