#!/usr/bin/python3
"""This module define a class for a rectangle"""


class Rectangle():
    """This class define a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initialize the class Rectangle"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This method returns the current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the current width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method returns the current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the current height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method gets the current area"""
        return self.__width * self.__height

    def perimeter(self):
        """This method gets the current perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This method prints a rectangle"""
        result = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                result += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    result += "\n"
        return result

    def __repr__(self):
        """This method returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the biggest rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __del__(self):
        """This method deletes an instance"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


obj = Rectangle
del obj
