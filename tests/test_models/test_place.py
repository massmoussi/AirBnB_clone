#!/usr/bin/python3
"""Unit test class Place """

import unittest
# import json
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """TestPlaceClass test """

    def test_is_instance(self):
        """ Test """
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))

    def test_field_types(self):
        """ Test field attributes of place """
        self.assertTrue(isinstance(Place.city_id, str))
        self.assertTrue(isinstance(Place.user_id, str))
        self.assertTrue(isinstance(Place.name, str))
        self.assertTrue(isinstance(Place.description, str))
        self.assertTrue(isinstance(Place.number_rooms, int))
        self.assertTrue(isinstance(Place.number_bathrooms, int))
        self.assertTrue(isinstance(Place.max_guest, int))
        self.assertTrue(isinstance(Place.price_by_night, int))
        self.assertTrue(isinstance(Place.latitude, float))
        self.assertTrue(isinstance(Place.longitude, float))


if __name__ == '__main__':
    unittest.main()
