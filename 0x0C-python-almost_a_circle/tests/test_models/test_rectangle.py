import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_rectangle(self):
        self.assertEqual(Rectangle(10, 2).id, 3)
        self.assertEqual(Rectangle(2, 10).id, 4)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(1, 3, 2, 0, 5).x, 2)
        self.assertEqual(Rectangle(3, 3, 0, 4, 5).y, 4)
        self.assertEqual(Rectangle(2, 3, 0, 0, 5).width, 2)
        self.assertEqual(Rectangle(1, 3, 0, 0, 5).height, 3)
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

        with self.assertRaises(TypeError):
            Rectangle("2", 3, 0, 0, 5).width

        with self.assertRaises(TypeError):
            Rectangle(2, "3", 0, 0, 5).height

        with self.assertRaises(TypeError):
            Rectangle(2, 3, "4", 0, 5).x

        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, "5", 5).y

        with self.assertRaises(TypeError):
            Rectangle(float("inf"), 3, 0, 0, 2).width

        with self.assertRaises(TypeError):
            Rectangle(2, float("NaN"), 0, 0, 2).height

        with self.assertRaises(ValueError):
            Rectangle(-2, 3, 0, 0, 5).width

        with self.assertRaises(ValueError):
            Rectangle(2, 0, 0, 0, 5).height

        with self.assertRaises(ValueError):
            Rectangle(2, 3, -4, 0, 5).x

        with self.assertRaises(ValueError):
            Rectangle(2, 3, 4, -5, 5).y

        with self.assertRaises(ValueError):
            Rectangle(-2, 3).area
