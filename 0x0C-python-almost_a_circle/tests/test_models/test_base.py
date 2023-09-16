import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_base(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(-3).id, -3)
        self.assertNotEqual(Base(float('NAN')).id, float('NAN'))
        self.assertEqual(Base(float('inf')).id, float('inf'))
