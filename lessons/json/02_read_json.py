from json import load
from os import path


def fetch_items(file, prop):
    json_file = open(
        file=file,
        mode='r',
        encoding='utf-8'
    )
    return load(json_file)[prop]


print(fetch_items('MOCK_DATA.json', 'users'))
