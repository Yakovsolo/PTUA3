"""Task Nr.1:

You have been asked to create a simple inventory management system for a small retail store. 
You need to define a Product class using the dataclass module that represents a product in the store. 
Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock. 
You also need to implement a method calculate_total_cost that calculates the total cost of a given number 
of items of the product, taking into account any discounts that may apply."""


from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def calculate_total_cost(
        self,
        number_of_items: Optional[int] = None,
    ) -> float:
        if number_of_items is None:
            return self.price * self.quantity
        else:
            return self.price * number_of_items


new_product = Product(
    id=1, name="apples", description="green", price=2.90, quantity=150
)

print(new_product.calculate_total_cost(5))

print(new_product.calculate_total_cost())
