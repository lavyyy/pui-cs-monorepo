"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 10
Date: 11/07/2023
"""
from book import Book
from bookshelf import Bookshelf


def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "208")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "384")

    inital_books = [book1, book2]

    bookshelf1 = Bookshelf(1, 3, inital_books)
    bookshelf1_id = bookshelf1.get_id()

    new_book = Book("IT", "Stephen King", "1168")
    new_book_title = new_book.get_title()
    new_book_author = new_book.get_author()

    print(f"{new_book_title} by {new_book_author} is being added to bookshelf #{bookshelf1_id}")

    bookshelf1.add_book(new_book)

    print(f"Books in bookshelf #{bookshelf1_id}:")
    for book in bookshelf1.get_books():
        print(book)

    print(f"Attempting to find Of Mice and Men in bookshelf #{bookshelf1_id}")
    book_to_find = bookshelf1.find_book_by_title("Of Mice and Men")
    if book_to_find is None:
        print("Book not found")
    else:
        print(f"Book found: {book_to_find}")


if __name__ == "__main__":
    main()
