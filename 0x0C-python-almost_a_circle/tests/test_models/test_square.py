#!/usr/bin/python3

import unittest
from models.square import Square

"""tests class square functions"""

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_init_with_args(self):
        s = Square(6, 4, 2, 10)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_property(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update(self):
        s = Square(1)
        s.update(2, 3, 2, 1)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        s = Square(5, 2, 1, 10)
        expected_dict = {'id': 10, 'size': 5, 'x':2, 'y': 1}
        self.assertDictEqual(s.to_dictionary(), expected_dict)
