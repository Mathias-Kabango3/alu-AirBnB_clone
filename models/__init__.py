#!/usr/bin/python3
"""The __init__ method for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
