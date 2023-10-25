"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 8
Date: 10/24/2023
"""

from utils import generate_new_dictionary, search_data

def main():
    user_data = {}

    # Gets the input from the user to populate the user_data array
    for i in range(5):
        username = str(input(f"Please enter the username for user #{i+1}: "))
        email = str(input(f"Please enter the email for user #{i+1}: "))
        address = str(input(f"Please enter the address for user ${i+1}: "))
        try:
            age = int(input(f"Please enter the age for user #{i+1}: "))
        except ValueError:
            print("Invalid value. Age has to be a numeric value")
            return

        user_data[username] = {
            "email": email,
            "address": address,
            "age": age,
        }

    # Populates a new dict with the private access column.
    user_data_new = generate_new_dictionary(user_data)

    search_input = str(input("Enter the key of the values you'd like to search: "))
    print(f"Search result: {search_data(search_input, user_data_new)}")

    print(f"User data: {user_data}")
    print(f"User data with new access column: {user_data_new}")


if __name__ == "__main__":
    main()
