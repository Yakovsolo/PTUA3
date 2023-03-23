# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deck After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

from random import shuffle


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Cards remaining in deck: {len(self.deck)}"

    def shuffle(self):
        if len(self.deck) < 52:
            raise ValueError("For shuffle you must have at least 52 cards in the deck")
        shuffle(self.deck)
        return self

    def deal(self):
        if len(self.deck) == 0:
            raise ValueError("Deck of cards has ended")
        return self.deck.pop()


my_cards = Deck()
print(my_cards.deck)


print(my_cards.shuffle())
print(my_cards.deck)
print(my_cards.__repr__())
print(my_cards.deal())
print(my_cards.__repr__())
print(my_cards.deal())
print(my_cards.__repr__())
