#!/usr/bin/python3

"""Defines unittests"""

import unittest
import models.base_model
import datetime
from models.__init__ import storage
from models.base_model import BaseModel


class baseText(unittest.TestCase):
    """basetext for text the basemodel class"""

    def setUp(self):
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj1.name = "omotayo"

    def test_documentation(self):
        """Testcase for documentaion of the Baseclass and also the Textclass"""
        self.assertTrue(len(BaseModel.__doc__) > 2)
        self.assertTrue(len(baseText.__doc__) > 2)

    def test_filedocumentation(self):
        self.assertTrue(len(models.base_model.__doc__) > 2)
        self.assertTrue(len("__main__".__doc__) > 2)

    def test_objectId(self):
        """testing if the obj1 id is equal"""
        ans = self.obj1.id
        ans1 = self.obj2.id
        self.assertEqual(self.obj1.id, an)
        self.assertEqual(self.obj2.id, ans1)

    def test_objectId(self):
        """testing value instance assignment
        if its present on the obj1 instance"""

        self.obj1.name = "omotayo"
        self.obj2.name = "tee"
        self.assertEqual(self.obj1.name, "omotayo")
        self.assertEqual(self.obj2.name, "tee")

    def test_objectDate(self):
        """testing the date instances"""

        first = self.obj1.created_at
        second = self.obj2.created_at

        self.assertEqual(self.obj1.created_at, first)
        self.assertEqual(self.obj2.created_at, second)

    def test_rasises(self):
        """test to check if re-create an instance
        with this dictionary representation of another instance"""

        store = BaseModel(**self.obj1.to_dict())

        self.assertEqual(store.id, self.obj1.id)
        self.assertEqual(store.name, self.obj1.name)

    def test_rasises(self):
        """test to check if re-create an instance
        with this dictionary representation of another instance"""

        store = BaseModel(**self.obj1.to_dict())

        self.assertEqual(store.id, self.obj1.id)
        self.assertEqual(store.name, self.obj1.name)

    def test_attributes(self):
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertTrue(hasattr(self.obj1, "created_at"))
        self.assertTrue(hasattr(self.obj1, "updated_at"))

    def test_id_generation(self):
        """Test if id is a string"""
        self.assertIsInstance(self.obj1.id, str)

    def test_created_and_updated_at(self):
        """Test the 'created_at' and 'updated_at' attributes."""
        self.assertIsInstance(self.obj1.created_at, datetime.datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime.datetime)
        initial_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.assertGreater(self.obj1.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        self.assertIsInstance(self.obj1.to_dict(), dict)
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        for key in expected_keys:
            self.assertIn(key, self.obj1.to_dict())
        self.assertTrue(isinstance(self.obj1.to_dict()["created_at"], str))
        self.assertTrue(isinstance(self.obj1.to_dict()["updated_at"], str))
        self.assertEqual(self.obj1.to_dict()["__class__"], "BaseModel")

    def test_str_method(self):
        """str reprensentation"""
        str_repr = str(self.obj1)
        self.assertIsInstance(str_repr, str)

    def test_save_method_updates_updated_at(self):
        """test case to filr to a file"""

        initial_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.assertGreater(self.obj1.updated_at, initial_updated_at)

    def test_save_method_saves_to_storage(self):
        """test for storage"""

        initial_objects_count = len(storage.all())
        self.obj1.save()
        updated_objects_count = len(storage.all())
        self.assertEqual(updated_objects_count, initial_objects_count)

    def test_base_model_attributes(self):
        """Test the default attributes of a BaseModel instance."""
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertTrue(hasattr(self.obj1, "created_at"))
        self.assertTrue(hasattr(self.obj1, "updated_at"))

    def test_base_model_save(self):
        """Test the save method of a BaseModel instance."""
        initial_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(initial_updated_at, self.obj1.updated_at)

    def test_base_model_str(self):
        """Test the __str__ method of a BaseModel instance."""
        base_model_str = str(self.obj1)
        self.assertIsInstance(base_model_str, str)
        self.assertIn("BaseModel", base_model_str)
        self.assertIn(self.obj1.id, base_model_str)


if __name__ == "__main__":
    unittest.main()
