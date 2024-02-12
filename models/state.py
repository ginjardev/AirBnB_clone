#!/usr/bin/python3

""" A State class inheriting from the Baseclass"""

from models.base_model import BaseModel


class State(BaseModel):
    """A State class
    name (str): state name
    """

    name = ""
