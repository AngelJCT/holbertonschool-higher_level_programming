#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_nb_objects(self):
        """Test case for nb_objects"""
        initial_nb_objects = Base._Base__nb_objects
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        r3 = Rectangle(10, 2)
        final_nb_objects = Base._Base__nb_objects
        self.assertEqual(final_nb_objects, initial_nb_objects + 3)

    def test_init(self):
        """Test case for initialization"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_init_with_id(self):
        """Test case for initialization with id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(10, 2, 0, 0, 40)
        self.assertEqual(r2.id, 40)
        r3 = Rectangle(10, 2, 0, 0, 100)
        self.assertEqual(r3.id, 100)

    def test_init_with_negative_id(self):
        """Test case for initialization with negative id"""
        r1 = Rectangle(10, 2, 0, 0, -1)
        self.assertEqual(r1.id, -1)
        r2 = Rectangle(10, 2, 0, 0, -40)
        self.assertEqual(r2.id, -40)
        r3 = Rectangle(10, 2, 0, 0, -100)
        self.assertEqual(r3.id, -100)


if __name__ == '__main__':
    unittest.main()
