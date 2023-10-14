#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module defines a class that stores the info of a user
"""


class User(BaseModel):
    """
    This class stores the user's input and inherits from BaseModel
    Class Attributes:
        email (str) : email of the user
        password (str) : password of the user
        first_name (str) : first_name of the user
        last_name (str) : last_name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
