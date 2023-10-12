from models.base_model import BaseModel
"""
This module defines a class that stores name of an amenity
"""


class Amenity(BaseModel):
    """
    This class stores the name of an amenity and inherits from BaseModel
    Class Attributes:
        name (str) : name of an amenity
    """
    name = ""
