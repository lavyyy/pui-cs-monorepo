from book import Book

class Textbook(Book):    
    def __init__(self, title, author, pages, grade_level, edition):
        super().__init__(title, author, pages)
        self.grade_level = grade_level
        self.edition = edition
    
    def __str__(self):
        return super().__str__() + f". Grade level: {self.grade_level}. Edition: {self.edition}"

    # New Methods
    def is_for_grade(self, grade):
        return self.grade_level == grade

    def describe_edition(self):
        return f"This is a {self.edition} edition textbook."

    # Getters
    def get_grade_level(self):
        return self.grade_level

    def get_edition(self):
        return self.edition
   
    # Setters
    def set_grade_level(self, grade_level):
        self.grade_level = grade_level
    
    def set_edition(self, edition):
        self.edition = edition
