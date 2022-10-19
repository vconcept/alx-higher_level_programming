#!/usr/bin/python3
"""

This module adds up two integers

"""

def add_integer(a, b=98):
    """This function takes two arguments and add the values if they are numbers
    Arguments: a, b - and they must be int or float, else, an exception is raised
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(b, (float)):
        b = int(b)
    return a + b
