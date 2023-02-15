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

    def test_without_id_and_increment(self):
        """Test case for initialization without id and increment"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 8)
        self.assertEqual(b2.id, 9)
        self.assertEqual(b3.id, 10)

    def test_nb_objects(self):
        """Test case for nb_objects"""
        initial_nb_objects = Base._Base__nb_objects
        b1 = Base()
        b2 = Base()
        b3 = Base()
        final_nb_objects = Base._Base__nb_objects
        self.assertEqual(final_nb_objects, initial_nb_objects + 3)

    def test_to_json_string_none(self):
        """Test case for to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """Test case for to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 7, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_save_to_file_none(self):
        """Test case for save_to_file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Test case for save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 6, "width": 2, "height": 4, "x": 0, "y": 0}]')


if __name__ == '__main__':
    unittest.main()
