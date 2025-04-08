import csv

def read_csv_file_generator(file_path):
    f = open(file_path, 'r')
    reader = csv.reader(f)
    columns = next(reader, None) 
    
    yield columns
    yield from reader
    
    f.close()

if __name__ == "__main__":
    gen = read_csv_file_generator('./lessons//files/employees-with-header.csv')
    columns = next(gen)
    print("Header:", columns)
    print("Data:")
    for row in gen:
        print(row)