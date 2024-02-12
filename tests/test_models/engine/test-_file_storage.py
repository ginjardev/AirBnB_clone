#!/usr/bin/python3

"""Testcase for storage """

import unittest
import models.base_model
import datetime
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
import os


class storageFile(unittest.TestCase):
    """Storagetext for testing the storage class"""

    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj1.name = "omotayo"

    def tearDown(self):
        """To Clean up: Remove the test file if it exists."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_documentation(self):
        """Testcase for documentaion of the Baseclass and also the Textclass"""
        self.assertTrue(len(FileStorage.__doc__) > 2)
        self.assertTrue(len(storageFile.__doc__) > 2)

    def test_filedocumentation(self):
        self.assertTrue(len(models.engine.file_storage.__doc__) > 2)
        self.assertTrue(len("__main__".__doc__) > 2)


class TestFileStorage_(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file1.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file1.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file1.json")
        except IOError:
            pass
        FileStorage.FileStorage_objects = {}

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageInstall(unittest.TestCase):
    """Unittests for testing instantiation."""

    def test_file_storage__no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_private_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
