#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """Test case for non-list arguments"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_rectangle_with_negative_arguments(self):
        """Test case for negative arguments"""
        self.assertRaises(ValueError, Rectangle, 10, -2)
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(ValueError, Rectangle, 10, 2, -3)
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -4)

    def test_rectangle_with_zero_arguments(self):
        """Test case for zero arguments"""
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_rectangle_with_non_list_argument(self):
        """Test case for non-list arguments"""
        self.assertRaises(TypeError, Rectangle, 2, "10")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 10, 2, "5")
        self.assertRaises(TypeError, Rectangle, 10, 2, 5, "3")

    def test_area(self):
        """Test case for area method"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    def test_str_rectangle(self):
        """Test case for __str__ method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """Test case for display method"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.display(), None)


if __name__ == "__main__":
    unittest.main
