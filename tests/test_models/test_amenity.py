#!/usr/bin/python3
"""Unit testing module for the Amenity class."""

import time
import re
import json
import os
import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    """Test Cases for the class Amenity."""

    def setUp(self):
        """Prepares methods for testing."""
        pass

    def tearDown(self):
        """Dismantles or finalizes test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets the data in FileStorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Examines the instantiation of the Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Evaluates the attributes of the Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
