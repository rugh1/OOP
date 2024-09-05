from shape import Shape


class Square(Shape):
    def __init__(self, side: float | int, color: float | int) -> None:
        super().__init__(side * side, side * 2)
        self.side = side
        self.color = color

    def __add__(self, shape: Shape) -> Shape:
        return Shape(self.area + shape.area, self.perimeter + shape.perimeter)
