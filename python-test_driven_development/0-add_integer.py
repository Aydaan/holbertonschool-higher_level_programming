#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""
def add_integer(a, b=98):
    """
    Return the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are cast to integers.
    Args:
        a (int or float): first number
        b (int or float, optional): second number (default 98)
    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
