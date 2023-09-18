import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):

    def test_square(self):
        self.assertEqual(Square(2).width, 2)
        self.assertEqual(Square(1, 3, 2).x, 3)
        self.assertEqual(Square(3, 3, 4).y, 4)
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(8, 7, 4, 12).id, 12)

        with self.assertRaises(TypeError):
            Square("2", 0, 0, 5).width

        with self.assertRaises(TypeError):
            Square(2, "4", 0, 5).x

        with self.assertRaises(TypeError):
            Square(2, 4, "5", 5).y

        with self.assertRaises(TypeError):
            Square(float("inf"), 0, 0, 2).width

        with self.assertRaises(ValueError):
            Square(-2, 0, 0, 5).width

        with self.assertRaises(ValueError):
            Square(2, -4, 0, 5).x

        with self.assertRaises(ValueError):
            Square(2, 4, -5, 5).y

        with self.assertRaises(ValueError):
            Square(-2).area
