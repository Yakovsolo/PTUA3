# 1. create 4 digit pin code that is either string or int 
# 2. create brute force algorithm that finds the correct pin code. 
# 3. print that code

pin_code = int(input("input 4 digit PIN code: "))

a = 0

while True:
    if a != pin_code:
        a +=1
        print(a)
    else:
        print("Your PIN code is: ", pin_code)
        break
