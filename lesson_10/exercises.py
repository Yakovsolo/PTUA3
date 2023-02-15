# Create at least 5 different functions by your own and test it.

# First function

# def math_equation(a: float, b: float, c: float) -> float:
#     x = round((b ** 2 - 4 * a * c) / (2 * a), 2)
#     return print(x)

# math_equation(100, 20.25, 3.25)

# Second function

# def adding_list(my_list: list) -> list:
#     my_new_list = [item**2 for item in my_list]
#     print(my_new_list)
    
# adding_list([1, 2, 3, 4, 5, 6, ])

# Third function

# def member_char(name: str, surname: str, age: int):
#     if age >= 18:
#         print(f'Dear {name} {surname}, wellcomw to our club!')
#     else:
#         print(f'{name} {surname}, you are too young to be here!')
        
# name, surname, age = input('input name, surname and age: ').split()

# member_char(name, surname, int(age))

# Fourth function

# def sorting_list(my_list: list) -> list:
#     sorted_list = sorted(my_list)
#     return sorted_list

# my_list = input('input list: ').split()

# print(sorting_list(my_list))

# Fifth function

def creating_new_dict(list_one: list, list_two: list) -> dict:
    new_dict = dict(zip(list_one, list_two))
    return new_dict
list_one = input('input list one (5 items): ').split()
list_two = input('input list two: (five items)').split()

print(creating_new_dict(list_one, list_two))
     
        
# Create a function that adds a string ending to each member in a list.

from typing import List

def add_ending(my_list: List[str], string_add: str) -> List:
    new_list = []
    for item in my_list:
        new_list.append(item + string_add)
    return new_list

my_list = input('input list, separated " ": ').split(' ')
string_add = input('input your string add: ')
print(my_list)
print(add_ending(my_list, string_add))


 

