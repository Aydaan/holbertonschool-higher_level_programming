#!/usr/bin/env python3
"""
Module demonstrating abstract classes and duck typing.
"""
from abc import ABC, abstractmethod
PI = 3.141592653589793
class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    @abstractmethod
    def area(self):
        """
        Return the area of the shape.
        """
        pass
    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the shape.
        """
        pass
class Circle(Shape):
    """
    Circle shape.
    """
    def __init__(self, radius):
        """
        Initialize the circle.
        """
        self.radius = radius
    def area(self):
        """
        Return the area of the circle.
        """
        return PI * (self.radius ** 2)
    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return 2 * PI * self.radius
class Rectangle(Shape):
    """
    Rectangle shape.
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle.
        """
        self.width = width
        self.height = height
    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height
    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)
def shape_info(shape):
    """
    Print the area and perimeter of any shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
