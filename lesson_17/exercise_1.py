# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.

import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Calculator:
    def __init__(self, number_one: Union[int, float], number_two: Union[int, float]):
        self.number_one: Union[int, float] = number_one
        self.number_two: Union[int, float] = number_two
        logging.info(f"Calculating {self.number_one} and {self.number_two}")

    def add(self):
        return self.number_one + self.number_two

    def subtract(self):
        return self.number_one - self.number_two

    def divide(self):
        if self.number_two == 0:
            logging.error(f"Cannot divide by zero")
            raise ZeroDivisionError("You cannot divide by zero")

        return self.number_one / self.number_two

    def multiply(self):
        return self.number_one * self.number_two

    def expon(self):
        return self.number_one**self.number_two


number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))


calculator = Calculator(number_one, number_two)


print(calculator.divide())
print(calculator.multiply())
print(calculator.add())
print(calculator.subtract())
print(calculator.expon())
