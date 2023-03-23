# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def get_name(self) -> None:
#         # Method to get vehicles name
#         pass

#     @abstractmethod
#     def get_vehicle_cost(self) -> None:
#         pass


# class Car(Vehicle):
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def get_age(self) -> None:
#         print(self.age)

#     def get_name(self) -> None:
#         # Method to get vehicles name
#         print(self.name)

#     def get_vehicle_cost(self) -> None:
#         print("Too much")


# my_car = Car(name="Audi-A6", age=2018)
# my_car.get_age
# print(my_car.get_vehicle_cost())


# class Vehicle:
#     def get_smth(self) -> None:
#         pass

#     def do_smth(self) -> None:
#         raise NotImplementedError


# class Combain(Vehicle):
#     def do_smth(self) -> None:
#         print("Do smth")


# my_veh = Combain()
# my_veh.do_smth()
