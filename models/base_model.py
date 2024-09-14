#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        Class Base
        Defines all common attributes/methods for other classes
        Attr :
                id: string - assigned with an uuid when an instance is created
                created_at: datetime - assigned with the current datetime
                when an instance is created

                updated_at: datetime - assigned with the current datetime
                when an instance is created.
                It will be updated every time the object change.
    """

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], tform)
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], tform)
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Set updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel instance.

        Includes key/value pair __class__.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return print/str representation of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
