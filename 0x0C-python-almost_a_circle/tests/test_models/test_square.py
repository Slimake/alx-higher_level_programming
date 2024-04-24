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

    def test_id_assert_equal(self):
        self.assertEqual(4, Square(2, 0, 0, 4).id)

    def test_x_assert_equal(self):
        self.assertEqual(0, Square(5).x)

    def test_x_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square(5, "1", 0, 4).x

    def test_x_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(5, -3)

    def test_y_assert_equal(self):
        self.assertEqual(0, Square(5).y)

    def test_y_assert_raises_type(self):
        with self.assertRaises(TypeError):
            Square(5, 1, "1", 4).y

    def test_y_assert_raises_value(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_area_assert_equal(self):
        self.assertEqual(9, Square(3).area())

    def test___str___assert_equal(self):
        self.assertEqual("[Square] (1) 0/0 - 3", Square(3, 0, 0, 1).__str__())

    def test_size_assert_equal(self):
        self.s.size = 9
        self.assertEqual(9, self.s.size)

    def test_update_assert_equal(self):
        self.assertEqual(1, self.s.y)

    def test_to_dictionary_assert_equal(self):
        self.s.update(size=7, id=89, y=1)
        self.assertEqual({
                'x': 0, 'y': 1, 'id': 89, 'size': 7},
                self.s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
