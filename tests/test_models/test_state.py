#!/usr/bin/python3


"""Unittest for State Class."""

import unittest

from models.state import State

from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases State class."""

    def test_instance(self):
        """test instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_is_class(self):
        """test instance."""
        state = State()
        self.assertEqual(str(type(state)),
                         "<class 'models.state.State'>")

    def test_is_subclass(self):
        """test is_subclass."""
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attr(self):
        """test is_subclass."""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
