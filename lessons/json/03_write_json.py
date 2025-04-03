import json
from os import path


def write_to_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

file = 'data.json'

write_to_json(file, data)
