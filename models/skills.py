#!/usr/bin/python3
""" this module builds Skills class """
from models.base_model import BaseModel, Base
from models.profile import profile_skills
from sqlalchemy.orm import relationship


class Skills(BaseModel, Base):
    """ this module defines Skills class """
    __tablename__ = "skills"
    profile_skills = relationship('Profile',
                                  secondary=profile_skills,
                                  backref='skills')
