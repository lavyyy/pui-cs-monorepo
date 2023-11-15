"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 11
Date: 11/14/2023
"""

from book import Book
from textbook import Textbook

def main():
    # Create and use a Book object
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 208)
    print(book)
    print("Is 'The Great Gatsby' a long read?", book.is_long_read())
    book.set_author("Fitzgerald")
    print("Updated book:", book)

    # Create and use a Textbook object
    textbook = Textbook("Calculus: Early Transcendentals", "James Stewart", 1368, "Freshman", 8)
    print(textbook)
    print("Is the textbook for Freshman?", textbook.is_for_grade("Freshman"))
    print(textbook.describe_edition())
    textbook.set_edition(9)
    print("Updated textbook:", textbook)

if __name__ == "__main__":
    main()
