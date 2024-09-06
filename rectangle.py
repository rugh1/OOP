"""
Author: Rugh1
Date: 06.9.2024
Description: rectangle class
"""
from shape import Shape


class Rectangle(Shape):
    def __init__(self, side1: float | int, side2: float | int, color: str) -> None:
        """
        Initialize a Rectangle object.

        :param side1: Length of the first side of the rectangle.
        :type side1: float or int

        :param side2: Length of the second side of the rectangle.
        :type side2: float or int

        :param color: The color of the rectangle.
        :type color: str

        """
        if not ((type(side1) is int or type(side1) is float) and side1 > 0):
            raise AssertionError
        if not ((type(side2) is int or type(side2) is float) and side2 > 0):
            raise AssertionError
        super().__init__(side1 * side2, (side1 + side2) * 2)
        self.side1 = side1
        self.side2 = side2
        self.color = color

    def __add__(self, shape: Shape) -> Shape:
        """
        Add the areas and perimeters of two shapes.

        :param shape: Another shape to add.
        :type shape: Shape

        :return: A new Shape object with combined area and perimeter.
        :rtype: Shape
        """
        return Shape(self.area + shape.area, self.perimeter + shape.perimeter)
