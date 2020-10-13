#!/usr/bin/python3
""" this module builds Identity class """
from models.base_model import BaseModel, Base
from models.profile import profile_identities
from sqlalchemy.orm import relationship


class Identity(Basemodel, Base):
    """ this module defines Identity class """
    __tablename__ = "identities"
    profile_identities = relationship('Profile',
                                      secondary=profile_identities,
                                      backref='identities')
