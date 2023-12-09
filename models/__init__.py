#!/usr/bin/python3
"""
This module initializes the storage variable, an instance of FileStorage,
and calls reload() on this variable.
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
