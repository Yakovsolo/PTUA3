from typing import List


class Leap:
    @staticmethod
    def check(year: int) -> bool:
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    @staticmethod
    def range(start: int, finish: int) -> List[int]:
        years: list = []
        for year in range(start, finish):
            if Leap.check(year):
                years.append(year)
        return years


if __name__ == "__main__":
    leap = Leap()
    print(Leap.check(2020))
