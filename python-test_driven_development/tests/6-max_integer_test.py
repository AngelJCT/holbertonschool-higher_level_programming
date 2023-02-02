#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class define a unittest file"""
    def test_max_integer(self):
        """This function define a test cases for max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, 7, 5, 4, 6]), 7)
        self.assertEqual(max_integer([1, 2, 5, 8, 9, 4]), 9)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5, -2, -1, 0, -6, -3, 1]), 1)
        self.assertEqual(max_integer([2, 2]), 2)
        self.assertEqual(max_integer([-4, -3, -2, -1, 0, -5]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5, -1]), -1)
        self.assertEqual(max_integer([100, 200, 150, -500, 360, 230, 300, 190]), 360)

if __name__ == "__main__":
    unittest.main()
