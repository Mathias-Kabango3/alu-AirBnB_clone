#!/usr/bin/python3
"""Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attribute:
        name (str): Name of amenity.
    """

    name = ""
