#!/usr/bin/python3
""" this module builds BaseModel class """
from datetime import datetime
from models import storage
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from sqlachemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel():
    """ this module defines BaseModel to be inherited by all classes """
    id = Column(String(60),
                nullable=False,
                primary_key=True)
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    name = Column(String(128),
                  nullable=False)

    def __init__(self, *args, **kwargs):
        """this method instantiates a new model from kwargs"""
        if kwargs:
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """this method returns a string representation of the instance"""
        cls = (str(type(self)))
        return "[{}.{}] {}".format(cls, self.id, self.__dict__)

    def save(self):
        """ this method updates time of change then saves new info """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """ this method deletes current instance from DBStorage """
        storage.delete(self)
