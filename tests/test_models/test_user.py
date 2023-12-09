#!/usr/bin/python3
"""Unit testing module for the User class."""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    """Test Cases for the class User."""

    def setUp(self):
        """Prepares test methods."""
        pass

    def tearDown(self):
        """Finalizes or cleans up test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Clears FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Evaluates the instantiation of the User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Evaluates the attributes of the User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
