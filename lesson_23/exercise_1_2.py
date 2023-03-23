# Task Nr.1:

# Create an abstract class Animal with which takes name of animal as an input and initialize it.
# The create speak abstract method, to be overridden by subclasses. And get_name method which returns name of the animal.


# Now create two subclasses of Animals: Dog and Cat which overrides the speak method, and provide the implementation
# which returns a string "Dog says Woof!" and "Cat says Meow!" respectively.


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

    def get_name(self) -> str:
        return self.name


class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name=name)

    def speak(self) -> str:
        return "Dog says Woof!"


class Cat(Animal):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name=name)

    def speak(self) -> str:
        return "Cat says Meow!"


my_animal = Cat("Murka")
print(my_animal.name)
print(my_animal.speak())
