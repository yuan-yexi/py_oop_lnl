# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass


@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    def book_info(self):
        return f"{self.title}, by {self.author}."


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
# these are automatically implemented in data classes
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
# these are automatically implemented in data classes
print( b1 == b2)

# TODO: change some fields
print(b1.book_info())
