# pylint: disable=all
# mypy: ignore-errors
# flake8: noqa

from dataclasses import dataclass

# class Position:
#     def __init__(self, name: str, lan: float, long: float) -> None:
#         self.name = name
#         self.lan = lan
#         self.long = long


@dataclass
class Position:
    name: str
    lan: float
    long: float


pos = Position(name="Vilnius", lan=0.01, long=0.01)

print(pos.name, pos.lan, pos.long)
