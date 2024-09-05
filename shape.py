class Shape:
    def __init__(self, area: float | int, perimeter: float | int, color='No color') -> None:
        assert (type(area) is int or type(area) is float or area < 0, 'area should be a positive number ')
        assert (type(perimeter) is int or type(perimeter) is float or perimeter < 0, 'perimeter need a positive number')

        self.area = area
        self.perimeter = perimeter
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def get_area(self) -> int:
        return getattr(self, 'area', 0)

    def get_perimeter(self) -> int:
        return getattr(self, 'perimeter', 0)
