"""
Author: Rugh1
Date: 06.9.2024
Description: main code
"""
from container import Container
from circle import Circle
from rectangle import Rectangle
from square import Square
from shape import Shape


def run_tests():
    """
    Run tests for Shape and its subclasses to verify correct functionality.
    """
    # Test Shape Initialization
    shape = Shape(25, 20, 'Red')
    assert shape.get_area() == 25, "Shape area initialization failed"
    assert shape.get_perimeter() == 20, "Shape perimeter initialization failed"
    assert shape.get_color() == 'Red', "Shape color initialization failed"

    # Test Circle Initialization
    circle = Circle(5, 'Blue')
    assert round(circle.get_area(), 5) == 78.53982, "Circle area calculation failed"
    assert round(circle.get_perimeter(), 5) == 31.41593, "Circle perimeter calculation failed"
    assert circle.get_color() == 'Blue', "Circle color initialization failed"

    # Test Square Initialization
    square = Square(4, 'Green')
    assert square.get_area() == 16, "Square area calculation failed"
    assert square.get_perimeter() == 16, "Square perimeter calculation failed"
    assert square.get_color() == 'Green', "Square color initialization failed"

    # Test Rectangle Initialization
    rectangle = Rectangle(4, 6, 'Yellow')
    assert rectangle.get_area() == 24, "Rectangle area calculation failed"
    assert rectangle.get_perimeter() == 20, "Rectangle perimeter calculation failed"
    assert rectangle.get_color() == 'Yellow', "Rectangle color initialization failed"

    # Test Setting Color of Shapes
    shape.set_color('Purple')
    assert shape.get_color() == 'Purple', "Shape color set failed"

    # Test Adding Shapes
    combined_shape = square + rectangle
    assert combined_shape.get_area() == 40, "Shape addition area failed"
    assert combined_shape.get_perimeter() == 36, "Shape addition perimeter failed"

    # Test Error Handling
    try:
        Shape(-5, 10, 'Red')  # Negative area should raise an error
    except AssertionError:
        print("Caught expected error for negative area in Shape")

    try:
        Circle(-1, 'Blue')  # Negative radius should raise an error
    except AssertionError:
        print("Caught expected error for negative radius in Circle")

    try:
        Square('invalid', 'Red')  # Invalid side type should raise an error
    except AssertionError:
        print("Caught expected error for invalid side type in Square")

    try:
        Rectangle(5, 'invalid', 'Green')  # Invalid side type should raise an error
    except AssertionError:
        print("Caught expected error for invalid side type in Rectangle")

    # Specific tests for Circle's calculated area and perimeter
    circle = Circle(10, 'Cyan')
    expected_area = 314.1592653589793
    expected_perimeter = 62.83185307179586
    assert round(circle.get_area(), 5) == round(expected_area, 5), "Circle area mismatch"
    assert round(circle.get_perimeter(), 5) == round(expected_perimeter, 5), "Circle perimeter mismatch"

    print("All tests passed successfully!")


def main():
    run_tests()

    my_container = Container()
    my_container.generate(10)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    main()
