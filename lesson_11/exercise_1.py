# Write a function that takes two lists and adds the first element in the first list with the first element in the second list, the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. Otherwise, return
# False. Example:

# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# # Both lists sum to [5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

from typing import List

def creating_new_list(list_one: list, list_two: list) -> List[int]:
    new_list = [int(el_one) + int(el_two) for el_one, el_two in zip(list_one,list_two)]
    return new_list


def checking_new_list(new_list: List[int]) -> bool:
    if len(set(new_list)) == 1:
        return True
    else:
        return False

list_one = input('Input list one: ').split()
list_two = input('Input list two: ').split()

print(creating_new_list(list_one, list_two))
print(checking_new_list(creating_new_list(list_one, list_two)))


