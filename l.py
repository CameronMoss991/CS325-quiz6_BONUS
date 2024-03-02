from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print("Get shape area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius * self.radius

    def set_radius(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length

    def get_area(self):
        # Used for area calculation 
        print("get area")

    def get_perimeter(self):
        # Used for perimeter calculation 
        print("get perimeter")

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4)

    shapes = [circle, rectangle, triangle]
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.get_area()}")

if __name__ == "__main__":
    main()
