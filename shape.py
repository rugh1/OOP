class Shape:
    def __init__(self) -> None:
        pass 
    
    def __init__(self,area, perimiter) -> None:
        self.area = area 
        self.perimeter = perimiter  

    def set_color(self ,color:str):
        self.color = color

    def get_color(self) -> str:
        return getattr(self, 'color', 'No color')

    def get_area(self) -> int:
        return getattr(self, 'area', 0)
    
    def get_perimeter(self) -> int:
        return getattr(self, 'perimeter', 0)