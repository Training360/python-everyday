import json
from os import path


def write_to_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    data = [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@company.org",
            "gender": "Male",
            "yearly_salary": 78395,
            "years_of_experience": 23
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@company.org",
            "gender": "Female",
            "yearly_salary": 65789,
            "years_of_experience": 19
        }
    ]

    file = './lessons//files/new_employees.json'
    write_to_json(file, data)
