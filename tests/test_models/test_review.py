#!/usr/bin/python3
"""Unit test for the file storag """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """TestReviewClass test """

    def test_is_instance(self):
        """ Test user """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """ Test field of user """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review.place_id, str))
        self.assertTrue(isinstance(my_Review.user_id, str))
        self.assertTrue(isinstance(my_Review.text, str))


if __name__ == '__main__':
    unittest.main()
