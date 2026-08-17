class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, isbn, patron_id):
        book = None
        patron = None

        for b in self.books:
            if b.isbn == isbn:
                book = b

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p

        if book and patron:
            if book.borrow():
                patron.borrow_book(book)
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
        else:
            print("Book or patron not found.")

    def return_book(self, isbn, patron_id):
        book = None
        patron = None

        for b in self.books:
            if b.isbn == isbn:
                book = b

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p

        if book and patron:
            book.return_book()
            patron.return_book(book)
            print("Book returned successfully.")
        else:
            print("Book or patron not found.")


# Main Program

library = Library()

# Add books
book1 = Book("Python Programming", "John Smith", "101")
book2 = Book("Data Structures", "Robert Brown", "102")

library.add_book(book1)
library.add_book(book2)

# Register patrons
patron1 = Patron("Aayush", "P01")
patron2 = Patron("Rahul", "P02")

library.register_patron(patron1)
library.register_patron(patron2)

# Borrow books
library.borrow_book("101", "P01")
library.borrow_book("102", "P02")

# Display borrowed books
print("\nPatron Information:")
print(patron1.name, "has borrowed:",
      [book.title for book in patron1.borrowed_books])

print(patron2.name, "has borrowed:",
      [book.title for book in patron2.borrowed_books])

# Return book
library.return_book("101", "P01")

# Display updated information
print("\nAfter returning the book:")
print(patron1.name, "has borrowed:",
      [book.title for book in patron1.borrowed_books])
