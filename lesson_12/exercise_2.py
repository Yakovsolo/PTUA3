# Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example

from typing import Union


def division(
    num_one: Union[int, float], num_two: Union[int, float]
) -> Union[int, float]:
    result = num_one / num_two
    return result


try:
    num_1 = 10
    num_2 = 5
    div = division(num_1, num_2)
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Your answer is : {div}")
finally:
    print("Program Ended")
