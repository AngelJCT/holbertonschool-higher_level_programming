#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_init_with_id(self):
        """Test case for initialization with id"""
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        b2 = Base(40)
        self.assertEqual(b2.id, 40)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_init_without_id(self):
        """Test case for initialization without id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_init_with_negative_id(self):
        """Test case for initialization with negative id"""
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)
        b2 = Base(-40)
        self.assertEqual(b2.id, -40)
        b3 = Base(-100)
        self.assertEqual(b3.id, -100)

    def test_nb_objects(self):
        """Test case for nb_objects"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_init_with_string_id(self):
        """Test case for initialization with string id"""
        b1 = Base("hello")
        self.assertEqual(b1.id, "hello")
        b2 = Base("world")
        self.assertEqual(b2.id, "world")
        b3 = Base("python")
        self.assertEqual(b3.id, "python")

if __name__ == '__main__':
    unittest.main()
