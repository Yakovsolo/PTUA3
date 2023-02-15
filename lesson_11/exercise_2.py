# There's a great war between the even and odd numbers. Many numbers already lost their lives in this war and it's your task to end this. You have to determine which group sums larger: the evens or the odds. The larger group wins.

# Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the difference between the sums of the even and odd numbers.

# Example:

# war_of_numbers([2, 8, 7, 5]) ➞ 2
# # 2 + 8 = 10
# # 7 + 5 = 12
# # 12 is larger than 10
# # So we return 12 - 10 = 2
# war_of_numbers([12, 90, 75]) ➞ 27
# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

from typing import Any

def war_of_numbers(my_list: list) -> int:
    even_sum = 0
    odd_sum = 0
    for num in my_list:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    return even_sum - odd_sum

my_list = (input('Input your list of numbers: ').split())

if war_of_numbers(my_list) > 0:
    print(f'Even numbers wins: {abs(war_of_numbers(my_list))}')
else:
    print(f'Odd numbers wins: {abs(war_of_numbers(my_list))}')
