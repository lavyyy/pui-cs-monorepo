import sys
from User import User


class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.firstname = None
        self.lastname = None
        self.db = None

    def __str__(self):
        return (
            f"Username: {self.username}\nFirst Name: {self.firstname}\nLast Name: {self.lastname}"
        )

    def start(self):
        from Database import Database

        if self.db is None:
            self.db = Database.get_instance()

        if self.firstname is None or self.lastname is None:
            self.firstname = self.db.get_student_firstname(self.username)
            self.lastname = self.db.get_student_lastname(self.username)

        while True:
            print("Select an option:")
            print("1. View Courses")
            print("2. Drop Course")
            print("3. Exit")

            option = input()

            match option:
                case "1":
                    self.view_courses()
                case "2":
                    self.drop_course()
                case "3":
                    print("Goodbye!")
                    sys.exit()
                case _:
                    print("Invalid option!")

    def view_courses(self):
        courses = self.db.get_courses(self.username)
        if courses is not None:
            print("Courses:")
            for course in courses:
                print(course)
        else:
            print("You are not enrolled in any courses!")

    def drop_course(self):
        course_identifier = input("Enter course identifier: ")

        if self.db.get_course_by_id(course_identifier) is None:
            print("Course does not exist!")
            return

        if self.db.drop_course(self.username, course_identifier):
            print("Course dropped!")
        else:
            print("Failed to drop course!")
