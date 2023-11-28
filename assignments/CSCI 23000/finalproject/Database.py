from __future__ import annotations
import os
from User import User
from Admin import Admin
from Student import Student


# Singleton
class Database:
    instance: Database | None = None

    def __init__(self):
        if Database.instance is None:
            Database.instance = self
        else:
            raise Exception("Database instance already exists.")

        if not os.path.exists("db"):
            os.mkdir("db")

        if not os.path.exists("db/users.csv"):
            with open(
                "db/users.csv",
                "w",
                encoding="utf-8",
            ) as f:
                f.write("id,username,password,firstname,lastname\n")

        if not os.path.exists("db/courses.csv"):
            with open(
                "db/courses.csv",
                "w",
                encoding="utf-8",
            ) as f:
                f.write("identifier,name,professor\n")

        if not os.path.exists("db/enrollments.csv"):
            with open(
                "db/enrollments.csv",
                "w",
                encoding="utf-8",
            ) as f:
                f.write("student_id,course_identifier\n")

    @staticmethod
    def get_instance() -> Database:
        if Database.instance is None:
            return Database()
        return Database.instance

    def login(self, username, password, role) -> User | None:
        if role == "admin":
            file_name = "db/admins.csv"
        elif role == "student":
            file_name = "db/users.csv"
        else:
            return None

        with open(file_name, "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                # TODO: Use dyanmic indexing
                if rows[1] == username and rows[2] == password:
                    if role == "admin":
                        return Admin(username)
                    if role == "student":
                        return Student(username)

        return None

    def register(self, username, password, firstname, lastname) -> bool:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            last_id = f.readlines()[-1].split(",")[0]
            if last_id.isnumeric():
                new_id = int(last_id) + 1
            else:
                new_id = 1

        with open("db/users.csv", "a", encoding="utf-8") as f:
            f.write(f"{new_id},{username},{password},{firstname},{lastname}\n")
            return True

    def get_courses(self, username: str) -> list[str] | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[1] == username:
                    user_id = rows[0]

        courses = []
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[0] == user_id:
                    courses.append(rows[1])

        if len(courses) == 0:
            return None

        return courses

    def get_all_courses(self) -> list[str] | None:
        courses = []
        with open("db/courses.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                courses.append(rows[0])

        if len(courses) == 0:
            return None

        return courses

    def get_course_by_id(self, course_identifier: str) -> str | None:
        with open("db/courses.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[0] == course_identifier:
                    return f"ID: {rows[0]}\nName: {rows[1]}\nProfessor: {rows[2]}\n"

        return None

    def add_course(self, identifier: str, name: str, professor: str) -> bool:
        with open("db/courses.csv", "a", encoding="utf-8") as f:
            f.write(f"{identifier},{name},{professor}\n")
            return True

    def add_student_to_course(self, username: str, course_identifier: str) -> bool:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[1] == username:
                    user_id = rows[0]

        with open("db/enrollments.csv", "a", encoding="utf-8") as f:
            f.write(f"{user_id},{course_identifier}\n")
            return True

    def get_student(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.split(",")
                if rows[1] == username:
                    return f"Username: {rows[1]}\nFirst Name: {rows[3]}\nLast Name: {rows[4]}\n"

        return None

    def get_student_firstname(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.split(",")
                if rows[1] == username:
                    return rows[3]

        return None

    def get_student_lastname(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.split(",")
                if rows[1] == username:
                    return rows[4]

        return None

    def get_enrollments(self, username) -> list[str] | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[1] == username:
                    user_id = rows[0]

        enrollments = []
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[0] == user_id:
                    enrollments.append(rows[1])

        return enrollments

    def get_students(self) -> list[str] | None:
        students = []
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                students.append(rows[1])

        if len(students) == 0:
            return None

        return students

    def drop_course(self, username: str, course_identifier: str) -> bool:
        user_id = None

        # read users to find the user_id
        with open("db/users.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[1] == username:
                    user_id = rows[0]
                    break

        if user_id is None:
            return False

        updated_enrollments = []
        enrollment_found = False

        # read enrollments and store all except the one to drop
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[0] == user_id and rows[1].strip() == course_identifier:
                    enrollment_found = True
                else:
                    updated_enrollments.append(line)

        # rewrite the enrollments file only if the enrollment was found
        if enrollment_found:
            with open("db/enrollments.csv", "w", encoding="utf-8") as f:
                for line in updated_enrollments:
                    f.write(line)
            return True

        return False
