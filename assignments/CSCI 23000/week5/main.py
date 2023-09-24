"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 5
Date: 9/24/2023
"""

from utils import get_budget, get_total_budget


def main():
    # Formatted as "Movie Name, Year of release, Budget"
    movie_data = "Movie1, 2019, 500_000; Movie2, 2023, 1_000_000; Movie3, 2025, 1_500_000; Movie4, 2027, 2_000_000; Movie5, 2029, 2_500_000"

    # Task 1: Get the budget of Movie3
    print(get_budget(movie_data, "Movie3"))

    # Task 2: Add up the budgets of all the movies
    print(get_total_budget(movie_data))


if __name__ == "__main__":
    main()
