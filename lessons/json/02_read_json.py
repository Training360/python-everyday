from json import load
from os import path


def fetch_items(file):
    json_file = open(
        file=file,
        mode='r',
        encoding='utf-8'
    )
    return load(json_file)


if __name__ == "__main__":
     print(fetch_items('./lessons/json/files/employees.json'))
