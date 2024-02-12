#!/usr/bin/python3


"""testcase of city"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestText(unittest.TestCase):
    """TesTExt class"""

    def test_documentation(self):
        """Testcase for documentaion of the Baseclass and also the Textclass"""
        self.assertTrue(len(City.__doc__) > 2)
        self.assertTrue(len(TestText.__doc__) > 2)

    def test_filedocumentation(self):
        self.assertTrue(len(City.__doc__) > 2)
        self.assertTrue(len("__main__".__doc__) > 2)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_city_inherits_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_assignment(self):
        city = City()
        city.state_id = "state_123"
        city.name = "Test City"
        self.assertEqual(city.state_id, "state_123")
        self.assertEqual(city.name, "Test City")


if __name__ == "__main__":
    unittest.main()
