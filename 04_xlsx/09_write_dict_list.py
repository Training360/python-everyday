import openpyxl


def write_xlsx(file, rows):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    headers = list(rows[0].keys())

    sheet.append(headers)

    for row in rows:
        sheet.append(list(row.values()))

    workbook.save(file)


if __name__ == "__main__":
    rows = [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "john.doe@company.com",
            "gender": "Male",
            "yearly_salary": 120000,
            "years_of_experience": 9,
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Doe",
            "email_address": "jane.doe@company.com",
            "gender": "Female",
            "yearly_salary": 90000,
            "years_of_experience": 3,
        },
    ]

    filename = "./files/employees-backup-2.xlsx"

    write_xlsx(filename, rows)
