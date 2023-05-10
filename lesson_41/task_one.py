"""Task Nr.1:
Write a Temperature class that has a celsius property and a fahrenheit property. 
The celsius property stores the temperature in Celsius, and the fahrenheit property 
stores the temperature in Fahrenheit. The fahrenheit property should be a computed
property that converts the Celsius temperature to Fahrenheit."""

class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return round((self.celsius * 1.8) + 32, 0)


temperature = Temperature(232.8)
print(f'Temperature in celsius: {temperature.celsius} \nTemperature in farenheit: {temperature.fahrenheit}')