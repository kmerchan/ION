#!/usr/bin/python3
""" this module builds Skills class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Skills(BaseModel, Base):
    """ this module defines Skills class """
    __tablename__ = "skills"
    id = Column(String(60), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
