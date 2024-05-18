#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.engine import storage


storage = FileStorage()
storage.reload()
