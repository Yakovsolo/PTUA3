# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.



dic_one = {
    1: 10,
    2: 20
}

dic_two = {
    3: 30,
    4: 40
}
dic_three = {
    5: 50,
    6: 60
}

# new_dic = {

# }

# new_dic.update(dic_one)
# new_dic.update(dic_two)
# new_dic.update(dic_three)

dic_one.update(dic_two)
dic_one.update(dic_three)

# print(new_dic)

print(dic_one)

