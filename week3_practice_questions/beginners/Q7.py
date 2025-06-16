# 🔹 Q7: Library System
# Create class Book and class Library.

# Book has title and author

# Library can store list of books, and method display_books()

# Add 2 books to library and print them.


class Book:
  def __init__(self, author, title):
    self.author = author
    self.title = title

class Library:
  def __init__(self):
    self.books_list = []

  def add_books(self, book):
    self.books_list.append(book)

  def display_books(self):
    for book in self.books_list:
      print(f"Title: {book.title}, Author: {book.author}")


book1 = Book("Santosh Shah", "The Himalayans")
book2 = Book("Hariom Shah", "The Everest")

libry = Library()
libry.add_books(book1)
libry.add_books(book2)

libry.display_books()
