#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

store = getenv("HBNB_TYPE_STORAGE", 'file')
if store == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif store == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
