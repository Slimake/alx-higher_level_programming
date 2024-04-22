#!/usr/bin/python3
""" test_rectangle module
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test for Rectangle class
    """
    def test_id_assert_equal(self):
        self.assertTrue(1, Rectangle(10, 5, 0, 0).id)
        self.assertTrue(4, Rectangle(10, 5, 0, 0, 4).id)

    def test_width_assert_equal(self):
        self.assertEqual(10, Rectangle(10, 5).width)

    def test_width_assert_true(self):
        self.assertTrue(10, Rectangle(10, 5).width)

    def test_width_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 5, 0, 0, 4)

    def test_width_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_height_assert_equal(self):
        self.assertEqual(5, Rectangle(10, 5).height)

    def test_height_assert_true(self):
        self.assertTrue(5, Rectangle(10, 5).height)

    def test_height_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "5", 0, 0, 4)

    def test_height_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_assert_equal(self):
        self.assertEqual(0, Rectangle(10, 5).x)

    def test_x_assert_true(self):
        self.assertTrue(1, Rectangle(10, 5, 1, 1).x)

    def test_x_assert_false(self):
        self.assertFalse(0, Rectangle(10, 5).x)

    def test_x_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "1", 0, 4).x

    def test_x_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1)

    def test_y_assert_equal(self):
        self.assertEqual(0, Rectangle(10, 5).y)

    def test_y_assert_true(self):
        self.assertTrue(1, Rectangle(10, 5, 1, 1).y)

    def test_y_assert_false(self):
        self.assertFalse(0, Rectangle(10, 5).y)

    def test_y_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 1, "1", 4).y

    def test_y_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 0, -1)

    def test_area_assert_equal(self):
        self.assertEqual(56, Rectangle(8, 7).area())

    def test_area_assert_True(self):
        self.assertTrue(6, Rectangle(3, 2).area())


if __name__ == "__main__":
    unittest.main()
