from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print("got area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class CreateShape:
    @staticmethod
    def new_shape(shape_type, *args):
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'square':
            return Square(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args)
        else:
            raise NotImplementedError(f"Shape '{shape_type}' not supported")

def main():
    # Dummy values
    shapes = [
        CreateShape.new_shape('circle', 5),
        CreateShape.new_shape('square', 4),
        CreateShape.new_shape('rectangle', 3, 6)
    ]

    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.get_area()}")

if __name__ == "__main__":
    main()
