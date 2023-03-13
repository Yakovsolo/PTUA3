# Create a few examples of yourself where you show four pillars of OOP in action.

class Building:
    def __init__(self, bulding_color: str, number_of_floors: int, floor_height: float) -> None:
        self.color = bulding_color
        self.number_of_floors = number_of_floors
        self.floor_height = floor_height
        
    def get_building_color(self) -> None:
        print(f'The color of building is {self.color}')

    def get_number_of_floors(self) -> None:
        print(f'Nuber of floors is: {self.number_of_floors}')
    
    def find_building_height(self) -> None:
        building_height = self.floor_height * self.number_of_floors
        print(f'Building height is: {building_height}')


class My_house(Building):
    def __init__(self, my_living_floor: int, my_living_area: float, color: str, number_of_floors: int, floor_height: float) -> None:
        super().__init__(bulding_color=color, number_of_floors=number_of_floors, floor_height=floor_height)
        self.my_living_floor = my_living_floor
        self.my_livig_area = my_living_area
                
    def get_number_of_floors(self) -> None:
       print(f'The number of floors of my house is {self.number_of_floors}')

    def get_my_livig_height(self) -> None:
        my_living_height = self.my_living_floor * self.floor_height
        print(f'My_living_height is: {my_living_height}')

abstract_building = Building(bulding_color='Gray', number_of_floors=5, floor_height=2.9)
my_living_house = My_house(my_living_floor=3, my_living_area=44.5, color='Red', number_of_floors=5, floor_height=2.9)

abstract_building.get_building_color()
my_living_house.get_my_livig_height()
my_living_house.find_building_height()
