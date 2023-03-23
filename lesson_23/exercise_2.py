# Task Nr.2:

# Create an abstract class Money which takes currency and value as input and initializes it. A class must have these methods:

# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input and converts the value of the money to the target currency.
#
# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination of the cash as input in the constructor, and should
# implement the convert_to_currency method.
# The Card class should take the credit limit of the card as input in the constructor, and should implement
# the convert_to_currency method using the conversion rate to convert the value of the card to the target currency.

from abc import ABC, abstractmethod
from typing import Dict


class Money(ABC):
    def __init__(self, currency: str, value: float) -> None:
        self.currency = currency
        self.value = value

    def get_currency(self):
        return self.currency

    def get_value(self):
        return self.value

    @abstractmethod
    def convert_to_currency(
        self, target_currency: str, coversation_rate: Dict[str, float]
    ) -> float:
        pass


class Cash(Money):
    def __init__(self, currency: str, value: float, denomination_index: float) -> None:
        self.currency = currency
        self.value = value
        self.denomination_index = denomination_index
        super().__init__(currency=currency, value=value)

    def convert_to_currency(
        self, target_currency: str, conversation_rate: Dict[str, float]
    ) -> float:
        self.value = round(
            self.value
            * conversation_rate[self.currency]
            * conversation_rate[target_currency],
            2,
        )
        return self.value


class Card(Money):
    def __init__(self, currency: str, value: float, credit_limit: int) -> None:
        self.currency = currency
        self.value = value
        self.credit_limit = credit_limit
        super().__init__(currency=currency, value=value)

    def convert_to_currency(
        self, target_currency: str, conversation_rate: Dict[str, float]
    ) -> float:
        self.value = round(
            self.value
            * conversation_rate[self.currency]
            * conversation_rate[target_currency],
            2,
        )
        return self.value


my_currency = Cash("CNY", 999.56, 0.88)
print(my_currency.convert_to_currency("USD", {"EUR": 1.1, "USD": 1, "CNY": 1.5}))

my_other_currency = Card("USD", 1560.20, 10000)
print(my_other_currency.convert_to_currency("CNY", {"EUR": 1.1, "USD": 1, "CNY": 1.5}))
