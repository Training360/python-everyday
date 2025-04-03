import csv

def read_csv_file(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        print([row for row in reader])


if __name__ == "__main__":
    read_csv_file('./lessons/csv/employees-with-header.csv')
