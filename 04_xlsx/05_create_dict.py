import openpyxl


def read_xlsx_file_generator(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    columns = [cell.value for cell in sheet[1]]

    yield columns

    for row in sheet.iter_rows(min_row=2, values_only=True):
        yield dict(zip(columns, row))


if __name__ == "__main__":
    gen = read_xlsx_file_generator("./files/employees-with-header.xlsx")

    columns = next(gen)
    print("Header:", columns)

    print("Data:")
    for row in gen:
        print(row)
