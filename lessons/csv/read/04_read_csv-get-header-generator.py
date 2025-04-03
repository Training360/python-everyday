import csv

def read_csv_file_generator(file_path, skip_first=True):
    f = open(file_path, 'r')
    reader = csv.reader(f)
    columns = next(reader, None) if skip_first else None
    
    yield columns
    yield from reader
    
    f.close()

# Get both header and data
gen = read_csv_file_generator('./lessons/csv/employees-with-header.csv')
columns = next(gen)
print("Header:", columns)
print("Data:")
for row in gen:
    print(row)