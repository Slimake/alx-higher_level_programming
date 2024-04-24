#!/usr/bin/python3
""" Test base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ Test for Base class
    """
    @classmethod
    def setUpClass(self):
        self.rect = Rectangle(10, 7, 2, 8).to_dictionary()

    def test_id_assert_equal(self):
        self.assertEqual(2, Base().id)
        self.assertEqual(12, Base(12).id)
        self.assertEqual(3, Base().id)
        self.assertEqual(int(float(3.4)), Base(3).id)

    def test_id_assert_true(self):
        self.assertTrue(2, Base().id)
        self.assertTrue(12, Base(12).id)
        self.assertTrue(3, Base().id)
        self.assertTrue(int(float(3.4)), Base(3).id)

    def test_to_json_string_assert_true(self):
        self.assertTrue(
                [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}],
                Base.to_json_string([self.rect]))


if __name__ == "__main__":
    unittest.main()
