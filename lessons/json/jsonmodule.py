from json import load


def fetch_items(file, prop):
    json_file = open(
        file=file,
        mode='r',
        encoding='utf-8'
    )
    return load(json_file)[prop]
