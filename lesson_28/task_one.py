# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and add static methods to transform those to Celsius and Fahrenheit units. Use OOP abstraction.

from abc import ABC, abstractmethod


class ConversionTool(ABC):
    @abstractmethod
    def kelvin_to_celsius(self) -> str:
        pass

    @abstractmethod
    def kelvin_to_farenheit(self) -> str:
        pass


class TemperatureConverter(ConversionTool):
    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> str:
        temperature_in_celsius = round((kelvin - 273.15), 2)
        return f"Converted {kelvin}K to {temperature_in_celsius}C"

    @staticmethod
    def kelvin_to_farenheit(kelvin: float) -> str:
        temperature_in_farenheit = round(((kelvin - 273.15) * (9 / 5) + 32), 2)
        return f"Converted {kelvin}K to {temperature_in_farenheit}F"


print(TemperatureConverter.kelvin_to_celsius(283))

print(TemperatureConverter.kelvin_to_farenheit(283))

# output:

# Converted 283K to 9.85C
# Converted 283K to 49.73F
