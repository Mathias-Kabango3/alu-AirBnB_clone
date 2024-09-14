#!/usr/bin/python3

"""Unittest for Place Class."""

import unittest

from models.place import Place
from models.city import City
from models.user import User

from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases Place class."""

    def test_instance(self):
        """test instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_is_class(self):
        """test instance."""
        place = Place()
        self.assertEqual(str(type(place)),
                         "<class 'models.place.Place'>")

    def test_is_subclass(self):
        """test is_subclass."""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_is_attr(self):
        """test instance."""
        city = City()
        user = User()
        place = Place()
        place.user_id = user.id
        place.city_id = city.id
        self.assertIsNotNone(place.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
