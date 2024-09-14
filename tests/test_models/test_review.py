#!/usr/bin/python3

"""Unittest for Review Class."""

import unittest

from models.review import Review

from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases Review class."""

    def test_instance(self):
        """test instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_class(self):
        """test instance."""
        review = Review()
        self.assertEqual(str(type(review)),
                         "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """test is_subclass."""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_text(self):
        """test is_subclass."""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")


if __name__ == "__main__":
    unittest.main()
