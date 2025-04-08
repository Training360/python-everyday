import csv
import os

def get_max_id(file):
    max_id = 0

    try:
        with open(file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'id' in row and row['id'].isdigit():
                    max_id = max(max_id, int(row['id']))
    except Exception as e:
        print(f"Error reading file for max ID: {e}")
    
    return max_id

def add_id_field(file, rows):
    max_id = get_max_id(file)
  
    for row in rows:
            max_id += 1
            row['id'] = str(max_id)
    
    fields = list(rows[0].keys())

    if 'id' not in fields:
        fields.insert(0, 'id') 

    return fields, rows


def append_csv(file, rows):    
    file_exists = os.path.isfile(file)
    
    if not file_exists:
        print(f"File {file} does not exist.")
    
    if not rows:
        return

    fields, rows = add_id_field(file, rows)

    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writerows(rows)


new_rows = [
        {
            'first_name': 'Robert', 
            'last_name': 'Smith', 
            'email_address': 'robert.smith@company.com', 
            'gender': 'Male', 
            'yearly_salary': 110000, 
            'years_of_experience': 7
        },
        {
            'first_name': 'Maria', 
            'last_name': 'Garcia', 
            'email_address': 'maria.garcia@company.com', 
            'gender': 'Female', 
            'yearly_salary': 95000, 
            'years_of_experience': 5
        },
       ]

filename = "./lessons//files/employees.csv"

if __name__ == "__main__":
    append_csv(filename, new_rows)
    print(f"Appended {len(new_rows)} rows to {filename}")