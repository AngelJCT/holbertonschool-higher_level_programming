#!/usr/bin/python3
"""Unittest for Square class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """Test case for non-list arguments"""
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s3 = Square(1, 2, 3, 5)
        self.assertEqual(s3.id, 5)
        self.assertEqual(s3.width, 1)
        self.assertEqual(s3.height, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

    def test_square_with_negative_arguments(self):
        """Test case for negative arguments"""
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 10, -3)
        self.assertRaises(ValueError, Square, 10, 3, -4)

    def test_square_with_zero_arguments(self):
        """Test case for zero arguments"""
        self.assertRaises(ValueError, Square, 0)

    def test_square_with_non_list_argument(self):
        """Test case for non-list arguments"""
        self.assertRaises(TypeError, Square, "10")
        self.assertRaises(TypeError, Square, 10, "5")
        self.assertRaises(TypeError, Square, 10, 5, "3")

    def test_area(self):
        """Test case for area method"""
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)

    def test_str_square(self):
        """Test case for __str__ method"""
        s1 = Square(1, 2, 3, 5)
        self.assertEqual(s1.__str__(), "[Square] (5) 2/3 - 1")

    def test_update(self):
        """Test case for update method"""
        s1 = Square(1, 2, 3, 5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/3 - 2")


if __name__ == '__main__':
    unittest.main()
