# Task Nr.4:

# Create a Calculator program : it should contain abstract class with methods (abstract and not), base class,
# geometry, arithmetic calculator classes. Every subclass should have at least 5 methods to make some meaningful
# calculus operations.

from abc import ABC, abstractmethod
import math


class Calculator(ABC):
    @abstractmethod
    def sum(self, ) -> float:
        pass

    def subtraction(self) -> float:
        pass

    def multiply(self) -> float:
        pass

    def divide(self) -> float:
        pass

    def sqrt(self) -> float:
        pass

    def get_figure_name(self, figure_name: str) -> str:
        pass

    def figure_area(self) -> float:
        pass

    class BaseCalculator(Calculator):
        def __init__(
            self, first_number: float, operation: str, second_number: float
        ) -> None:
            self.first_number = first_number
            self.operation = operation
            self.second_number = second_number

        def calculator_choise(self) -> None:
            calculator_name = input("There are following types of calculators:\n1. Arithmetic calculator\n2. Geometry calculator\nPlease, choise calculator (1, 2): )
            return calculator_name

        @abstractmethod
        def sum(self) -> float:
            return self.first_number + self.second_number

        def subtraction(self) -> float:
            return self.first_number - self.second_number

        def multiply(self) -> float:
            return self.first_number * self.second_number

        def divide(self) -> float:
            return self.first_number / self.second_number

