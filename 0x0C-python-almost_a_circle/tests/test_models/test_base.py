#!/usr/bin/python3
""" Test base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test for Base class
    """
    def test_id_assert_equal(self):
        self.assertEqual(1, Base().id)
        self.assertEqual(12, Base(12).id)
        self.assertEqual(2, Base().id)
        self.assertEqual(int(float(3.4)), Base(3).id)

    def test_id_assert_true(self):
        self.assertTrue(1, Base().id)
        self.assertTrue(12, Base(12).id)
        self.assertTrue(2, Base().id)
        self.assertTrue(int(float(3.4)), Base(3).id)


if __name__ == "__main__":
    unittest.main()
