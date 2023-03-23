class Vehicle:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class Engine:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hi_engine(self) -> None:
        print(f"Hi engine with name {self.name}")


class Golfukas(Vehicle, Engine):
    def __init__(self, name: str, cost: float) -> None:
        super().__init__(name=name)
        Engine.__init__(self, name=name)
        self.coast = cost

    def get_cost(self) -> float:
        return self.coast


CAR_NAME = "Achujiena tacka"
my_car = Golfukas(name=CAR_NAME, cost=100)

print(my_car.say_hi_engine())
