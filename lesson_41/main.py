from typing import List


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def get_coordinates(self) -> List[float]:
        return[self._x, self._y]
    
my_point = Point(2.5, 6.3)
print(my_point.get_coordinates())