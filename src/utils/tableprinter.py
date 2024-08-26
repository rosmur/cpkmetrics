def print_table(data):
    col_names = ["Metric", "Value"]

    # Convert dictionary to list of lists, formatting floats to 3 decimal place
    table_data = []
    for k, v in data.items():
        if isinstance(v, float):
            v = f"{v:.3f}"
        table_data.append([k, v])

    # Find the maximum width for each column
    col_widths = [
        max(len(str(item)) for item in col) for col in zip(*table_data, col_names)
    ]

    # Create the format string
    row_format = "| {:<" + str(col_widths[0]) + "} | {:<" + str(col_widths[1]) + "} |"

    # Print header and divider
    print(row_format.format(*col_names))
    print("|" + "-" * (sum(col_widths) + 5) + "|")

    # Print rows
    for row in table_data:
        print(row_format.format(str(row[0]), str(row[1])))
