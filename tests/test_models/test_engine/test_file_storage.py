#!/usr/bin/python3
"""Unit testing module for the FileStorage class."""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Cases for the class FileStorage."""

    def setUp(self):
        """Prepares test methods."""
        pass

    def resetStorage(self):
        """Clears FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Finalizes or cleans up test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Evaluates the instantiation of the Storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_3_init_no_args(self):
        """Evaluates the __init__ method with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Evaluates the __init__ method with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Examines the class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """
        Conducts helper tests for the all() method specific to
        the given class name.
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_5_all_base_model(self):
        """Conducts tests for the all() method in the BaseModel class."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Conducts tests for the all() method in the User class."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Conducts tests for the all() method in the State class."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Conducts tests for the all() method in the City class."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Conducts tests for the all() method in the Amenity class."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Conducts tests for the all() method in the Place class."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Conducts tests for the all() method in the Review class."""
        self.help_test_all("Review")

    def help_test_all_multiple(self, classname):
        """
        Conducts helper tests for the all() method with multiple objects
        specific to the given class name.
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_5_all_multiple_base_model(self):
        """Conducts tests for the all() method with multiple objects."""
        self.help_test_all_multiple("BaseModel")

    def test_5_all_multiple_user(self):
        """Conducts tests for the all() method for User."""
        self.help_test_all_multiple("User")

    def test_5_all_multiple_state(self):
        """Conducts tests for the all() method for State."""
        self.help_test_all_multiple("State")

    def test_5_all_multiple_city(self):
        """Conducts tests for the all() method for City."""
        self.help_test_all_multiple("City")

    def test_5_all_multiple_amenity(self):
        """Conducts tests for the all() method for Amenity."""
        self.help_test_all_multiple("Amenity")

    def test_5_all_multiple_place(self):
        """Conducts tests for the all() method for Place."""
        self.help_test_all_multiple("Place")

    def test_5_all_multiple_review(self):
        """Conducts tests for the all() method for Review."""
        self.help_test_all_multiple("Review")

    def test_5_all_no_args(self):
        """Evaluates the all() method with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_all_excess_args(self):
        """Examines the all() method with an excessive number of arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_new(self, classname):
        """Assists in testing the new() method specific to given class name."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)

    def test_5_new_base_model(self):
        """Conducts tests for the new() method in the BaseModel class."""
        self.help_test_new("BaseModel")

    def test_5_new_user(self):
        """Conducts tests for the new() method for User."""
        self.help_test_new("User")

    def test_5_new_state(self):
        """Conducts tests for the new() method for State."""
        self.help_test_new("State")

    def test_5_new_city(self):
        """Conducts tests for the new() method for City."""
        self.help_test_new("City")

    def test_5_new_amenity(self):
        """Conducts tests for the new() method for Amenity."""
        self.help_test_new("Amenity")

    def test_5_new_place(self):
        """Conducts tests for the new() method for Place."""
        self.help_test_new("Place")

    def test_5_new_review(self):
        """Conducts tests for the new() method for Review."""
        self.help_test_new("Review")

    def test_5_new_no_args(self):
        """Conducts tests for the new() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def test_5_new_excess_args(self):
        """Conducts tests for the new() with too many arguments."""
        self.resetStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_save(self, classname):
        """Assists in testing the save() method specific to given class name"""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: o.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_5_save_base_model(self):
        """Conducts tests for the save() method in the BaseModel class."""
        self.help_test_save("BaseModel")

    def test_5_save_user(self):
        """Conducts tests for the save() method for User."""
        self.help_test_save("User")

    def test_5_save_state(self):
        """Conducts tests for the save() method for State."""
        self.help_test_save("State")

    def test_5_save_city(self):
        """Conducts tests for the save() method for City."""
        self.help_test_save("City")

    def test_5_save_amenity(self):
        """Conducts tests for the save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_5_save_place(self):
        """Conducts tests for the save() method for Place."""
        self.help_test_save("Place")

    def test_5_save_review(self):
        """Conducts tests for the save() method for Review."""
        self.help_test_save("Review")

    def test_5_save_no_args(self):
        """Conducts tests for the save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Conducts tests for the save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_reload(self, classname):
        """
        Assists in testing the reload() method specific to
        the given class name.
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        storage.reload()
        self.assertEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_base_model(self):
        """Conducts tests for the reload() method for BaseModel."""
        self.help_test_reload("BaseModel")

    def test_5_reload_user(self):
        """Conducts tests for the reload() method for User."""
        self.help_test_reload("User")

    def test_5_reload_state(self):
        """Conducts tests for the reload() method for State."""
        self.help_test_reload("State")

    def test_5_reload_city(self):
        """Conducts tests for the reload() method for City."""
        self.help_test_reload("City")

    def test_5_reload_amenity(self):
        """Conducts tests for the reload() method for Amenity."""
        self.help_test_reload("Amenity")

    def test_5_reload_place(self):
        """Conducts tests for the reload() method for Place."""
        self.help_test_reload("Place")

    def test_5_reload_review(self):
        """Conducts tests for the reload() method for Review."""
        self.help_test_reload("Review")

    def help_test_reload_mismatch(self, classname):
        """
        Assists in testing the reload() method specific to
        the given class name.
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        o.name = "Laura"
        storage.reload()
        self.assertNotEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_mismatch_base_model(self):
        """
        Conducts tests for a mismatch in the reload() method for
        the BaseModel class.
        """
        self.help_test_reload_mismatch("BaseModel")

    def test_5_reload_mismatch_user(self):
        """Conducts tests for a mismatch in the reload() method for User."""
        self.help_test_reload_mismatch("User")

    def test_5_reload_mismatch_state(self):
        """Conducts tests for a mismatch in the reload() method for State."""
        self.help_test_reload_mismatch("State")

    def test_5_reload_mismatch_city(self):
        """Conducts tests for a mismatch in the reload() method for City."""
        self.help_test_reload_mismatch("City")

    def test_5_reload_mismatch_amenity(self):
        """Conducts tests for a mismatch in the reload() method for Amenity."""
        self.help_test_reload_mismatch("Amenity")

    def test_5_reload_mismatch_place(self):
        """Conducts tests for a mismatch in the reload() method for Place."""
        self.help_test_reload_mismatch("Place")

    def test_5_reload_mismatch_review(self):
        """Conducts tests for a mismatch in the reload() method for Review."""
        self.help_test_reload_mismatch("Review")

    def test_5_reload_no_args(self):
        """Evaluates the reload() method with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_excess_args(self):
        """Examines the reload() method with an many of arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()