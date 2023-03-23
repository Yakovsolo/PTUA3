# ask Nr.2: Magic Number problem. A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits
# after every addition. If the single digit comes out to be 1,then the number is a magic number.
# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number

# For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

# Write a python function that takes in one parameter - integer and then returns True if number is magic number or False if it is not a magic number


def magic_number_check(number_to_check: int) -> bool:
    digits_list = [int(digit) for digit in str(number_to_check)]
    print(digits_list)
    if len(digits_list) == 1:
        if digits_list[0] == 1:
            return True
        else:
            return False
    else:
        check = sum(digits_list)
        return magic_number_check(check)


number_to_check = int(input("Enter a number, you woul'd like to check: "))

print(magic_number_check(number_to_check))
