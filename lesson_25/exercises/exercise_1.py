# write a function that accepts a number as a parameter. The function should return a number that’s the
# difference between the largest and smallest numbers that the digits can form in the number.


def get_difference(number: int) -> int:
    number_to_str = str(number)
    number_one = "".join(sorted((number_to_str), reverse=True))
    number_two = "".join(sorted(number_to_str))
    print(number_one)
    print(number_two)
    difference = int(number_one) - int(number_two)
    return difference


number = int(input("Input your number:\n"))

print(get_difference(number))
