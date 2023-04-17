# Task Nr.3:

# Create a class method to return the list of prime numbers up to a given number.
from typing import List


class CheckNumbers:
    @classmethod
    def is_number_prime(cls, number: int) -> bool:
        if number <= 1:
            return False

        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                return True

        return True

    @classmethod
    def get_prime_numbers_list(cls, number: int) -> List[int]:
        prime_numbers_list = []
        for number in range(2, number + 1):
            if cls.is_number_prime(number):
                prime_numbers_list.append(number)
        return prime_numbers_list


print(CheckNumbers.get_prime_numbers_list(15))

# Output:
# [2, 3, 5, 7, 9, 11, 13, 15]
