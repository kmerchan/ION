#!/usr/bin/python3
""" this module builds Profile class """
import models
from models.base_model import BaseModel, Base
from models.identity import Identity
from models.skills import Skills
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship


# secondary table that holds the relationship between profile and skills
# table contains 2 columns with cascading delete/update for db management
# 1 column: ForeignKey associated with profile id
# 2 column: ForeignKey associated with skills id
# each row of data links a profile id with a specific skills id
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

# secondary table that holds the relationship between profile and identities
# table contains 2 columns with cascading delete/update for db management
# 1 column: ForeignKey associated with profile id
# 2 column: ForeignKey associated with identity id
# each row of data links a profile id with a specific identity id
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
    # attribute to establish corresponding table name in MySQL
    __tablename__ = "profiles"
    # creates required column in MySQL table, user must input email attribute
    email = Column(String(128),
                   nullable=False)
    # creates optional column in MySQL table for user's password
    # in the future, this will be encrypted and required for each user
    # it will allow user's to manage their profile directly with auth.
    password = Column(String(128))
    # creates optional column in MySQL table if user wishes to provide
    # their organization info
    company_school_name = Column(String(256))
    # creates optional column in MySQL table if user wishes to provide
    # a brief bio about their background/why they use ION
    about_me = Column(String(1024))
    # creates optional column in MySQL table if user wishes to provide
    # link to their LinkedIn profile
    linkedin = Column(String(256))
    # creates optional column in MySQL table if user wishes to provide
    # links to other social media
    social_media = Column(String(1024))
    # creates reference to secondary table to get all skills
    # that match profile through relationship
    skills = relationship('Skills',
                          secondary=profile_skills,
                          backref='profile',
                          viewonly=False)
    # creates reference to secondary table to get all identities
    # that match profile through relationship
    identities = relationship('Identity',
                              secondary=profile_identities,
                              backref='profile',
                              viewonly=False)

    def __init__(self, *args, **kwargs):
        """
        calls on BaseModel __init__ method to instantiate Profile object
        """
        # initializes new profile object based on BaseModel
        # sets profile id, created_at, updated_at attributes
        # requires user to input name attribute before saving to db
        super().__init__(*args, **kwargs)
