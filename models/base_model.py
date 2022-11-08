#!/usr/bin/python3
""" Class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Class BaseModel """
    def __init__(self, *args, **kwargs):
        """ Public instance attributes """
        if not kwargs == {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        clssN = self.__class__.__name__
        return "[{}] ({}) {}".format(clssN, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of __dict__ """
        nDict = self.__dict__.copy()
        nDict["__class__"] = self.__class__.__name__
        nDict["created_at"] = nDict["created_at"].isoformat()
        nDict["updated_at"] = nDict["updated_at"].isoformat()
        return nDict
