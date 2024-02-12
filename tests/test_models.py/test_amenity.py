#!/usr/bin/python3

"""Testcase for Amentity"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        hold = Amenity()
        self.assertIn("id", hold.to_dict())
        self.assertIn("created_at", hold.to_dict())
        self.assertIn("updated_at", hold.to_dict())
        self.assertIn("__class__", hold.to_dict())

    def test_to_dict_contains_added_attributes(self):
        hold = Amenity()
        hold.middle_name = "Holbert"
        hold.my_number = 9
        self.assertEqual("Holbert", hold.middle_name)
        self.assertIn("my_number", hold.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        hold = Amenity()
        am_dict = hold.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        hold = Amenity()
        hold.id = "123456"
        hold.created_at = hold.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Amenity",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(hold.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        hold = Amenity()
        self.assertNotEqual(hold.to_dict(), hold.__dict__)

    def test_to_dict_with_arg(self):
        hold = Amenity()
        with self.assertRaises(TypeError):
            hold.to_dict(None)


class TestAmenitysave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


if __name__ == "__main__":
    unittest.main()
