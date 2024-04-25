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
        self.base = Base()
        self.rect = Rectangle(10, 7, 2, 8)
        self.to_json = Base.to_json_string([self.rect.to_dictionary()])

    def test_id_assert_equal(self):
        self.assertEqual(1, self.base.id)
        self.assertEqual(12, Base(12).id)
        self.assertEqual(1, self.base.id)
        self.assertEqual(int(float(3.4)), Base(3).id)

    def test_to_json_string_assert_equal(self):
        self.assertEqual(
                '[{"id": 2, "width": 10, "height": 7, "x": 2, "y": 8}]',
                self.to_json)

    def test_from_json_string_assert_equal(self):
        self.assertEqual(
                [{"x": 2, "width": 10, "id": 2, "height": 7, "y": 8}],
                Base.from_json_string(self.to_json))


if __name__ == "__main__":
    unittest.main()
