# class Names:
#     '''This is a class aboutour forgotten friend Antanas'''

#     def __init__(self, name: str, surname: str, age: int) -> None:
#         self.name = name
#         self._surname = surname
#         self.__age = age
      
#     def print_out_the_name(self) -> None:
#         print(self.name)
        
#     def change_name(self, name: str) -> None:
#         self.name = name


# my_name = Names(name = "Antanas", surname = 'Jakov', age = 25)

# print(my_name.name)
# print(my_name._surname)
# print(my_name.__age)


# my_name._surname = 'Petras'
# print(my_name._surname)


# class Car:
#     def __init__(self, make_year: int, cost: float,  color: str) -> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f'Full info: {cost} linero - {make_year} years - {color}..'
        
#     def get_car_color(self) -> None:
#         print(f'My car color: {self.color}')
    
#     def get_color(self) -> float:
#         return self.cost
    
#     def get_full_info(self) -> None:
#         print(f'My full info: {self.full_info}')


class Car:
    def __init__(self) -> None:
        self.check_this_one: int = 1
        
            
    def get_car_color(self, color: str) -> None:
        print(f'My car color: {color}')
    
    def get_cost(self, cost: float) -> float:
        return self.cost
    
    def get_full_info(self, full_info: str) -> None:
        print(f'My full info: {full_info}')


class Ferrari(Car):
    SPEED_CONSTANT = 20.5

    def __init__(self, hp: int) -> None:
        self.hp = hp
            
    def get_max_speed(self) -> float:
        return self.hp * self.SPEED_CONSTANT

my_uber_car = Ferrari(hp=450)
print(f' My max speed: {my_uber_car.get_max_speed()}')

