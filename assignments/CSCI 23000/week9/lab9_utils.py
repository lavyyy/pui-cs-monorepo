import os

def parse_line(line):
    fields = []
    field = ""
    in_quotes = False

    for char in line.strip():  # strip the line to remove the newline character at the end
        if char == '"':
            in_quotes = not in_quotes  # toggle in_quotes status
        elif char == ',' and not in_quotes:
            fields.append(field)  # dont strip here, it removes intended spaces
            field = ""
        else:
            field += char

    fields.append(field)  # add the last field, which could be empty if the line ends with a comma

    return fields

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            data = [parse_line(line) for line in lines]
        return data
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        return []

def add_column(data):
    header = data[0]
    rows = data[1:]

    new_header = "ESTIMATE_ROUNDED"
    header.append(new_header)

    estimate_index = header.index("ESTIMATE")

    for row in rows:
        try:
            # try to convert to float and round to the nearest whole number
            estimate_value = float(row[estimate_index])
            new_value = round(estimate_value)
        except ValueError:
            # if it's not a number just use the original value
            new_value = row[estimate_index]

        row.append(str(new_value))


    return [header] + rows

def save_data(directory, filename, data):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_header = "Death Rates for Suicide by Sex, Race, Hispanic Origin, and Age"
    file_footer = "Report by: Cayden Young, Date: 10/31/2023"

    with open(os.path.join(directory, filename), "w") as file:
        file.write(file_header + "\n")  # file header
        for row in data:
            formatted_row = []
            for field in row:
                # check if the field contains a comma or if its an empty field that should remain empty
                if ',' in field:
                    formatted_row.append(f'"{field}"')  # wrap field in quotes if it contains a comma
                else:
                    formatted_row.append(field)  # keep field as is (which could be an empty string)
            file.write(",".join(formatted_row) + "\n")
        file.write(file_footer)  # file footer

