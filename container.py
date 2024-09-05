import circle
import random
import rectangle
import square


class Container:
    MAX_VALUE = 20
    MIN_VALUE = 1
    COLORS = ['Turquoise', 'Blue', 'Cyan', 'Navy Blue', 'Aqua', 'Cerulean', 'Electric blue',
              'Sapphire', 'Azure', 'Aquamarine', 'Lapis', 'Berry', 'Arctic', 'Admiral', 'Celeste']
    _CREATE_FUNCTIONS = [
        lambda: square.Square(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                              random.choice(Container.COLORS)),
        lambda: circle.Circle(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                              random.choice(Container.COLORS)),
        lambda: rectangle.Rectangle(Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                                    Container.MIN_VALUE + random.random() * (Container.MAX_VALUE - Container.MIN_VALUE),
                                    random.choice(Container.COLORS))]

    def __init__(self) -> None:
        self.shapes = []

    def generate(self, x: int) -> None:
        for i in range(x):
            self.shapes.append(Container._CREATE_FUNCTIONS[random.randint(0, 2)]())

    def sum_areas(self) -> int:
        sum = 0
        for i in self.shapes:
            sum += i.get_area()
        return sum

    def sum_perimeters(self) -> int:
        sum = 0
        for i in self.shapes:
            sum += i.get_perimeter()
        return sum

    def count_colors(self):
        color_dict = dict.fromkeys(Container.COLORS, 0)
        for i in self.shapes:
            color_dict[i.get_color()] += 1
        return color_dict
