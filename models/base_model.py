#!/usr/bin/python3


"""Base class model that contains all the
    common attributes
    and method for other classes
    the is the root of all class
"""
import datetime
import uuid
import models


class BaseModel:
    """Baseclass model the root of all class that generate uuid id
    created_at time and date and also updated time and date

    """

    def __init__(self, *args, **kwargs):
        """initalizing instances"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

        if kwargs != {}:
            listt = [i for i in kwargs.keys() if i != "__class__"]

            for i in listt:
                if i == "created_at" or i == "updated_at":
                    first = kwargs[i]
                    hold = datetime.datetime
                    take = hold.strptime(first, "%Y-%m-%dT%H:%M:%S.%f")
                    kwargs[i] = take
                setattr(self, i, kwargs[i])
        else:
            """where its save to a store at every instances"""
            models.storage.new(self)

    def save(self):
        """A method that update the public instance attribute of
             updating the `updated_at` attribute with
        the current datetime. This function does not take any
        parameters and does not return anything.
        """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """A method that returns a dictionary
        containing all keys/value of  __dict__"""

        hold = self.__dict__
        hold = self.__dict__.copy()
        hold["created_at"] = self.created_at.isoformat()
        hold["updated_at"] = self.updated_at.isoformat()
        hold["__class__"] = f"{self.__class__.__name__}"
        return hold

    def delete(self):
        """Deletes the instance from the storage."""
        key = f"{self.__class__.__name__}.{self.id}"
        hold = models.storage.all()
        hold.pop(key)
        models.storage.save()

    def __str__(self):
        """A method that returns
        the nicely
        print representation
        of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
