import csv

def validate_columns(file_columns, required_columns):
    missing_columns = [col for col in required_columns if col not in file_columns]
    if missing_columns:
        raise ValueError(f"Hiányzó oszlopok a CSV-ben: {missing_columns}")
    
    return [file_columns.index(col) for col in required_columns]

def read_csv_file_generator(file_path, required_columns):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        columns = next(reader)
    
        col_indices = validate_columns(columns, required_columns)
        
        yield required_columns
        
        for row in reader:
            filtered_row = [row[i] for i in col_indices]
            yield dict(zip(required_columns, filtered_row))


if __name__ == "__main__":
    required_cols = ["yearly_salary","years_of_experience"] 
    file_path = './lessons/csv/files/employees-with-header.csv'
    try:
        gen = read_csv_file_generator(file_path, required_cols)
        columns = next(gen)
        print("Header:", columns)
        print("Data:")
        for row in gen:
            print(row)
    except ValueError as e:
        print("Error:", e)