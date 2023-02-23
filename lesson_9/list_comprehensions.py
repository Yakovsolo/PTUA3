# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)


# squares = [number * number for number in range(10)]
# print(squares)

# squares = [number + 2 for number in range(10) if number == 5]
# print(squares)

# names_list = ['John', 'Jane', 'Mary', 'William']

# names = []

# for name in names_list:
#     if len(name) >= 4:
#         names.append(name)
# print(f'Names_list_one: {names}')       

# names_list = ['John', 'Jane', 'Mary', 'William', 'Hellboy']
# print([name for name in names_list if len(name) >= 5])


# Dictionarie comrehensions

# my_smth = {
#     'Alpha': 1,
#     'Beta': 2,
# }

# squares = {i: i * i for i in range(10) if i <= 6}
# print(squares)

#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)

# my_dict = {
#     'one': 12,
#     'two': 23,
#     'three': 34,
#     'four': 45,
#     'five': 56,
# }
# new_dict = {key.upper(): int(str(value)[::-1]) for key, value in my_dict.items()}
# print(new_dict)

# new_dict = {}
# for key, value in my_dict.items():
#     new_dict[key.upper()] = int(str(value)[::-1])
# print(new_dict)

# values = ["a", "b", "c"]
# for index, value in enumerate(values):
#     print(index, value)

# names_list = ['John', 'Jane', 'Mary', 'William', 'Hellboy']

# my_dict = {}
# for number, name in enumerate(names_list):
#     my_dict[number] = name
# print(my_dict)

# my_dict = {number: name for number, name in enumerate(names_list)}

# print(my_dict)


# Find all of the numbers from 1-1000 that are divisible by 6.

# numbers = []

