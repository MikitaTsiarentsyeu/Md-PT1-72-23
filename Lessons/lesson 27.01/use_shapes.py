import shape

sq = shape.Shape.create_shape("square", 4)
print(sq.area())

shape.Shape.create_square(2)

class Rectangle(shape.Shape):

    def __init__(self, side_a, side_b) -> None:
        super().__init__(side_a)
        self.side_b = side_b

    def area(self):
        return self.side * self.side_b
    
    def perimeter(self):
        return self.side * 2 + self.side_b * 2


r = Rectangle(2, 3)