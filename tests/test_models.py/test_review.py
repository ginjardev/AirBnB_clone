#!/usr/bin/python3

"""Test case for review """


import models
from models.review import Review

import contextlib
import os
import unittest
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """testing save method of the Review class."""

    @classmethod
    def setUpClass(cls) -> None:
        with contextlib.suppress(IOError):
            os.rename("file.json", "tmp")

    def tearDown(self) -> None:
        with contextlib.suppress(IOError):
            os.remove("file.json")
        with contextlib.suppress(IOError):
            os.rename("tmp", "file.json")

    def test_one_save(self) -> None:
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_two_saves(self) -> None:
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_save_with_arg(self) -> None:
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updates_file(self) -> None:
        rev = Review()
        rev.save()
        rvid = f"Review.{rev.id}"
        with open("file.json", "r", encoding="utf-8") as file:
            self.assertIn(rvid, file.read())


class TestReview_instantance(unittest.TestCase):
    """testing instantiation of the Review class."""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_is_public_class(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)


if __name__ == "__main__":
    unittest.main()
