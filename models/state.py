from models.base_model import BaseModel
"""
This module defines a class that stores name of a state
"""


class User(BaseModel):
    """
    This class stores the name of a state and inherits from BaseModel
    Class Attributes:
        name (str) : name of state
    """
    name = ""
