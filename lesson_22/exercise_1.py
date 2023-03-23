# Define a Shape class with the following attributes and methods:

# A name attribute, which is a string that represents the name of the shape.
# A sides attribute, which is an integer that represents the number of sides of the shape.
# An area method, which returns the area of the shape.
# Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:

# A width attribute, which is a float that represents the width of the rectangle.
# A height attribute, which is a float that represents the height of the rectangle.
# An init method that initializes the name, sides, width, and height attributes.
# An area method that overrides the area method of the Shape class and returns the area of the rectangle.
# Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:

# A side_length attribute, which is a float that represents the length of the sides of the square.
# An init method that initializes the side_length attribute and calls the init method of the Rectangle class to initialize the name, sides, width, and height attributes.


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def get_area(self) -> None:
        pass


class Rectangle(Shape):
    def __init__(self, name: str, sides: int, width: float, height: float) -> None:
        super().__init__(name=name, sides=sides)
        self.name = name
        self.sides = sides
        self.width = width
        self.height = height

    def get_area(self) -> float:
        area = self.width * self.height
        return area


class Square(Rectangle):
    def __init__(self, side_length: float) -> None:
        super().__init__(width=side_length, height=side_length, name="Square", sides=4)
        self.side_length = side_length


my_shape = Square(side_length=5)
print(my_shape.get_area())
print(my_shape.name)
