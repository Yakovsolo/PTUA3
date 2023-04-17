'''Task Nr.3:

Create a class called Book that takes title, author, and ISBN as parameters. The class should have __bool__, __repr__, 
__len__, __str__, __eq__, __add__, and __getitem__ methods defined.

The __bool__ method should return True if the book has a title, False otherwise.
The __repr__ method should return a string in the format "Book(title, author, ISBN)" where title, author and ISBN are the 
respective attributes of the class
The __len__ method should return the number of pages of the book
The __str__ method should return a string in the format "title by author (ISBN)"
The __eq__ method should compare two books and return True if both ISBN are the same and False otherwise.
The __add__ method should add two books and return a new book object that contains the contents of both books concatenated 
and the title of the new book should be the title of the first book
The __getitem__ method should return the title of the book if the index passed is 0, and the author of the book if the index passed is 1.'''

class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def
