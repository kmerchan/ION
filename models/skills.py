#!/usr/bin/python3
""" this module builds Skills class """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Skills(BaseModel, Base):
    """ this module defines Skills class """
    __tablename__ = "skills"

    def __init__(self, *args, **kwargs):
        """
        calls on BaseModel __init__method to instantiate Skills object
        """
        super().__init__(*args, **kwargs)
