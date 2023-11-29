"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Final Project
Date: 11/23/2023
"""

import sys
from Database import Database


def main():
    db = Database.get_instance()
    logged_in = False
    login_attempts = 0

    # Login/Register loop
    while logged_in is False:
        print("Select an option:")
        print("1. Login as Admin")
        print("2. Login as Student")
        print("3. Register")
        print("4. Exit")

        option = input()

        match option:
            # Admin Login
            case "1":
                username = input("Username: ")
                password = input("Password: ")

                # returns a admin instance
                session = db.login(username, password, "admin")

                if session is not None:
                    print("Logged in!")
                    logged_in = True
                    session.start()
                else:
                    login_attempts += 1
                    if login_attempts < 5:
                        print("Invalid username or password!")
                    else:
                        print("Too many login attempts!")
                        sys.exit()
            # Student Login
            case "2":
                username = input("Username: ")
                password = input("Password: ")

                # returns a student instance
                session = db.login(username, password, "student")

                if session is not None:
                    print("Logged in!")
                    logged_in = True
                    session.start()
                else:
                    login_attempts += 1
                    if login_attempts < 5:
                        print("Invalid username or password!")
                    else:
                        print("Too many login attempts!")
                        sys.exit()
            case "3":
                username = input("Username: ")
                password = input("Password: ")
                firstname = input("First Name: ")
                lastname = input("Last Name: ")

                if db.register(username, password, firstname, lastname):
                    print("Registered!")
                else:
                    print("Failed to register!")

            case "4":
                print("Exiting...")
                sys.exit()

            case _:
                print("Invalid option!")


if __name__ == "__main__":
    main()
