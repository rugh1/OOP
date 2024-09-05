from shape import Shape


class Square(Shape):
    def __init__(self, side: float | int, color: float | int) -> None:
        assert (type(side) is int or type(side) is float or side < 0, 'side should be a positive number ')
        super().__init__(side * side, side * 2)
        self.side = side
        self.color = color

    def __add__(self, shape: Shape) -> Shape:
        return Shape(self.area + shape.area, self.perimeter + shape.perimeter)
