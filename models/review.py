#!/usr/bin/python3

""" A State class inheriting from the Baseclass"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review classs

    Attributes:
    place_id (str): place id
    user_id (str): user id
    text (str): review text
    """

    place_id = ""
    user_id = ""
    text = ""
