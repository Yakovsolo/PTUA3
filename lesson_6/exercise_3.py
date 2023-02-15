# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

a = float(input('Input first number, please:'))
b = float(input('Input second number, please:'))

if a > b:
    print('First number is hier than second')
elif a == b:
    print('First number is equal second number')
else:
    print('First number is smaller than second')
