"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 3
Date: 9/07/2023
"""

import string
import random
from typing import List

# Global constants
PASSWORD_LENGTH = 25;

"""
Password Generator
Generates a random password of a given length
"""

def passwordGenerator(length: int):
    # Constants
    types = ["UPPERCASE", "LOWERCASE", "NUMBER", "SYMBOL"];
    symbols = ["!", "@", "#", "$", "%", "&"];
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];

    # Initalizes password list
    password_list: List[str] = [];

    # Returns a random character depending on the type
    def getRandomCharacter(type: str):
        # Matches the type to one of the types defined in the types list
        match type:
            case "UPPERCASE":
                return random.choice(string.ascii_uppercase);
            case "LOWERCASE":
                return random.choice(string.ascii_lowercase);
            case "NUMBER":
                return random.choice(numbers);
            case "SYMBOL":
                return random.choice(symbols);

    # For every number in the length, add a random character to the list
    for _ in range(length):
        # Picks a random type from the type list
        index_type = random.choice(types);

        # Adds a random character to the list
        password_list.append(getRandomCharacter(index_type));

    # Joins every element of the list together to make a single string
    def joinList(list: List[str]):
        return "".join(list);

    return joinList(password_list);

print("Your password is: " + passwordGenerator(PASSWORD_LENGTH));
