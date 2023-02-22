# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.

# First function

# from typing import Union

# def adding_list(my_list: list, operation_digit: int) -> Union[list, None]:

#     my_new_list = [item / operation_digit for item in my_list]
#     return(my_new_list)


# try:
#     print(adding_list([1, 2, 3, 4, 5], 2))
#     print(adding_list([1, 2, 3, 4, 5], 0))
#     print(adding_list([1, 2, 3, 4, 5], 'a'))
# except ZeroDivisionError:
#     print('Operation digit cannot be zero')
# except TypeError:
#     print('Operation digit must be an integer')

# Second function

# from typing import Union
# import math

# def finding_sqare_root(number: int) -> Union[float, None]:
#     sqare_root = math.sqrt(number)
#     # return y 
# try:
#     print(finding_sqare_root(4))
#     print(finding_sqare_root(-4))

# except ValueError:
#         print('Cannot find square root, number must be a positive integer')

# Third function

# def sum(numb_1: int, numb_2: int) -> int:
#     sum = numb_1 + numb_2
#     return(sum)
# try:
#     a = 5
#     b = 6
#     print(sum(a, c))    
# except NameError as e:
#     print(f'NameError:  {e}')





        
