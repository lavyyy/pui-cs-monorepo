"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 9
Date: 10/31/2023
"""

from lab9_utils import load_data, add_column, save_data


def main():
    source_filepath = (
        "Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv"
    )
    data = load_data(source_filepath)
    data = add_column(data)
    save_data("out", "processed_data.csv", data)


if __name__ == "__main__":
    main()
