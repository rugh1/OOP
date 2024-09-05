from shape import Shape


class Rectangle(Shape):
    def __init__(self, side1: float | int, side2: float | int, color: str) -> None:
        assert (type(side1) is int or type(side1) is float or side1 < 0, 'side1 should be a positive number ')
        assert (type(side2) is int or type(side2) is float or side2 < 0, 'side1 should be a positive number ')
        super().__init__(side1 * side2, (side1 + side2) * 2)
        self.side1 = side1
        self.side2 = side2
        self.color = color

    def __add__(self, shape: Shape) -> Shape:
        return Shape(self.area + shape.area, self.perimeter + shape.perimeter)
