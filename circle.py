"""
Author: Rugh1
Date: 06.9.2024
Description: circle class
"""
from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius: float | int, color: str) -> None:
        """
        Initialize a Circle object.

        :param radius: The radius of the circle.
        :type radius: float or int

        :param color: The color of the circle.
        :type color: str

        """
        if not ((type(radius) is int or type(radius) is float) and radius > 0):
            raise AssertionError
        super().__init__(radius * radius * pi, pi * radius * 2)
        self.radius = radius
        self.color = color
