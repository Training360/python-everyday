import csv

def read_csv_file(file, skip_first=True):
    with open(file, 'r') as file:
        reader = csv.reader(file)

        if skip_first:
            next(reader, None)
        return  [row for row in reader]


data = read_csv_file('./lessons/csv/employees-with-header.csv', False)
# print(data)