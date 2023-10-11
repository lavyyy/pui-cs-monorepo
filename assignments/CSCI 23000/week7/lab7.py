"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 7
Date: 10/10/2023
"""


# Checks if the email in the user dictionary contains "@barking.dev"
def has_private_access(user: dict):
    email = user.get("email", "")  # Get the email from the user dictionary
    return "@barking.dev" in email


# Uses the provided dict to create a new dict with a private_access column
def generate_new_dictionary(user_data: dict):
    new_dict = {}

    for user in user_data:
        new_dict[user] = dict(
            email=user_data[user].get("email"),
            age=user_data[user].get("age"),
            private_access=has_private_access(user_data[user]),
        )

    return new_dict


# Loops over each user in the data provided and checks if it input exists within the nested data
def search_data(input, user_data: dict):
    data_found = ""

    for user in user_data:
        if input in user_data[user]:
            data_found += f"{user_data[user].get(input)}, "

    if len(data_found) == 0:
        return None

    return data_found.rstrip(", ")


def main():
    user_data = {}

    # Gets the input from the user to populate the user_data array
    for i in range(2):
        username = str(input(f"Please enter the username for user #{i+1}: "))
        email = str(input(f"Please enter the email for user #{i+1}: "))
        try:
            age = int(input(f"Please enter the age for user #{i+1}: "))
        except ValueError:
            print("Invalid value. Age has to be a numeric value")
            return

        user_data[username] = {
            "email": email,
            "age": age,
        }

    # Populates a new array with the private access column.
    # Passing in user_data.copy() so we don't modify the original array
    user_data_new = generate_new_dictionary(user_data)

    search_input = str(input("Enter the key of the values you'd like to search: "))
    print(f"Search result: {search_data(search_input, user_data_new)}")

    print(f"User data: {user_data}")
    print(f"User data with new access column: {user_data_new}")


if __name__ == "__main__":
    main()
