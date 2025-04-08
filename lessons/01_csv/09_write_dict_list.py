import csv

def write_csv(file, rows):
    fields = list(rows[0].keys())
    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(rows)


if __name__ == "__main__":
    rows = [
            {
                'id': 1,
                'first_name': 'John', 
                'last_name': 'Doe', 
                'email_address': 'john.doe@company.com', 
                'gender': 'Male', 
                'yearly_salary': 120000, 
                'years_of_experience': 9
            },
            {
                'id': 2,
                'first_name': 'Jane', 
                'last_name': 'Doe', 
                'email_address': 'jane.doe@company.com', 
                'gender': 'Female', 
                'yearly_salary': 90000, 
                'years_of_experience': 3
            },
        ]

    filename = "./lessons//files/employees-backup-2.csv"

    write_csv(filename, rows)