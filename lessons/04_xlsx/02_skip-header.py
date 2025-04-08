import openpyxl

def read_xlsx_file(file, skip_first=True):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active  # Use the active sheet (default sheet)
    rows = list(sheet.iter_rows(values_only=True))

    return rows[1:] if skip_first else rows

if __name__ == "__main__":
    data = read_xlsx_file('./lessons/files/employees-with-header.xlsx', False)
    print(data)
