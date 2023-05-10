# Task Nr.1:

# Create a class Person that has two methods: set_name and set_age, which set the name and age attributes of the class,
# respectively. Modify these methods to return self, so that the calls can be chained together.


class Person:
    def __init__(self) -> None:
        self.name = None
        self.age = None

    def set_name(self, name: str) -> "Person":
        self.name = name
        return self

    def set_age(self, age: int) -> "Person":
        self.age = age
        return self


new_person = Person()
new_person.set_name("Jakov Solovov").set_age(37)

print(f"New person is: {new_person.name}, he is {new_person.age} years old.")
