# Filter section:


# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190]
# Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

# Write a Python program to filter a list of integers using Lambda Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter((lambda x: x % 2 == 0), original_list)))
print(list(filter((lambda x: x % 2 != 0), original_list)))
