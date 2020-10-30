#!/usr/bin/python3
""" this module builds Profile class """
import models
from models.base_model import BaseModel, Base
from models.identity import Identity
from models.skills import Skills
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship


profile_skills = Table("profile_skills",
                       Base.metadata,
                       Column('profiles.id',
                              String(60),
                              ForeignKey('profiles.id',
                                         onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              nullable=False,
                              primary_key=True),
                       Column('skills.id',
                              String(60),
                              ForeignKey('skills.id',
                                         onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              nullable=False,
                              primary_key=True))

profile_identities = Table("profile_identities",
                           Base.metadata,
                           Column('profiles.id',
                                  String(60),
                                  ForeignKey('profiles.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  nullable=False,
                                  primary_key=True),
                           Column('identities.id',
                                  String(60),
                                  ForeignKey('identities.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  nullable=False,
                                  primary_key=True))


class Profile(BaseModel, Base):
    """ this module defines Profile class """
    __tablename__ = "profiles"
    email = Column(String(128),
                   nullable=False)
    password = Column(String(128))
    company_school_name = Column(String(256))
    about_me = Column(String(1024))
    linkedin = Column(String(256))
    social_media = Column(String(1024))
    skills = relationship('Skills',
                          secondary=profile_skills,
                          backref='profile',
                          viewonly=False)
    identities = relationship('Identity',
                              secondary=profile_identities,
                              backref='profile',
                              viewonly=False)

    def __init__(self, *args, **kwargs):
        """
        calls on BaseModel __init__ method to instantiate Profile object
        """
        super().__init__(*args, **kwargs)
