"""
Author: Rugh1
Date: 06.9.2024
Description: square class
"""
from shape import Shape


class Square(Shape):
    def __init__(self, side: float | int, color: str) -> None:
        """
            initializing square

            :param side: side of square
            :type side: union float or int

            :param color: The command and the directory path.
            :type color: str

        """
        if not (type(side) is int or type(side) is float and side > 0):
            raise AssertionError
        super().__init__(side * side, side * 4)
        self.side = side
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
