#!/usr/bin/python3
import uuid
import models
from datetime import datetime

"""
This module defines a base model class
for the other classes in the application
"""


class BaseModel:
    """
    Base model that will act as the base class
    Takes in kwargs specified by the user
    Attributes default values:
        id (str): Unique ID associated with an instance
        created_at (datetime): time the instance was created
        updated_at (datetime): time the instance was updated
    """
    def __init__(self, *args, **kwargs):
        """
        Class constructor
        Initializes the id, created_at, and updated_at attributes.
        """
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, format))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        User friendly representation of the instance
        Returns:
            str: String representation of the instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attriute to current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Represent the class in form of a dictionary
        Return:
            dict: dictionary respresentaion
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
