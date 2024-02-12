#!/usr/bin/python3

""" A City class inheriting from the Baseclass"""

from models.base_model import BaseModel


class City(BaseModel):
    """A State class

    Attributes:
        state_id (str): State id
        name (str): State name
    """

    state_id = ""
    name = ""
