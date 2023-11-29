from __future__ import annotations
import os
from User import User
from Admin import Admin
from Student import Student
from utils import get_index_from_header


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
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )
            password_index = get_index_from_header(
                "password",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username and rows[password_index] == password:
                    if role == "admin":
                        return Admin(username)
                    if role == "student":
                        return Student(username)

        return None

    def register(self, username, password, firstname, lastname) -> bool:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            # get the last id in the file
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
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            user_id_index = get_index_from_header(
                "id",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username:
                    user_id = rows[user_id_index]

        courses = []
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            user_id_index = get_index_from_header(
                "student_id",
                header,
            )

            course_id_index = get_index_from_header(
                "course_identifier",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[user_id_index] == user_id:
                    courses.append(rows[course_id_index])

        if len(courses) == 0:
            return None

        return courses

    def get_all_courses(self) -> list[str] | None:
        courses = []
        with open("db/courses.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            course_id_index = get_index_from_header(
                "identifier",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                courses.append(rows[course_id_index])

        if len(courses) == 0:
            return None

        return courses

    def get_course_by_id(self, course_identifier: str) -> str | None:
        with open("db/courses.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            identifier_index = get_index_from_header(
                "identifier",
                header,
            )

            name_index = get_index_from_header(
                "name",
                header,
            )

            professor_index = get_index_from_header(
                "professor",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[identifier_index] == course_identifier:
                    return f"ID: {rows[identifier_index]}\nName: {rows[name_index]}\nProfessor: {rows[professor_index]}\n"

        return None

    def add_course(self, identifier: str, name: str, professor: str) -> bool:
        with open("db/courses.csv", "a", encoding="utf-8") as f:
            f.write(f"{identifier},{name},{professor}\n")
            return True

    def add_student_to_course(self, username: str, course_identifier: str) -> bool:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            id_index = get_index_from_header(
                "id",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username:
                    user_id = rows[id_index]

        with open("db/enrollments.csv", "a", encoding="utf-8") as f:
            f.write(f"{user_id},{course_identifier}\n")
            return True

    def get_student(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            firstname_index = get_index_from_header(
                "firstname",
                header,
            )

            lastname_index = get_index_from_header(
                "lastname",
                header,
            )

            for line in f.readlines():
                rows = line.split(",")
                if rows[username_index] == username:
                    return f"Username: {rows[username_index]}\nFirst Name: {rows[firstname_index]}\nLast Name: {rows[lastname_index]}\n"

        return None

    def get_student_firstname(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            firstname_index = get_index_from_header(
                "firstname",
                header,
            )

            for line in f.readlines():
                rows = line.split(",")
                if rows[username_index] == username:
                    return rows[firstname_index]

        return None

    def get_student_lastname(self, username: str) -> str | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            lastname_index = get_index_from_header(
                "lastname",
                header,
            )

            for line in f.readlines():
                rows = line.split(",")
                if rows[username_index] == username:
                    return rows[lastname_index]

        return None

    def get_enrollments(self, username) -> list[str] | None:
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            id_index = get_index_from_header(
                "id",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username:
                    user_id = rows[id_index]

        enrollments = []
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            user_id_index = get_index_from_header(
                "student_id",
                header,
            )

            course_id_index = get_index_from_header(
                "course_identifier",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[user_id_index] == user_id:
                    enrollments.append(rows[course_id_index])

        if len(enrollments) == 0:
            return None

        return enrollments

    def get_students(self) -> list[str] | None:
        students = []
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                students.append(rows[username_index])

        if len(students) == 0:
            return None

        return students

    def drop_course(self, username: str, course_identifier: str) -> bool:
        user_id = None

        # read users to find the user_id
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            id_index = get_index_from_header(
                "id",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username:
                    user_id = rows[id_index]
                    break

        if user_id is None:
            return False

        updated_enrollments = []
        enrollment_found = False

        # read enrollments and store all except the one to drop
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            id_index = get_index_from_header(
                "student_id",
                header,
            )

            course_id_index = get_index_from_header(
                "course_identifier",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[id_index] == user_id and rows[course_id_index].strip() == course_identifier:
                    enrollment_found = True
                else:
                    updated_enrollments.append(line)

        # rewrite the enrollments file only if the enrollment was found
        if enrollment_found:
            with open("db/enrollments.csv", "w", encoding="utf-8") as f:
                # put the header back
                f.write(header)
                for line in updated_enrollments:
                    f.write(line)
            return True

        return False

    def is_student_in_course(self, username: str, course_identifier: str) -> bool:
        user_id = None

        # read users to find the user_id
        with open("db/users.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            username_index = get_index_from_header(
                "username",
                header,
            )

            id_index = get_index_from_header(
                "id",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[username_index] == username:
                    user_id = rows[id_index]
                    break

        if user_id is None:
            return False

        # read enrollments and check if the user_id and course_identifier are in the file
        with open("db/enrollments.csv", "r", encoding="utf-8") as f:
            header = f.readline()

            id_index = get_index_from_header(
                "student_id",
                header,
            )

            course_id_index = get_index_from_header(
                "course_identifier",
                header,
            )

            for line in f.readlines():
                rows = line.replace("\n", "").split(",")
                if rows[id_index] == user_id and rows[course_id_index].strip() == course_identifier:
                    return True

        return False
