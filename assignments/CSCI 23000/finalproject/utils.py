def get_index_from_header(string: str, csv_header: str) -> int:
    return csv_header.replace("\n", "").split(",").index(string)
