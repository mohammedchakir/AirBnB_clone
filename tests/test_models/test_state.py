#!/usr/bin/python3
"""Unit testing module for the State class."""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models.state import State
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    """Test Cases for the class State."""

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
        """Evaluates the instantiation of the State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Evaluates the attributes of the State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()