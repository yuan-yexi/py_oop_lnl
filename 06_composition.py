# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        # created a relationship where a book has an author associated with it
        self.author = author

        self.chapters = []

    # a method that takes a chapter object
    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        result = 0
        for ch in self.chapters:
            result += ch.page_count

        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count

# Create an author
auth1 = Author("Leo", "Tolstoy")
# Create a book
b1 = Book("War and Peace", 39.0, auth1)

# Add chapters to the book
b1.add_chapter(Chapter("Chapter 1", 125))
b1.add_chapter(Chapter("Chapter 2", 97))
b1.add_chapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.get_book_page_count())
