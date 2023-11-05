"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 9
Date: 10/31/2023
"""

import os


def parse_line(line):
    fields = []
    field = ""
    in_quotes = False

    for char in line:
        if char == '"':
            in_quotes = not in_quotes  # Toggle in_quotes status
        elif char == "," and not in_quotes:
            fields.append(field.strip())  # Strip to remove any unwanted whitespace
            field = ""
        else:
            field += char

    fields.append(field.strip())  # Add the last field
    return fields


def load_data(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        data = [parse_line(line) for line in lines]
    return data


def add_column(data):
    header = data[0]
    rows = data[1:]

    new_header = "ESTIMATE_ROUNDED"
    header.append(new_header)

    estimate_index = header.index("ESTIMATE")

    for row in rows:
        if row[estimate_index].replace(".", "").isnumeric():
            new_value = round(float(row[estimate_index]), 2)
        else:
            new_value = row[estimate_index]

        row.append(str(new_value))

    return [header] + rows


def save_data(directory, filename, data):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_header = "Death Rates for Suicide by Sex, Race, Hispanic Origin, and Age"
    file_footer = "Report by: Cayden Young, Date: 10/31/2023"

    with open(os.path.join(directory, filename), "w") as file:
        file.write(file_header + "\n")
        for row in data:
            file.write(",".join(row) + "\n")
        file.write(file_footer)


def main():
    source_filepath = "Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv"
    data = load_data(source_filepath)
    data = add_column(data)
    save_data("out", "processed_data.csv", data)


if __name__ == "__main__":
    main()
