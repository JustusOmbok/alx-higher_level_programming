#!/usr/bin/python3
"""unittest for function mav_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer(""), None)

    def test_string(self):

        string = "Breman"
        self.assertEqual(max_integer("Brennan"), 'r')

    def test_ints_floats(self):
        ints_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_floats), 15.5)


if __name__ == '__main__':
    unittest.main()
