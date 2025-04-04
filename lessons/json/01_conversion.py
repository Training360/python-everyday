from json import loads, dumps

employee_json = '''{
    "id": 1,
    "first_name": "Jayne",
    "last_name": "Burchmore",
    "email": "jburchmore0@unicef.org",
    "gender": "Female",
    "yearly_salary": 78395,
    "years_of_experience": 23
  }'''

# json to python code
employee = loads(employee_json)
print(type(employee), employee)
print(employee['email'])

# to json
employee["first_name"] = "Jane"
employee["last_name"] = "Doe"

updated_employee_json = dumps(employee)
print(updated_employee_json)
