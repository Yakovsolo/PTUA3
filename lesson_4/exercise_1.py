my_list = []

number_of_range = int(input('input list range: '))

for i in range(number_of_range):
    i = input('input items with different types: ')
    print(f'my value: {i}, my type {type(i)}')
    my_list.append(i)

for item in my_list:
    print(type(item))


