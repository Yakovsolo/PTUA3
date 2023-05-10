class Menu:
    def __init__(self, name, weight, prep_time, calories, price):
        self.name = name
        self.weight = weight
        self.prep_time = prep_time
        self.calories = calories
        self.price = price


class Breakfast(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Breakfast"


class Lunch(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Lunch"


class Dinner(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Dinner"


class Alcohol(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Alcohol"


class AlcoholFree(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Alcohol Free"


class Vegetarian(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Vegetarian"


class Vegan(Menu):
    def __init__(self, name, weight, prep_time, calories, price):
        super().__init__(name, weight, prep_time, calories, price)
        self.category = "Vegan"


menu = {
    "Breakfast": {
        {
            "name": "Egg and Toast",
            "weight": "200g",
            "prep_time": "10 mins",
            "calories": "250 cal",
            "price": 4.99,
        },
        {
            "name": "Pancakes",
            "weight": "300g",
            "prep_time": "15 mins",
            "calories": "350 cal",
            "price": 5.99,
        },
        {
            "name": "Bagel with Cream Cheese",
            "weight": "150g",
            "prep_time": "5 mins",
            "calories": "200 cal",
            "price": 3.99,
        },
    },
    "Lunch": {
        {
            "name": "Burger and Fries",
            "weight": "500g",
            "prep_time": "20 mins",
            "calories": "800 cal",
            "price": 9.99,
        },
        {
            "name": "Caesar Salad",
            "weight": "350g",
            "prep_time": "10 mins",
            "calories": "400 cal",
            "price": 7.99,
        },
        {
            "name": "Chicken Sandwich",
            "weight": "300g",
            "prep_time": "15 mins",
            "calories": "500 cal",
            "price": 8.99,
        },
    },
    "Dinner": {
        {
            "name": "Steak and Mashed Potatoes",
            "weight": "700g",
            "prep_time": "30 mins",
            "calories": "1200 cal",
            "price": 19.99,
        },
        {
            "name": "Seafood Paella",
            "weight": "500g",
            "prep_time": "25 mins",
            "calories": "800 cal",
            "price": 16.99,
        },
        {
            "name": "Vegetable Lasagna",
            "weight": "400g",
            "prep_time": "20 mins",
            "calories": "500 cal",
            "price": 14.99,
        },
    },
    "Drinks": {
        {
            "name": "Coca-Cola",
            "weight": "350ml",
            "prep_time": "0 mins",
            "calories": "150 cal",
            "price": 1.99,
        },
        {
            "name": "Orange Juice",
            "weight": "350ml",
            "prep_time": "0 mins",
            "calories": "100 cal",
            "price": 2.49,
        },
        {
            "name": "Mojito",
            "weight": "400ml",
            "prep_time": "5 mins",
            "calories": "200 cal",
            "price": 6.99,
        },
        {
            "name": "Virgin Mojito",
            "weight": "400ml",
            "prep_time": "5 mins",
            "calories": "100 cal",
            "price": 4.99,
        },
        {
            "name": "Beer",
            "weight": "500ml",
            "prep_time": "0 mins",
            "calories": "200 cal",
            "price": 3.99,
        },
    },
    "Vegetarian": {
        {
            "name": "Vegetable Soup",
            "weight": "300g",
            "prep_time": "10 mins",
            "calories": "250 cal",
        }
    },
}
