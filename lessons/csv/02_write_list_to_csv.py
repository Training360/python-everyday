import csv
from os import path


def write_csv(file, fields, rows):
    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


# field names
fields = ['id', 'first_name', 'last_name', 'email_address', 'gender', 'yearly_salary', 'years_of_experience']

# data rows of csv file
rows = [
        [1, 'John', 'Doe', 'john.doe@company.com', 'Male', 120000, 9],
        [2, 'Jane', 'Doe', 'jane.doe@company.com', 'Female', 90000, 3],
       ]

# name of csv file
filename = "employees.csv"

write_csv(filename, fields, rows)