#!/usr/bin/python3


"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import time
import uuid
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel ."""

    def test_instance(self):
        """test instance."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_is_class(self):
        """test instance."""
        base = BaseModel()
        self.assertEqual(str(type(base)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """test save."""
        base = BaseModel()
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)
        self.assertTrue(base.updated_at > base.created_at)

    def test_save_file(self):
        """test save."""
        if os.path.isfile("file.json"):
            os.remove(os.path.join("file.json"))
            print(os.path.isfile("file.json"))
        base = BaseModel()
        print(base.id)
        time.sleep(1)
        base.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", 'w') as file:
            serialized_content = json.load(file)
            for item in serialized_content.values():
                self.assertIsNotNone(item['__class__'])

    def test_str_(self):
        """test str."""
        base = BaseModel()

        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(base)
            self.assertEqual(fake_out.getvalue(),
                             "[{}] ({}) {}\n".format(base.__class__.__name__,
                                                     base.id,
                                                     base.__dict__))

    def test_to_dict(self):
        """test dict."""
        base = BaseModel()
        dict_repr = base.to_dict()
        self.assertTrue(dict_repr['__class__'] == base.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
