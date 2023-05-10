"""You need to create a program to manage a list of books in a library. Each book has a title, an author, a publication 
year, and an ISBN. You need to define a Book class using the dataclass module that contains attributes for these properties. 
You also need to implement a Library class that manages a list of books. The Library class should allow you to add and remove 
books from the library, search for books by title or author, and display the list of books currently in the library."""

from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    isbn: str


class Library:
    books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn: str) -> None:
        for library_book in self.books:
            if library_book.isbn == isbn:
                self.books.remove(library_book)

    def find_book_by_isbn(self, isbn: str) -> str:
        for library_book in self.books:
            if isbn == library_book.isbn:
                return f"We have this book:\n {library_book.title} by {library_book.author}"
        return f"We have no book you are looking for"

    def find_book_by_title(self, title: str) -> str:
        for library_book in self.books:
            if title == library_book.title:
                return f"We have this book:\n {library_book.title} by {library_book.author}"
        return f"We have no book you are looking for"

    def get_list_of_books(self) -> None:
        for book in self.books:
            print(
                f"{book.title} by {book.author}, publication year: {book.publication_year}, ISBN: {book.isbn}"
            )


if __name__ == "__main__":
    first_book = Book(
        title="Solar Queen",
        author="A. Norton",
        publication_year=2004,
        isbn="978-0765300553",
    )
    second_book = Book(
        title="Nine Princes In Amber",
        author="R. Zelazny",
        publication_year=1977,
        isbn="978-0380014309",
    )
    third_book = Book(
        title="The Stainless Steel Rat",
        author="H. Harrison",
        publication_year=1997,
        isbn="978-1857984989",
    )

    my_library = Library()
    my_library.add_book(first_book)
    my_library.add_book(second_book)
    my_library.add_book(third_book)

    print(my_library.find_book_by_isbn(isbn="978-0765300553"))
    print(my_library.find_book_by_isbn(isbn="978-0765300554"))
    print(my_library.find_book_by_title(title="Nine Princes In Amber"))
    my_library.get_list_of_books()

    my_library.remove_book("978-1857984989")
    my_library.get_list_of_books()

# output:
# We have this book:
#  Solar Queen by A. Norton

# We have no book you are looking for

# We have this book:
#  Nine Princes In Amber by R. Zelazny

# Solar Queen by A. Norton, publication year: 2004, ISBN: 978-0765300553
# Nine Princes In Amber by R. Zelazny, publication year: 1977, ISBN: 978-0380014309
# The Stainless Steel Rat by H. Harrison, publication year: 1997, ISBN: 978-1857984989

# Solar Queen by A. Norton, publication year: 2004, ISBN: 978-0765300553
# Nine Princes In Amber by R. Zelazny, publication year: 1977, ISBN: 978-0380014309
