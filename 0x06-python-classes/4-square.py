#!/usr/bin/python3
"""This square module generates the size of each object for us"""


class Square:
    """The major class at work here"""

    def __init__(self, size=0):  # The main attrib that specifies size
        if not isinstance(size, int):
            raise TypeError("size must be an Integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            # The parameter supplied become object size

    def area(self):
        return self.__size ** 2  # The area ofthe square is ready
    
    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
