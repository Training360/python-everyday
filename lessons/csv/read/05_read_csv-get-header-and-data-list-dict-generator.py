import csv

def read_csv_file_generator(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader, None)
        yield columns  

        for row in reader:
            yield dict(zip(columns, row)) 

# Generátor használata
gen = read_csv_file_generator('./lessons/csv/employees-with-header.csv')
columns = next(gen)
print("Header:", columns)
print("Data:")
for row in gen:
    print(row)
