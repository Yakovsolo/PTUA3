# Lambdas section:


# Write a Python program to find if a given string starts with a given character using Lambda. Sample Output: True False

print((lambda s, c: s.startswith(c))("after", "b"))

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

print((lambda x, y: [x + 15, y + 15, x * y])(5, 10))

# Write a Python program to add two given lists using map and lambda.

list_one = ["moon ", "fobos ", "deimos ", "io ", "ganymede ", "callisto "]
list_two = ["amalthea", "himalia", "elara", "pasiphae", "sinope", "lysithea"]

print((lambda a, b: a + b)(list_one, list_two))

print(list(map((lambda a, b: a + b), list_one, list_two)))

# Write a Python program to square and cube every number in a given list of integers using Lambda

print((list(map(lambda x: [x**2, x**3], [1, 2, 3, 4, 5]))))

# Write a Python program to extract year, month, date and time using Lambda. Sample Output: 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178

import datetime

time_now = datetime.datetime.now()

current_year = lambda x: x.year
current_month = lambda x: x.month
current_day = lambda x: x.day
current_time = lambda x: x.time()
print(current_year(time_now))
print(current_month(time_now))
print(current_day(time_now))
print(current_time(time_now))
