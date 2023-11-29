import sys
from User import User


class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.db = None

    def __str__(self):
        return f"Admin: {self.username}"

    def start(self):
        from Database import Database

        if self.db is None:
            self.db = Database.get_instance()

        while True:
            print("Select an option:")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Add Student to Course")
            print("4. View Student Info")
            print("5. View Course Info")
            print("6. View Student Enrollments")
            print("7. Exit")

            option = input()

            match option:
                case "1":
                    self.add_student()
                case "2":
                    self.add_course()
                case "3":
                    self.add_student_to_course()
                case "4":
                    self.view_student()
                case "5":
                    self.view_course()
                case "6":
                    self.view_enrollments()
                case "7":
                    print("Goodbye!")
                    sys.exit()

    def add_student(self):
        username = input("Enter username: ")

        # check if username already exists
        if self.db.get_student(username) is not None:
            print("Student already exists!")
            return

        password = input("Enter password: ")

        firstname = input("Enter first name: ")

        lastname = input("Enter last name: ")

        if self.db.register(username, password, firstname, lastname):
            print("Student added!")
        else:
            print("Failed to add student!")

    def add_course(self):
        course_identifier = input("Enter course identifier: ")

        # check if course already exists
        if self.db.get_course_by_id(course_identifier) is not None:
            print("Course already exists!")
            return

        course_name = input("Enter course name: ")

        professor = input("Enter professor: ")

        if self.db.add_course(course_identifier, course_name, professor):
            print("Course added!")
        else:
            print("Failed to add course!")

    def add_student_to_course(self):
        username = input("Enter username: ")

        # check if username exists
        if self.db.get_student(username) is None:
            print("Student does not exist!")
            return

        course_identifier = input("Enter course identifier: ")

        # check if course exists
        if self.db.get_course_by_id(course_identifier) is None:
            print("Course does not exist!")
            return

        # check if student is already enrolled in course
        if self.db.is_student_in_course(username, course_identifier) is True:
            print("Student is already enrolled in course!")
            return

        if self.db.add_student_to_course(username, course_identifier):
            print("Student added to course!")
        else:
            print("Failed to add student to course!")

    def view_student(self):
        username = input("Enter username: ")

        student = self.db.get_student(username)

        if student is not None:
            print(student)
        else:
            print("Student not found!")

    def view_course(self):
        course_identifier = input("Enter course identifier: ")

        course = self.db.get_course_by_id(course_identifier)

        if course is not None:
            print(course)
        else:
            print("Course not found!")

    def view_enrollments(self):
        username = input("Enter username: ")

        if self.db.get_student(username) is None:
            print("Student does not exist!")
            return

        enrollments = self.db.get_enrollments(username)

        if enrollments is not None:
            print(f"Enrollments for student {username}:")
            for enrollment in enrollments:
                print(enrollment)
        else:
            print("No enrollments found!")

    def view_students(self):
        students = self.db.get_students()

        if students is not None:
            print("Students:")
            for student in students:
                print(student)
        else:
            print("No students found!")

    def view_courses(self):
        courses = self.db.get_all_courses()

        if courses is not None:
            print("Courses:")
            for course in courses:
                print(course)
        else:
            print("No courses found!")
