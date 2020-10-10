#!/usr/bin/python3
""" this module builds Identity class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class Identity(Basemodel, Base):
    """ this module defines Identity class """
    __tablename__ = "identities"
    name = Column(String(60), nullable=False)
    people_id = Column(String(60), ForiegnKey(people.id), nullable=False)
