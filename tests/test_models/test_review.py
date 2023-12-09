#!/usr/bin/python3
"""Unit testing module for the Review class.."""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models.review import Review
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):

    """Test Cases for the class Review."""

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
        """Evaluates the instantiation of the Review class."""
        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Evaluates the attributes of the Review class."""
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
