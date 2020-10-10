#!/usr/bin/python3
""" this module builds BaseModel class """
from sqlalchemy import Column, Integer, String, DateTime
from sqlachemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel():
    """ this module defines BaseModel to be inherited by all classes """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    name = Column(String(128), nullable=False) #unsure if we need a name for BaseModel

    # __init__ method

    def delete(self):
        """ this method deletes current instance from DBStorage """
        import models
        models.storage.delete(self)

    def save(self):
        """ this method updates time of change then saves new info """
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
