# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

from typing import List


class Person:
    def __init__(
        self, name: str, foods_they_like: List[str], foods_they_hate: List[str]
    ) -> None:
        self.name = name
        self.foods_they_like = foods_they_like
        self.foods_they_hate = foods_they_hate

    def taste(self, food_name: str) -> None:
        if food_name in self.foods_they_like:
            print(f"{self.name} eats the {food_name} and loves it!")
        elif food_name in self.foods_they_hate:
            print(f"{self.name} eats the {food_name} and hates it!")
        else:
            print(f"{self.name} eats the {food_name}!")


if __name__ == "__main__":
    p1 = Person("Sam", ["ice cream"], ["carrots"])
    p1.taste("ice cream")
    p1.taste("cheese")
    p1.taste("carrots")
