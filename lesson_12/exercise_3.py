# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. 
# Handle all possible errors that may occur.

from typing import Union

def calc(number_one: float, number_two: float) -> dict[str, Union[int, float]]:
    sum = number_one + number_two
    subtraction = number_one - number_two
    division = number_one / number_two
    multiplication = number_one * number_two
    calc_result = {
    'sum of numbers is: ': sum, 
    'subtraction of numbers is: ': subtraction, 
    'division of numbers is: ': division, 
    'multiplication of numbers is: ': multiplication}
    return calc_result

def beauty_print_dict(calc_result: dict[str, Union[int, float]]) -> None:
    for key, value in calc_result.items():
        print(f"{key}: {value}")

try:
    number_one = float(input("Enter first number: "))
    number_two = float(input("Enter second number: "))
    result = calc(number_one, number_two)
    beauty_print_dict(result)
except ZeroDivisionError:
    print("Never divide by zero")
except ValueError:
    print("You didn't enter a number")


