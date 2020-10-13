#!/usr/bin/python3
""" this module builds People class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class People(BaseModel, Base):
    """ this module defines People class """
    __tablename__ = "people"
    id = Column(String(60), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
