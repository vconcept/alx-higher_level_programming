#!/usr/bin/python3
"""This module gives us the shape/size/dimension of a rectangle, together with calculation"""
class Rectangle:
    """This is a class of triangle"""
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    @property
    def width(self):
        return self.__width

    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value
    

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle
        
        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
