# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.


name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))

if age >= 21:
    print(f'Dear {name}, you are allowed to enter an online casino!')
else:
    print(f'{name}, are you crazy? Get out from here!')