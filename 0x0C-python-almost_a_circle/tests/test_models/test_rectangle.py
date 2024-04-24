#!/usr/bin/python3
""" test_rectangle module
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test for Rectangle class
    """
    @classmethod
    def setUpClass(self):
        self.s = Rectangle(3, 4, 1, 1)

    def test_id_assert_equal(self):
        self.assertEqual(1, Rectangle(3, 4, 1, 1, 1).id)
        self.assertEqual(4, Rectangle(10, 5, 0, 0, 4).id)

    def test_width_assert_equal(self):
        self.assertEqual(10, Rectangle(10, 5).width)

    def test_width_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 5, 0, 0, 4)

    def test_width_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_height_assert_equal(self):
        self.assertEqual(5, Rectangle(10, 5).height)

    def test_height_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "5", 0, 0, 4)

    def test_height_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_assert_equal(self):
        self.assertEqual(0, Rectangle(10, 5).x)

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

    def test___str___assert_True(self):
        self.assertEqual(
                ("[Rectangle] (1) 0/0 - 3/4",
                 Rectangle(3, 4, 0, 0, 1).__str__()))

    def test_to_dictionary_assert_equal(self):
        self.s.update(width=1, x=1, height=2, y=3, id=89)
        self.assertEqual({
                'x': 1, 'y': 3, 'id': 89, 'height': 2, 'width': 1},
                self.s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
