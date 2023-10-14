#!/usr/bin/python3
"""
This module defines a class that stores name of a state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class stores the name of a state and inherits from BaseModel
    Class Attributes:
        name (str) : name of state
    """
    name = ""
