# What are magic methods
# Automatically associated with every object
# Can be customized to behavior and integrate with the language
# Define how objects are represented as strings
# Control access to attribute values, both for get and set
# Build in comparison and equality testing capabilities
# Allow objects to be callable like functions


# Using the __str__ and __repr__ magic methods
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    # used to return user friendly string function when object is printed
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    # generate developer facing string for debugging purposes
    def __repr__(self) -> str:
        return f"title={self.title}, author={self.author}, price={self.price}"

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Cannot compare Book to a non-Book.")

        return (self.title == o.title and self.author == o.author and self.price == o.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, o: object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Cannot compare Book to a non-Book.")

        return self.price >= o.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Cannot compare Book to a non-Book.")

        return self.price < o.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# print(f"This prints the __str__ method: {b1}")
# print(f"This prints the __str__ method: {b2}")

print("__str__ method: ", str(b1))
print("__repr__ method: ", repr(b2))

# TODO: Check for equality
# since b1 and b3 are the same book with the same attrs
print(b1 == b3) # returns False as they are not the same obj in memory, however adding __eq__ will return True
print(b1 == b2) # returns False

# TODO: Check for greater and lesser value
print(b1 >= b2)
print(b1 < b2)

# TODO: Now we can sort them too
books = [b1, b2, b3, b4]
books.sort() # uses the built in __lt__ to sort, so it will sort by price
print([book.title for book in books])
