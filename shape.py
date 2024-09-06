"""
Author: Rugh1
Date: 06.9.2024
Description: shape class
"""


class Shape:
    def __init__(self, area: float | int, perimeter: float | int, color='No color') -> None:
        """
        Initialize a Shape object.

        :param area: The area of the shape.
        :type area: float or int

        :param perimeter: The perimeter of the shape.
        :type perimeter: float or int

        :param color: The color of the shape, default is 'No color'.
        :type color: str

        """

        if not ((type(area) is int or type(area) is float) and area > 0):
            raise AssertionError
        if not ((type(perimeter) is int or type(perimeter) is float) and perimeter > 0):
            raise AssertionError
        self.area = area
        self.perimeter = perimeter
        self.color = color

    def set_color(self, color: str):
        """
        Set the color of the shape.

        :param color: The new color of the shape.
        :type color: str

        """
        self.color = color

    def get_color(self) -> str:
        """
        Get the color of the shape.

        :return: The color of the shape.
        :rtype: str
        """
        return self.color

    def get_area(self) -> int:
        """
        Get the area of the shape.

        :return: The area of the shape.
        :rtype: int
        """
        return self.area

    def get_perimeter(self) -> int:
        """
        Get the perimeter of the shape.

        :return: The perimeter of the shape.
        :rtype: int
        """
        return self.perimeter
