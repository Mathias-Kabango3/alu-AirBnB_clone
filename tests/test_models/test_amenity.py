#!/usr/bin/python3

"""Unittest for Amenity Class."""

import unittest

from models.amenity import Amenity

from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for  Amenity class."""

    def test_instance(self):
        """test instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_is_class(self):
        """test instance."""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")

    def test_is_subclass(self):
        """test is_subclass."""
        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attr(self):
        """test is_subclass."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertIsNotNone(amenity.id)


if __name__ == "__main__":
    unittest.main()
