"""Task Nr.4:

Create three different task with real world scenario what would include all 
magic methods we covered today and plus 3 others from the provided list."""


from typing import Union


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
        price: float,
    ) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self) -> str:
        return f"Book title: {self.title}\nBook author: {self.author}\n"

    def __repr__(self) -> str:
        return f"Book title: {self.title}\nBook author: {self.author}\nISBN: {self.isbn}\nPrice: {self.price}"

    def __len__(self) -> int:
        return len(self.isbn)

    def __bool__(self) -> bool:
        if len(self.isbn) != 13:
            return False
        return True

    def __add__(self, other: "Book") -> str:
        return f"Total cost: {self.price + other.price}"

    def __getitem__(self, key: int) -> Union[str, float]:
        if key == 0:
            return self.title
        if key == 1:
            return self.author
        if key == 2:
            return self.isbn
        if key == 3:
            return self.price
        return "There are no attribute, you are ooking for"

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


first_book = Book(
    title="Solar Queen",
    author="Andre Norton",
    isbn="9780765300546",
    price=8.99,
)
second_book = Book(
    title="Nine Princes in Amber",
    author="Roger Zelazny",
    isbn="9780571097821",
    price=12.55,
)

print(first_book)
print(repr(first_book))
print(len(first_book))
print(bool(first_book))
print(first_book[0])
print(second_book[2])
print(second_book[4])
print()

total_cost = first_book + second_book

print(total_cost)

# Output:
# Book title: Solar Queen
# Book author: Andre Norton

# Book title: Solar Queen
# Book author: Andre Norton
# ISBN: 9780765300546
# Price: 8.99
# 13
# True
# Total cost: 21.54
