from shape import Shape


class Rectangle(Shape):
    def __init__(self, side1: float | int, side2: float | int, color: str) -> None:
        super().__init__(side1 * side2, (side1 + side2) * 2)
        self.side1 = side1
        self.side2 = side2
        self.color = color

    def __add__(self, shape: Shape) -> Shape:
        return Shape(self.area + shape.area, self.perimeter + shape.perimeter)
