#!/usr/bin/python3
"""Module square that inherits from Rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
            return arg
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
            return v
