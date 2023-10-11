import uuid
from datetime import datetime
"""
This module defines a base model class
for the other classes in the application
"""


class BaseModel:
    """
    Base model that will act as the base class
    Attributes:
        id (str): Unique ID associated with an instance
        created_at (datetime): time the instance was created
        updated_at (datetime): time the instance was updated
    """
    def __init__(self):
        """
        Class constructor

        Initializes the id, created_at, and updated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        User friendly representation of the instance
        Returns:
            str: String representation of the instance
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attriute to current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Represent the class in form of a dictionary
        Return:
            dict: dictionary respresentaion
        """
        class_name = self.__class__.__name__
        created_f = self.created_at.isoformat()
        updated_f = self.updated_at.isoformat()

        obj_dict = {
            "__class__": class_name,
            "id": self.id,
            "created_at": created_f,
            "updated_at": updated_f
        }

        obj_dict.update(self.__dict__)

        return obj_dict
