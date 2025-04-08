import openpyxl

def validate_columns(file_columns, required_columns):
    missing_columns = [col for col in required_columns if col not in file_columns]
    if missing_columns:
        raise ValueError(f"Hiányzó oszlopok az XLSX fájlban: {missing_columns}")
    
    return [file_columns.index(col) for col in required_columns]

def read_xlsx_file_generator(file_path, required_columns):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    columns = [cell.value for cell in sheet[1]]  # First row is the header
    col_indices = validate_columns(columns, required_columns)
    
    yield required_columns
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        filtered_row = [row[i] for i in col_indices]
        yield dict(zip(required_columns, filtered_row))

if __name__ == "__main__":
    required_cols = ["yearly_salary", "years_of_experience"]
    file_path = './lessons/files/employees-with-header.xlsx' 
    
    try:
        gen = read_xlsx_file_generator(file_path, required_cols)
        columns = next(gen)
        print("Header:", columns)
        print("Data:")
        for row in gen:
            print(row)
    except ValueError as e:
        print("Error:", e)
