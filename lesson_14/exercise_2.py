# Write a function that moves all elements of one type to the end of the list:

# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# Log out inputs and results in a file.

import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def move_to_end(
    my_list_with_something: list, moving_element: Union[str, int, float]
) -> list:
    for element in my_list_with_something:
        if element == moving_element:
            my_list_with_something.append(element)
            my_list_with_something.remove(element)
    return my_list_with_something


my_list_with_something = input('Enter your list, separated with " ": ').split()
moving_element = input("Enter moving element: ")

logging.info(f"Your entered list is: {my_list_with_something}")
logging.info(f"Moving element is: {moving_element}")

my_new_list = move_to_end(my_list_with_something, moving_element)
logging.info(f"Your new list is: {my_new_list}")
