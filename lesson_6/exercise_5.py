# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)

import random
number = random.randint(0, 10)

print('I guessed a number from 1 to 10. Number is integer. Guess my number')

guessing_number = int(input('I guess your number is: '))
if guessing_number == number:
    print('You guessed right')
else:
    print('You did not guess right')