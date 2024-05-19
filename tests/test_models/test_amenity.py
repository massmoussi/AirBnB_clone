#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenityClass(unittest.TestCase):

    def test_is_instance(self):
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity, BaseModel))

    def test_field_types(self):
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity.name, str))


if __name__ == '__main__':
    unittest.main()
