# 1.
from os import path


def write_name_to_file(file):
    user_name = input('Add meg a neved: ')
    with open(file, 'w') as file:
        file.write(user_name)


write_name_to_file('username.txt')
