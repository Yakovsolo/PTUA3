"""Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000) 
and would stop itterating until the word longer than 7 lettters is found.
Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)"""

from py_random_words import RandomWords
from typing import List
from collections.abc import Iterator
import sys
import time


rnd_word = RandomWords()
list_of_words = [rnd_word.get_word() for _ in range(10000)]
print(f"Generator mem size is: {sys.getsizeof(list_of_words)}")


generator_of_wors = (word for word in list_of_words)
print(f"List mem size is: {sys.getsizeof(generator_of_wors)}")


def get_long_word(generator_of_words: List[str]) -> Iterator[str]:
    for word in generator_of_words:
        if len(word) > 7:
            yield word


start_time = time.perf_counter()

long_word = get_long_word(list_of_words)
print(next(long_word))

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time using generator is: {execution_time * 1000} ms")


def get_long_word_from_list(list_of_words: List[str]) -> str:
    for word in list_of_words:
        if len(word) > 7:
            return word
    return f"There are no words, longer than seven letters in list"


start_time = time.perf_counter()

print(get_long_word_from_list(list_of_words))

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time using list is: {execution_time * 1000} ms")


# Output:

# Generator mem size is: 85176
# List mem size is: 200
# reindeer
# The execution time using generator is: 0.00015430000348715112
# reindeer
# The execution time using list is: 0.0002514999941922724
