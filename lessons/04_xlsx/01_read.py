import openpyxl

def read_xlsx_file(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active  
    for row in sheet.iter_rows(values_only=True):
        print(row)

if __name__ == "__main__":
    read_xlsx_file('./lessons/files/employees.xlsx')
