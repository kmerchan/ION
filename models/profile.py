#!/usr/bin/python3
""" this module builds Profile class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship


profile_skills = Table("profile_skills",
                     Base.metadata,
                     Column('profile.id',
                            String(60),
                            ForeignKey('profile.id'),
                            nullable=False,
                            primary_key=True),
                      Column('skill.id',
                             String(60),
                             ForeignKey('skill.id'),
                             nullable=False,
                             primary_key=True))

profile_identities = Table("profile_identities",
                     Base.metadata,
                     Column('profile.id',
                            String(60),
                            ForeignKey('profile.id'),
                            nullable=False,
                            primary_key=True),
                      Column('identity.id',
                             String(60),
                             ForeignKey('identity.id'),
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
    LinkedIn = Column(String(256))
    social_media = Column(String(1024))
    skills = relationship('Skills',
                          secondary=profile_skills,
                          backref='profile',
                          viewonly=False)
    identities = relationship('Identities',
                              secondary=profile_identities,
                              backref='profile',
                              viewonly=False)
