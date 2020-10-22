#!/usr/bin/python3
""" this module builds Identity class """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Identity(BaseModel, Base):
    """ this module defines Identity class """
    __tablename__ = "identities"

    def __init__(self, *args, **kwargs):
        """
        calls on BaseModel __init__method to instantiate Identity object
        """
        super().__init__(*args, **kwargs)
