#!/usr/bin/python3
"""
This module defines a class that stores name of an amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class stores the name of an amenity and inherits from BaseModel
    Class Attributes:
        name (str) : name of an amenity
    """
    name = ""
