#!/usr/bin/python3

import unittest
from models.base import Base

"""tests base class functions"""

class TestBase(unittest.TestCase):

    def test_base_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(100)
        self.assertEqual(base3.id, 100)

        base4 = Base()
        self.assertEqual(base4.id, 3)
