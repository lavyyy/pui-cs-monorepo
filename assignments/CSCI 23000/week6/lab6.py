"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 6
Date: 9/28/2023
"""


# Checks each user column for the @barking.dev email and gives them private access.
# (not safe!! but im just following the assignment's rubric of not hard coding indexes)
def has_private_access(user_columns: list):
    for col in user_columns:
        if isinstance(col, str) and col.find("@barking.dev") != -1:
            return True

    return False


# Loops over each row in user_data and appends the new private access column
def populate_access_column(user_data):
    for user in user_data:
        user.append(has_private_access(user))

    return user_data


def main():
    user_data = []

    # Gets the input from the user to populate the user_data array
    for i in range(5):
        username = str(input(f"Please enter the username for user #{i+1}: "))
        email = str(input(f"Please enter the email for user #{i+1}: "))
        age = int(input(f"Please enter the age for user #{i+1}: "))

        user_data.append([username, email, age])

    # Populates a new array with the private access column.
    # Passing in user_data.copy() so we don't modify the original array
    user_data_new = populate_access_column(user_data.copy())

    print(f"User data: {user_data}")
    print(f"User data with new access column: {user_data_new}")


if __name__ == "__main__":
    main()
