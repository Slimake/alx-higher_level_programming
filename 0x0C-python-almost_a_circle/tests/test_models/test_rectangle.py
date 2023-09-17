import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_rectangle(self):
        self.assertEqual(Rectangle(10, 2).id, 3)
        self.assertEqual(Rectangle(2, 10).id, 4)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(1, 3, 2, 0, 5).x, 2)
        self.assertEqual(Rectangle(3, 3, 0, 4, 5).y, 4)
        self.assertEqual(Rectangle(-1, -3, 0, 0, 5).width, -1)
        self.assertEqual(Rectangle(-1, -3, 0, 0, 5).height, -3)
        self.assertEqual(Rectangle(-1, -3, 0, 0, 5).height, -3)
        self.assertEqual(Rectangle(float("inf"), float("NaN"),
                                   0, 0, 2).width, float("inf"))
        self.assertNotEqual(Rectangle(4, float("NaN"),
                                      0, 0, 2).height, float("NaN"))
