from models.base_model import BaseModel
"""
This module defines a class that stores the reviews of a place
"""


class State(BaseModel):
    """
    This class stores the name of a state and inherits from BaseModel
    Class Attributes:
        place_id (str): the Place.id
        user_id (str): the User.id
        text(str) - the review
    """
    place_id = ""
    user_id = ""
    text = ""
