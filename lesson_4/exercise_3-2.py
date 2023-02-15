# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.


my_list = [1.238, 3.523, 9.267]
another_list = []

a = my_list[0]
another_list.append(round(a,2))
b = my_list[1]
another_list.append(round(b,2))
c = my_list[2]
another_list.append(round(c,2))

print(my_list)
print(another_list)