from models.base_model import BaseModel
"""
City class implementation
"""


class City(BaseModel):
    """
    City class represents a city in your application.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
