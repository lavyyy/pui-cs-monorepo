from book import Book


class Bookshelf:
    def __init__(
        self,
        shelf_id: int,
        capacity: int,
        books: list[Book],
    ):
        self.id = shelf_id
        self.capacity = capacity
        self.books = books

    def __str__(self):
        return f"Bookshelf #{self.id} with a capacity of {self.capacity}"

    # Getters
    def get_books(self) -> list[Book]:
        return self.books

    def get_id(self) -> int:
        return self.id

    # Setters
    def set_id(self, shelf_id: int):
        self.id = shelf_id

    def set_capacity(self, capacity: int):
        self.capacity = capacity

    # Actions
    def find_book_by_title(self, title) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
        else:
            print(
                f"The max capacity of the bookshelf has been reached, the maximum capacity is {self.capacity}"
            )

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
