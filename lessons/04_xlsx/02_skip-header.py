import openpyxl

def read_xlsx_file(file, skip_first=True):
    # Open the Excel file
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active  # Use the active sheet (default sheet)

    # Skip the first row (header) if skip_first is True
    rows = list(sheet.iter_rows(values_only=True))
    
    if skip_first:
        rows = rows[1:]

    return rows

if __name__ == "__main__":
    data = read_xlsx_file('./lessons/files/employees-with-header.xlsx', False)
    print(data)
