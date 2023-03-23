# Task Nr.2:

# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.

class Vehicle:
    def __init__(self, make: str, model: str, year: str, seating_capacity: int, cost: float) -> None:
        self.make: str = make
        self.model: str = model
        self.year: str = year
        self.seating_capacity: int = seating_capacity
        self.cost: float = cost

    def get_make(self) -> str:
        return self.make
    
    def get_model(self) -> str:
        return self.model
    
    def get_year(self) -> str:
        return self.year
    
    def get_cost(self) -> float:
        return self.cost
    
    def get_seating_capacity(self) -> int:
        return self.seating_capacity
    
    def fare_charge(self) -> float:
        return self.seating_capacity * 100


class Bus(Vehicle):
    
    def fare_charge(self) -> float:
        return round((self.seating_capacity * 100) * 1.1, 2)


class Taxi(Vehicle):
    pass


class Train(Vehicle):
   pass



if __name__ == "__main__":

    my_vehicle = Bus(make="Mersedez-Benz", model="Tourismo M/2 standard", year="2023", seating_capacity=55, cost=150000)

    print(my_vehicle.fare_charge())
    print(my_vehicle.get_cost())
