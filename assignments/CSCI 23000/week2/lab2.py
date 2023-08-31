"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 2
Date: 8/31/2023
"""

# Constants
NUM_1 = 5
NUM_2 = 10
NUM_3 = 15
PRINT_TO_CONSOLE = True

# Sets the value of NUM_1 to the sum of NUM_1 and NUM_2
NUM_4 = NUM_1 + NUM_2

# Creates a list of unsorted numbers
unsortedList = [
    NUM_2,
    NUM_3,
    NUM_4,
    NUM_1,
]

# Creates a duplicate of the unsorted list and sorts it from least to greatest
sortedList = unsortedList
sortedList.sort()

# Prints the results of the computation if PRINT_TO_CONSOLE is True
if PRINT_TO_CONSOLE:
    print(
        f"This program first adds {NUM_2} and {NUM_1} together which equals {NUM_4}, then creates a list including those two numbers, as well as {NUM_3} and {NUM_4} in a mixed order: {unsortedList}. It then creates a duplicate of this list and sorts it from least to greatest. The final result is: {sortedList}"
    )
