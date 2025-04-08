import openpyxl

def read_xlsx_file(file):
    # Open the Excel file
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active  # Use the active sheet (default sheet)

    # Read the entire sheet into a list of rows (values only)
    rows = list(sheet.iter_rows(values_only=True))

    # Separate columns (header) from data
    columns = rows[0]
    data = rows[1:]

    return columns, data

if __name__ == "__main__":
    columns, data = read_xlsx_file('./lessons/files/employees-with-header.xlsx')
    print('Columns: ', columns)
    print('Data: ', data)
