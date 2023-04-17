# Task Nr.1:

# Create a class method to return the factorial of a given number.


class Calc:
    @classmethod
    def get_factorial(cls, number: int) -> int:
        if number == 1:
            return number
        else:
            return number * cls.get_factorial(number - 1)


print(Calc.get_factorial(number=10))

# output:
# 3628800
