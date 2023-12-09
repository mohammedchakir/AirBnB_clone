#!/usr/bin/python3
"""This module defines the City class, which inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a City with state_id and name attributes."""

    state_id = ""
    name = ""
