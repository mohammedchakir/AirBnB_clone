#!/usr/bin/python3
"""Unit testing module for the Place class."""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models.place import Place
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):

    """Test Cases for the class Place."""

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
        """Evaluates the instantiation of the place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Evaluates the attributes of the place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
