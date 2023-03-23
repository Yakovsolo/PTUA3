# Task Nr.3:

# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :) 🐒


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self) -> str:
        return f"Look what noise makes {self.name}"


class Mammal(Animal):
    def __init__(self, warm_blooded: bool, name: str) -> None:
        super().__init__(name=name)
        self.warm_blooded = warm_blooded
        self.name = name

    def give_birth(self) -> str:
        return f"{self.name} is born"


class Primate(Mammal):
    def __init__(self, name: str, opposble_thumbs: bool) -> None:
        super().__init__(True, name=name)
        Animal.__init__(self, name=name)
        self.opposble_thumbs = opposble_thumbs
        self.name = name


chimpanzee = Primate("Chimpanzee", True)
print(chimpanzee.make_noise())
