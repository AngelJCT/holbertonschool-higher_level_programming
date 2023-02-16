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

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_id_none(self):
        """Test case for initialization without id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """Test case for initialization with id"""
        b2 = Base(40)
        self.assertEqual(b2.id, 40)

    def test_nb_objects(self):
        """Test case for initialization without id and increment"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_to_json_string_none(self):
        """Test case for to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """Test case for to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

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
            self.assertEqual(f.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_create_rectangle(self):
        """Test case for creating a rectangle"""
        r1 = Rectangle(3, 5, 1, 1)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """test case for creating a square"""
        sqr1 = Square(5)
        dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**dictionary)
        self.assertEqual(sqr1 == sqr2, False)
        self.assertEqual(sqr1 is sqr2, False)
        self.assertNotEqual(sqr1, sqr2)

    def test_from_json_string(self):
        """Test case for from_jason_string"""
        json_list = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        list_objs = Base.from_json_string(json_list)
        self.assertEqual(len(list_objs), 1)

    def test_from_json_string_none(self):
        """Test case for from_json_string with none as argument"""
        list_objs = Base.from_json_string(None)
        self.assertEqual(list_objs, [])

    def test_load_from_file(self):
        """Test case for load_from_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 2)
        self.assertEqual(list_rectangles[0].id, 1)
        Rectangle.save_to_file(None)
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 0)
        Rectangle.save_to_file([])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 0)


if __name__ == '__main__':
    unittest.main()
