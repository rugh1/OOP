from shape import Shape
class Square(Shape): 
    def __init__(self,side) -> None:
        super().__init__(side*side, side<<2) 
        self.side = side

