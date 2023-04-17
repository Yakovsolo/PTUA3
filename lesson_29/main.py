class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def from_square(cls, side_length: float) -> "Rectangle":
        return cls(side_length, side_length * 2)


rectangle_one: Rectangle = Rectangle(3.0, 4.0)
rectangle_two: Rectangle = Rectangle.from_square(2.0)

print(rectangle_one.area())  # 12.0
print(rectangle_two.area())  # 4.0
