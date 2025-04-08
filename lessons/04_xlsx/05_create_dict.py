import openpyxl

def read_xlsx_file_generator(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    # Read header (first row)
    columns = [cell.value for cell in sheet[1]]
    
    yield columns  # Yield header

    # Yield the rest of the rows as dictionaries
    for row in sheet.iter_rows(min_row=2, values_only=True):
        yield dict(zip(columns, row))

if __name__ == "__main__":
    gen = read_xlsx_file_generator('./lessons/files/employees-with-header.xlsx')
    
    columns = next(gen)  # Get the header
    print("Header:", columns)
    
    print("Data:")
    for row in gen:  # Iterate over the remaining rows
        print(row)
