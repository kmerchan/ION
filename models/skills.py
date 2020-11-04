#!/usr/bin/python3
""" this module builds Skills class """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Skills(BaseModel, Base):
    """ this module defines Skills class """
    # attribute to establish corresponding table name in MySQL
    __tablename__ = "skills"

    def __init__(self, *args, **kwargs):
        """
        calls on BaseModel __init__method to instantiate Skills object
        """
        # initializes new profile object based on BaseModel
        # sets profile id, created_at, updated_at attributes
        # requires user to input name attribute before saving to db
        super().__init__(*args, **kwargs)
