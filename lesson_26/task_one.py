# Task Nr.1:

# Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and Space Shuttle classes.
# Create a simple calculator with:

# Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).

# Through the main class you should be able to calculate the mission cost which includes:
# fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).

# Prepare the final report in the file document and on screen with a method get_full_report with all gathered and calculated data.

from abc import ABC, abstractmethod
import datetime
from typing import Dict
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Carrier:
    """Cost  - shuttle cost in USD,
    Year built - year, when shuttle was built,
    Weight - shuttle weight in kg"""

    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        self._cost: float = cost
        self._year_built: int = year_built
        self._weight: float = weight

    def get_age(self) -> int:
        current_year = datetime.date.today().year
        age = current_year - self._year_built
        return age

    def get_cost(self) -> float:
        return self._cost

    def get_weight(self) -> float:
        return self._weight


class SpaseShuttle(Carrier):
    CEPAJAV_CONSTANT = 2500
    """Use imperial units for the lenght measurements"""

    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        super().__init__(cost, year_built, weight)
        self.fuel_cost = None
        self.average_personals_exp = None

    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        return self.CEPAJAV_CONSTANT / orbit_height

    def get_fuel_cost(
        self, fuel_cost: float, burn_rate: float, orbit_height: float
    ) -> float:
        burn_rate_variable = self._get_burn_rate_variable(orbit_height)
        self.fuel_cost = fuel_cost * burn_rate * burn_rate_variable
        return self.fuel_cost

    def get_average_personals_expenses(
        self, base_salary: float, people_count: int
    ) -> float:
        self.average_personals_exp = base_salary * people_count
        return self.average_personals_exp

    def calculate_mission_cost(
        self,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        base_salary: float,
        people_count: int,
    ) -> float:
        expedition_fuel_cost = self.get_fuel_cost(fuel_cost, burn_rate, orbit_height)
        average_personel_cost = self.get_average_personals_expenses(
            base_salary, people_count
        )
        return expedition_fuel_cost + average_personel_cost

    def get_full_report(self) -> None:
        #  Prepare the final report in the file document and on screen with a method get_full_report with all gathered and calculated data.
        mission_data = {
            "Shuttle age": self.get_age(),
            "Shuttle cost": self.get_cost(),
            "Shuttle year built": self._year_built,
            "Shuttle weight": self.get_weight(),
            "Fuel cost": self.fuel_cost,
        }
        print(mission_data)


my_shuttle = SpaseShuttle(cost=5000, year_built=1979, weight=500)
print(
    my_shuttle.calculate_mission_cost(
        fuel_cost=5.5,
        burn_rate=8.7,
        orbit_height=200,
        base_salary=25000,
        people_count=85,
    )
)

my_shuttle.get_full_report()
