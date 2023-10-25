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
            address=user_data[user].get("address"),
            age=user_data[user].get("age"),
            private_access=has_private_access(user_data[user]),
        )

    return new_dict


# Loops over each user in the data provided and checks if it input exists within the nested data
def search_data(user_input, user_data: dict):
    data_found = ""

    for user in user_data:
        if user_input in user_data[user]:
            data_found += f"{user_data[user].get(user_input)}, "

    if len(data_found) == 0:
        return None

    return data_found.rstrip(", ")