import json
import os


def fetch_items(file):
    json_file = open(file=file, mode="r", encoding="utf-8")
    return json.load(json_file)


def append_to_json(file, new_data):
    data = fetch_items(file)

    if isinstance(new_data, dict):
        data.append(new_data)
    elif isinstance(new_data, list):
        data.extend(new_data)
    else:
        print(
            f"Error: Invalid data type. Expected dict or list, got {type(new_data).__name__}."
        )
        return

    # Írjuk vissza az adatokat a fájlba
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    file = "./files/new_employees.json"
    new_employee = {
        "id": 3,
        "first_name": "Robert",
        "last_name": "Smith",
        "email": "robert.smith@company.org",
        "gender": "Male",
        "yearly_salary": 82500,
        "years_of_experience": 15,
    }

    append_to_json(file, new_employee)
