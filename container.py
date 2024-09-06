"""
Author: Rugh1
Date: 06.9.2024
Description: container class
"""
import circle
import random
import rectangle
import square


class Container:
    MAX_VALUE = 20
    MIN_VALUE = 1
    COLORS = ['Turquoise', 'Blue', 'Cyan', 'Navy Blue', 'Aqua', 'Cerulean', 'Electric blue',
              'Sapphire', 'Azure', 'Aquamarine', 'Lapis', 'Berry', 'Arctic', 'Admiral', 'Celeste']
    _CREATE_FUNCTIONS = [
        lambda: square.Square(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                              random.choice(Container.COLORS)),
        lambda: circle.Circle(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                              random.choice(Container.COLORS)),
        lambda: rectangle.Rectangle(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                                    Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                                    random.choice(Container.COLORS))]

    def __init__(self) -> None:
        """
        Initialize a Container object.

        """
        self.shapes = []

    def generate(self, x: int) -> None:
        """
        Generate random shapes and add them to the container.

        :param x: The number of shapes to generate.
        :type x: int

        """
        assert (type(x) is int and x > 0, 'generate function takes positive integers')
        for i in range(x):
            self.shapes.append(Container._CREATE_FUNCTIONS[random.randint(0, 2)]())

    def sum_areas(self) -> int:
        """
        Calculate the sum of the areas of all shapes in the container.

        :return: The total area of all shapes.
        :rtype: int
        """
        sum = 0
        for i in self.shapes:
            sum += i.get_area()
        return sum

    def sum_perimeters(self) -> int:
        """
        Calculate the sum of the perimeters of all shapes in the container.

        :return: The total perimeter of all shapes.
        :rtype: int
        """
        sum = 0
        for i in self.shapes:
            sum += i.get_perimeter()
        return sum

    def count_colors(self):
        """
        Count the occurrences of each color among the shapes in the container.

        :return: A dictionary with colors as keys and their counts as values.
        :rtype: dict
        """
        color_dict = dict.fromkeys(Container.COLORS, 0)
        for i in self.shapes:
            color_dict[i.get_color()] += 1
        return color_dict
