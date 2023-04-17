# In this implementation, Calculator is an abstract base class that defines four abstract methods for the basic arithmetic
# operations of addition, subtraction, multiplication, and division. It also defines a concrete method square that can be used by any subclass.

# ArithmeticCalculator is a subclass of Calculator that implements the four abstract methods as well as an additional method exponentiate for raising a number to a power.

# GeometryCalculator is another subclass of Calculator that overrides the basic arithmetic methods with NotImplementedError
# to indicate that they are not supported by this calculator. It also defines three new methods for calculating the area of a square, rectangle, and circle.

# Both subclasses of Calculator inherit the square method from the base class.

# Note that this implementation is just one possible approach and there are many other ways to structure a calculator program with different features and functionality.

from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

    def square(self, a):
        return self.multiply(a, a)


class ArithmeticCalculator(Calculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def exponentiate(self, a, b):
        return a**b


class GeometryCalculator(Calculator):
    def add(self, a, b):
        raise NotImplementedError("Geometry calculator does not support addition")

    def subtract(self, a, b):
        raise NotImplementedError("Geometry calculator does not support subtraction")

    def multiply(self, a, b):
        raise NotImplementedError("Geometry calculator does not support multiplication")

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def area_of_square(self, side):
        return self.square(side)

    def area_of_rectangle(self, length, width):
        return self.multiply(length, width)

    def area_of_circle(self, radius):
        pi = 3.14159265359
        return self.multiply(pi, self.square(radius))
