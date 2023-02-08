# Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)

my_list = ["There ", "is ", "a ", "house ", "in ", "New ", "Orleans"]

x = str()

for a in my_list:
    c = x + a
    x = c

print(x)
