# 1: Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n.

from collections.abc import Iterator


def generate_even_numbers(n: int) -> Iterator[int]:
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = 70
my_even_numbers = generate_even_numbers(n)

for number in my_even_numbers:
    print(number)
