# from typing import List


# class Mylist:
#     def __init__(self, items: List[int]) -> None:
#         self.items = items

#     def __bool__(self) -> bool:
#         return False

#     def __len__(self) -> int:
#         return len(self.items) * 2

#     def __str__(self) -> str:
#         return "My favourite class for lists"

#     def return_iems_lenght(self) -> int:
#         return len(self.items)


# my_list = Mylist(items=[1, 2, 3])

# print(len(my_list))
# print(my_list.return_iems_lenght())

# print(my_list)

# print(bool(my_list))

# print(dir(Mylist))

# my_list = [1, 2, 3, 4, 5]

# print(len(my_list))     # __len__


# class MyDict:
#     def __init__(self, data: dict) -> None:
#         self.data = data

#     def __str__(self) -> str:
#         return "Awesome dic class"

#     def __getitem__(self, key: str):
#         return self.data[key]


# my_dict = MyDict(data={"a": 1, "b": 2})

# print(my_dict["a"])
# print(my_dict.data["a"])


# from typing import List

# Image = List[List[int]]


# def flatten_image(image: Image) -> List:  # custom type Image
#     flat_list = []
#     for sublist in image:
#         for item in sublist:
#             flat_list.append(item)
#     return flat_list


# image = [[1, 2, 3], [4, 5, 6]]


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError(
            "unsupported operand type(s) for +: 'Vector' and '{}'".format(
                type(other).__name__
            )
        )

    def __radd__(self, other: "Vector") -> "Vector":
        return self.__add__(other)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y)  # 4 6
v4 = 2 + v1
print(v4.x, v4.y)  # 3 4
