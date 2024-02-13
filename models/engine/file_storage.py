#!/usr/bin/python3

"""A class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import models


class FileStorage:
    """A Storage Engine of instances"""

    dict_val = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
    }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """A method that update the class
        attribute object before the save is been call"""

        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects.update({key: obj})

    def save(self):
        """An object that serializes object into json file"""
        load_instance_to_dictionaries = {
            key: value.to_dict() for key, value in type(self).__objects.items()
        }
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(load_instance_to_dictionaries, file)

    def reload(self):
        """A method that deserialize json file"""

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                hold = json.load(file)

            for key, value in hold.items():
                obj = self.dict_val[value["__class__"]](**value)
                self.__objects[key] = obj
        except Exception:
            pass
