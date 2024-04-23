#!/usr/bin/python3
""" test_square module
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Test for Square class
    """
    @classmethod
    def setUpClass(self):
        self.s = Square(3)
        self.s.update(size=7, id=89, y=1)
        self.s.size = 9

    def test_id_assert_equal(self):
        self.assertTrue(1, Square(5).id)
        self.assertTrue(2, Square(2, 0, 0, 2).id)

    def test_width_assert_equal(self):
        self.assertEqual(5, Square(5).width)

    def test_width_assert_true(self):
        self.assertTrue(10, Square(5, 10).width)

    def test_width_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square("5", 0, 0, 4)

    def test_width_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(0, 5)

    def test_height_assert_equal(self):
        self.assertEqual(10, Square(10).height)

    def test_height_assert_true(self):
        self.assertTrue(10, Square(10).height)

    def test_height_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square("10", 0, 0, 4)

    def test_height_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_assert_equal(self):
        self.assertEqual(0, Square(5).x)

    def test_x_assert_true(self):
        self.assertTrue(1, Square(5, 1, 1).x)

    def test_x_assert_false(self):
        self.assertFalse(0, Square(5).x)

    def test_x_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square(5, "1", 0, 4).x

    def test_x_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(5, -3)

    def test_y_assert_equal(self):
        self.assertEqual(0, Square(5).y)

    def test_y_assert_true(self):
        self.assertTrue(1, Square(5, 1, 1).y)

    def test_y_assert_false(self):
        self.assertFalse(0, Square(5).y)

    def test_y_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square(5, 1, "1", 4).y

    def test_y_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_area_assert_equal(self):
        self.assertEqual(9, Square(3).area())

    def test_area_assert_true(self):
        self.assertTrue(16, Square(4).area())

    def test___str___assert_true(self):
        self.assertTrue("[Square] (1) 4/4 - 2/2", Square(2, 4, 4))

    def test_size_assert_equal(self):
        self.assertEqual(9, self.s.size)

    def test_update_assert_equal(self):
        self.assertEqual(1, self.s.y)


if __name__ == "__main__":
    unittest.main()
