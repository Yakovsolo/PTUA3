# a = 2
# b = 5

# def addition(number1, number2):
#     sum = number1 + number2
#     return sum
    
# c = addition(10, 15)

# print(c)

# def print_smth():
#     print('Hello world!')

# print_smth()

# my_list = [1, 2, 3]

# my_list = my_list.append(4)

# print(my_list)

# import random

# def get_random_number():
#     return print(random.randint(0, 10))
# get_random_number()

# def __get_something():
#     print('asdf')
# __get_something()

# def find_sum(num1, num2):
#     '''Returns the sum of num1 and num2.'''

    
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# print(help(find_sum))
# print(find_sum.__doc__)

# import random


# def even_odd(num):

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"

# number = random.randint(0, 10)

# if even_odd(number) == "even":
#     print(f'my number: {number} is even')
# else:
#     print(f'my number: {number} is odd')

# def find_subtraction(num1, num2=20):
#     '''Returns the sum of num1 and num2.'''
#     sum_nums = num1 - num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers
# print(find_subtraction(5))

# def add_two_int_numbers(a: int, b:int) -> int:
#   return a + b
# number1 = add_two_int_numbers(10.02, 2)
# print(number1)

# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True


# from typing import List, Tuple, Dict, Union, Optional

# Dicttype_annotation_tuple: Tuple[str] = ('1','2','3')
# type_annotation_list: List[str] = ['a', 'b', 'c']
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

# def get_random_object() -> Union[int, str, List[str]]:
#     number = random.randint(0, 3)
#     if number == 0:
#         return 0
#     elif number == 1:
#         return "str"
#     else:
#         return ['1', '2', '3']
# print(get_random_object())

# from typing import Tuple, Optional, Union

# def the_func(x: Union[int, float], y: Tuple[str], z: Optional[float] = None) -> str:
#    return 'You called the_func with ' + str(x) + str(y) + str(z)
# print(the_func(10, ('a')))



