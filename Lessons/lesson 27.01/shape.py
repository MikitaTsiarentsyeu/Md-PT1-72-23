from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    __supported_shapes = {}

    @abstractmethod
    def __init__(self, side) -> None:
        self.side = side

    @abstractmethod
    def area(self):
        print("some area logic")

    @abstractmethod
    def perimeter(self): pass

    def add_shape(self):
        pass

    @classmethod
    def register_shape(cls, name, shape):
        cls.__supported_shapes[name] = shape

    @classmethod
    def create_shape(cls, name, *args):
        return cls.__supported_shapes[name](*args)
    
    @classmethod
    def create_square(cls, a):
        return cls.__supported_shapes["square"](a)

    @classmethod
    def create_circle(cls, a):
        return cls.__supported_shapes["circle"](a)

class __Square(Shape):

    def __init__(self, side_length) -> None:
        super().__init__(side_length)

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4
    
class __Circle(Shape):

    def __init__(self, r) -> None:
        super().__init__(r)

    def area(self):
        return pi*self.side**2

    def perimeter(self):
        return 2*pi*self.side

# Shape()

# sq = __Square(4)
# print(sq.area(), sq.perimeter())


# c = __Circle(10)
# print(c.area(), c.perimeter())


Shape.register_shape("square", __Square)
Shape.register_shape("circle", __Circle)