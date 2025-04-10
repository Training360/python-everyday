import openpyxl
from os import path


def write_xlsx(file, headers, rows):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet.append(headers)

    for row in rows:
        sheet.append(row)

    workbook.save(file)


if __name__ == "__main__":
    headers = [
        "id",
        "first_name",
        "last_name",
        "email_address",
        "gender",
        "yearly_salary",
        "years_of_experience",
    ]

    rows = [
        [1, "John", "Doe", "john.doe@company.com", "Male", 120000, 9],
        [2, "Jane", "Doe", "jane.doe@company.com", "Female", 90000, 3],
    ]

    filename = "./files/employees-backup-1.xlsx"

    write_xlsx(filename, headers, rows)
