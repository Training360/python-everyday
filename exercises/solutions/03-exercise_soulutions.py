# 3.
from os import path


def sort_names(file):
    with open(file, 'r') as file:
        names = [name.strip() for name in file.readlines()]
        return sorted(names)


print(sort_names('primarchs.txt'))
