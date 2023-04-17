# Task Nr.4:

# Create a class to represent a library system. The library system should have a collection of books that can be
# borrowed by users. Users can register to the library system, borrow books, and return books. The library system should
# keep track of the books borrowed by users, and the number of available copies of each book.


from typing import Dict, List


class Book:
    def __init__(self, author: str, title: str, number_of_copies: int) -> None:
        self.author = author
        self.title = title
        self.number_of_copies = number_of_copies


class User:
    def __init__(self, username: str) -> None:
        self.username = username
        self.books_borrowed: List[Book] = []


class LibrarySystem:
    books: List[Book] = []
    users: List[User] = []

    @classmethod
    def add_book(cls, book: Book) -> None:
        cls.books.append(book)

    @classmethod
    def add_user(cls, user: User) -> None:
        cls.users.append(user)

    @classmethod
    def borrow_book(cls, user: User, book: Book) -> None:
        for library_book in cls.books:
            if book.author == library_book.author and book.title == library_book.title:
                if library_book.number_of_copies > 0:
                    library_book.number_of_copies -= 1
                    user.books_borrowed.append(book)
                    print(f"Here is yours {book.author}'s {book.title}")
                    return
                else:
                    print(
                        f"Excuse me, but all copies of {book.author}'s {book.title} are borrowed"
                    )
                return
        else:
            print(f"Excuse me, but we didn't have {book.author}'s {book.title}")

    @classmethod
    def return_book(cls, user: User, book: Book) -> None:
        for user_book in user.books_borrowed:
            if book.author == user_book.author and book.title == user_book.title:
                book.number_of_copies += 1
                user.books_borrowed.remove(book)
                print(f"{user.username} has returned {book.author}'s {book.title}.")
                return
        print("Sorry, the user has not borrowed the book with the given ISBN.")

    @classmethod
    def list_of_books(cls) -> List[Book]:
        return cls.books

    @classmethod
    def list_of_users(cls) -> List[User]:
        return cls.users


if __name__ == "__main__":

    def add_new_books():
        add_books_number = int(
            input(f"Please enter a number of books you want to add to library: \n")
        )
        for _ in range(add_books_number):
            author, title, quantity = input(
                "Please enter a book you want to add (author, title, quantity): \n"
            ).split(",")
            new_book = Book(author=author, title=title, number_of_copies=int(quantity))
            LibrarySystem.add_book(new_book)

    def add_new_user():
        add_users_number = int(
            input(f"Please enter a number of users you want to register: \n")
        )

        for _ in range(add_users_number):
            username = input(f"Please enter new user's name: \n")
            new_user = User(username=username)
            LibrarySystem.add_user(new_user)

            books = LibrarySystem.list_of_books()
            for book in books:
                print(
                    f"{book.title} by {book.author}, Copies available: {book.number_of_copies}"
                )
