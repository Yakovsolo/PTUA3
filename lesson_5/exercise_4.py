# Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary

name = input("What is your name? ")
surname = input("What is your surname? ")
age = int(input('How old are you? '))

my_dic = {'name' : name, 'surname': surname, 'age': age}

print(my_dic)