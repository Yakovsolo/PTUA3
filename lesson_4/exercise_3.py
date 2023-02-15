# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

my_list = [1.238, 3.523, 9.267]
another_list = []

for item in my_list:
    i = round(item, 2)
    another_list.append(i)

print(my_list)
print(another_list)
