#!/usr/bin/python3
"""This module defines the User class, which inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines a User with email, password, first_name,
    and last_name attributes.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""