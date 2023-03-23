import datetime


name = input("Enter your name: ")
age = int(input("Ener your age: "))
clause = input("Did you already have a birthday this year (Y / N)?")

x = datetime.datetime.now()
current_year = x.year
if clause == "Y":
    birth_year = current_year - age
else:
    birth_year = current_year - age - 1

print(birth_year)
