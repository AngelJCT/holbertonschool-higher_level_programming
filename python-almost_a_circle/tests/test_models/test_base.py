#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_init_without_id(self):
        """Test case for initialization without id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_with_id(self):
        """Test case for initialization with id"""
        b2 = Base(40)
        self.assertEqual(b2.id, 40)

    def test_nb_objects(self):
        """Test case for nb_objects"""
        initial_nb_objects = Base._Base__nb_objects
        b1 = Base()
        b2 = Base()
        b3 = Base()
        final_nb_objects = Base._Base__nb_objects
        self.assertEqual(final_nb_objects, initial_nb_objects + 3)


if __name__ == '__main__':
    unittest.main()
