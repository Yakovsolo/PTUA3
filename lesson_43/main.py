"""Google is launching a network of autonomous pizza delivery drones and wants 
you to create a flexible rewards system (Pizza Points™) that can be tweaked in 
the future. The rules are simple: if a customer has made at least N orders of at 
least Y price, they get a FREE pizza!
Create a function that takes a dictionary of customers, a minimum number of orders 
and a minimum order price. Return a list of customers that are eligible for a free pizza."""

from typing import Dict, List


def eligible_customers(
    customers_dict: Dict[str, List[float]],
    min_orders: int,
    min_order_price: float,
) -> List[str]:
    eligible_customers = []
    for customer, orders in customers_dict.items():
        number_of_orders = len(orders)
        total_price = sum(orders)
        if number_of_orders >= min_orders and total_price >= min_order_price:
            eligible_customers.append(customer)
    return eligible_customers


if __name__ == "__main__":
    customers = {
        "Ann": [12.5, 8.8, 15.45, 5, 22.5],
        "Ben": [13.4, 57.5, 32.4],
        "John": [11.4, 35.5, 22.6, 18.5],
    }
    print(
        eligible_customers(customers_dict=customers, min_orders=3, min_order_price=50)
    )
