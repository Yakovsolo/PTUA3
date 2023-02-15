# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

a = float(input('a= '))
sign = input('Input arithmetic sign (+, -, *, /, ^): ')
b = float(input('b= '))

# if sign == '+':
#     print(a + b)
# elif sign == '-':
#     print(a - b)
# elif sign == '*':
#     print(a * b)
# elif sign == '/':
#     print(a / b)
# elif sign == '^':
#     print(a ** b)
sign_list = ['+', '-', '*', '/', '**']
if sign in sign_list:
    if sign == '+':
        answer = a + b
    elif sign == '-':
        answer = a - b
    elif sign == '*':
        answer = a * b
    elif sign == '/':
        answer = a / b
    elif sign == '^':
        answer = a ** b
    print(answer)
else:
    print('to much')
