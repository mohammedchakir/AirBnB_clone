#!/usr/bin/python3
"""This module defines the Review class, which inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines a Review with place_id, user_id, and text attributes.
    """

    place_id = ""
    user_id = ""
    text = ""
