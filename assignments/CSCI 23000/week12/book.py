class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}. Pages: {self.pages}"

    # Getters
    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_pages(self) -> int:
        return self.pages

    # Setters
    def set_title(self, title: str):
        self.title = title

    def set_author(self, author: str):
        self.author = author

    def set_pages(self, pages: int):
        self.pages = pages

    # Actions
    def is_long_read(self):
        return self.pages >= 300

