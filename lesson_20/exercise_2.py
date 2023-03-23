# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients,
#     add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
#     Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.

from typing import Dict
import pdb


class Smoothie:
    def __init__(self, ingredients_cost: Dict[str, float]) -> None:
        self.ingredients_cost: Dict[str, float] = ingredients_cost

    def get_cost(self) -> float:
        return sum(self.ingredients_cost.values())

    def get_price(self) -> float:
        pdb.set_trace()
        return round((self.get_cost() + self.get_cost() * 1.5), 2)

    def get_name(self) -> str:
        pdb.set_trace()
        name_list = self.ingredients_cost.keys()
        smoothie_name = " ".join(sorted(name_list))
        smoothie_name = smoothie_name.replace("berries", "berry")

        if len(name_list) > 1:
            pdb.set_trace()
            return f"{smoothie_name} fusion"
        else:
            pdb.set_trace()
            return f"{smoothie_name} smoothie"


class BlueberrySmoothie(Smoothie):
    INGREDIENTS_COST = {
        "Blueberries": 2.5,
        "Chocolate": 1.3,
    }

    def __init__(self) -> None:
        super().__init__(ingredients_cost=self.INGREDIENTS_COST)


class AmazingSmoothie(Smoothie):
    INGREDIENTS_COST = {
        "Strawberries": 2.5,
        "Raspberries": 1.3,
        "Mint": 1.5,
        "Milk": 0.75,
    }

    def __init__(self) -> None:
        super().__init__(ingredients_cost=self.INGREDIENTS_COST)


if __name__ == "__main__":
    smoothie_one = BlueberrySmoothie()
    print(smoothie_one.get_name())
    print(smoothie_one.get_cost())
    print(smoothie_one.get_price())

    smoothie_two = AmazingSmoothie()
    print(smoothie_two.get_name())
    print(smoothie_two.get_cost())
    print(smoothie_two.get_price())
