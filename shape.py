class Shape:
    def __init__(self, area, perimeter, color='No color') -> None:
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
