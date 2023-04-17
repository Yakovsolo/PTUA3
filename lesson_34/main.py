# import time


# def infinite_sequence():
#     num = 0
#     while True:
#         num += 1
#         yield num
#         time.sleep(0.5)


# my_generator = infinite_sequence()
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))


# for value in my_generator:
#     print(value)


# my_words_list = []  # list of million words

# for word in my_words_list:
#     yield word
#     print(word)

import sys

# nums_squared_lc = [num**2 for num in range(5)]

# print(nums_squared_lc)
# nums_squared_gc = (num**2 for num in range(5))
# print(nums_squared_gc)
# nums_squared_lc = [num**2 for num in range(10000)]

# nums_squared_gc = (num**2 for num in range(10000))
# print(f"List mem size is: {sys.getsizeof(nums_squared_lc)}")
# print(f"Generator mem size is: {sys.getsizeof(nums_squared_gc)}")

from collections.abc import Iterator

def generate_even_numbers(n: int) -> Iterator[int]:
    for i in range(n+1):
        if i % 2 == 0:
            yield i