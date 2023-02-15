# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input('n= '))
my_dic = {}

for i in range (1, n + 1):
    my_dic[i] = i ** i


    # dic_keys = [i]
    # dic_values = [i**i]
    # intermediate_dictionary = dict(zip(dic_keys, dic_values))
    # my_dic.update(intermediate_dictionary)

print(my_dic)