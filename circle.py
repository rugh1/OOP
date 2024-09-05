from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius: float | int, color: str) -> None:
        assert (type(radius) is int or type(radius) is float)
        super().__init__(radius * radius * pi, pi * radius * 2)
        self.radius = radius
        self.color = color
