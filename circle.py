from shape import Shape
from math import pi
class Circle(Shape): 
    def __init__(self,radius) -> None:
        super().__init__(radius*radius*pi, pi*radius<2) 
        self.radius = radius

