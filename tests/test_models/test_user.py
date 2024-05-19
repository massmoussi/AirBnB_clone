#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """TestUserClass resume """

    def test_is_instance(self):
        """ Test user """
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test field """
        my_user = User()
        self.assertTrue(isinstance(my_user.email, str))
        self.assertTrue(isinstance(my_user.password, str))
        self.assertTrue(isinstance(my_user.first_name, str))
        self.assertTrue(isinstance(my_user.last_name, str))


if __name__ == '__main__':
    unittest.main()
