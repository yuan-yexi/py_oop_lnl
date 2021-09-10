# Class: blueprint for creating objects of a particular type
# Methods: Regular functions that are part of a class
# Attributes: Variables that hold data that are part of a class
# Object: A specific instance of a class
# Inheritance: Means by which a class can inherit capabilities from another class
# Composition: Means of building complex objects out of other objects

from typing import Union

# Basic class definition
# TODO: create a basic class
class Book:
    # TODO: properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __book_list = None

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list == None:
            Book.__book_list = []
        
        return Book.__book_list

    def __init__(self, title: str, author: str, pages: int, price: float, booktype: str) -> Union[str, int, float]:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."

        # using the class level BOOK_TYPES
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    # TODO: create instance methods
    def get_price(self) -> int:
        # check if the _discount attr is defined in the object instance, if true, apply discounted price
        if hasattr(self, "_discount"):
            return round(self.price - (self.price * self._discount), 2)
        return self.price

    def set_discount(self, pct: float) -> float:
        # _ underscore hints that the method is internal to the class
        self._discount = pct

class Newspaper:
    def __init__(self, name: str) -> None:
        self.name = name

# TODO: access the class attribute
print("Book Types:", Book.get_book_types())

# TODO: create instances of the class
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95, "HARDCOVER")
book2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95, "PAPERBACK")

newspaper1 = Newspaper("The New York Times")

# TODO: print the class and property
print(book1)
print(f"Before discount: {book1.get_price()}")

# TODO: apply the discount method to the book1 instance
book1.set_discount(0.05)
print(f"After discount: {book1.get_price()}")

# TODO: double underscore attrs are hidden by the interpreter
# * However it is still accessible by adding the class name to the attr
print(book1._Book__secret) # this returns "This is a secret attribute"

# TODO: use type() to inspect the object type
print(type(book1)) # <class '__main__.Book'>
print(type(newspaper1)) # <class '__main__.Newspaper'>

# TODO: compare the book and newspaper class instances
if type(book1) == type(book2):
    print(True)
else:
    print(False)

if type(book1) == type(newspaper1):
    print(True)
else:
    print(False)

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(book1, Book)) # True
print(isinstance(newspaper1, Newspaper)) # True
print(isinstance(book2, Newspaper)) # False
print(isinstance(book2, object)) # True

# TODO: Use the static method to access a singleton object
thebooks = Book.get_book_list()
thebooks.append(book1)
thebooks.append(book2)
print(thebooks)
