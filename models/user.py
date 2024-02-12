#!/use/bin/python3


""" A user class inheriting from the Baseclass"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class


    Attributes:
    email (str): user email
    password (str): user password
    first_name (str): first name
    last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
