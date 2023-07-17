#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

"""tests for class rectangle functions"""

class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(7, 2, 0, 7)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 7)

    def test_area(self):
        r = Rectangle(7, 2)
        self.assertEqual(r.area(), 14)

    def test_str(self):
        r = Rectangle(8, 12, 4, 2, 24)
        expected_output = "[Rectangle] (24) 4/2 - 8/12"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        r = Rectangle(5, 5)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(20, 40, 4, 8, 1)
        expected_dict = {'id': 1, 'width': 20, 'height': 40, 'x': 4, 'y': 8}
        self.assertEqual(r.to_dictionary(), expected_dict)
