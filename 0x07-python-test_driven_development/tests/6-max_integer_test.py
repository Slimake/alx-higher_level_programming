#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_num(self):
        self.assertEqual(None, max_integer([]))
        self.assertEqual(1, max_integer([1]))
        self.assertEqual(4, max_integer([1, 2, 3, 4]))
        self.assertEqual(-1, max_integer([-1, -2, -3, -4]))
        self.assertEqual(4, max_integer([1, 2, True, 4]))
        self.assertEqual(5, max_integer([1, float("NaN"), 5, 4]))
        self.assertEqual(float(1.9e3234), max_integer([1, float(1.89e323423), 3, 4]))

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, [1, 3], 3, 4])
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
