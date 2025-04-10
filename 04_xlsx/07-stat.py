import openpyxl


def validate_columns(file_columns, required_columns):
    missing_columns = [col for col in required_columns if col not in file_columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    return [file_columns.index(col) for col in required_columns]


def read_xlsx_file_generator(file_path, required_columns):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    columns = [cell.value for cell in sheet[1]]

    col_indices = validate_columns(columns, required_columns)

    yield required_columns

    for row in sheet.iter_rows(min_row=2, values_only=True):
        filtered_row = [row[i] for i in col_indices]
        yield dict(zip(required_columns, filtered_row))


def calculate_statistics(file_path, column_name):
    gen = read_xlsx_file_generator(file_path, [column_name])
    values = []
    stat = {"min": None, "max": None, "sum": None, "avg": None, "count": 0}

    for row in gen:
        try:
            value = float(row[column_name])
            values.append(value)
        except (ValueError, TypeError):
            continue

    if len(values) > 0:
        stat["count"] = len(values)
        stat["min"] = min(values)
        stat["max"] = max(values)
        stat["sum"] = sum(values)
        stat["avg"] = stat["sum"] / stat["count"]

    return stat


if __name__ == "__main__":
    stat = calculate_statistics("./files/employees-with-header.xlsx", "yearly_salary")
    print(stat)
