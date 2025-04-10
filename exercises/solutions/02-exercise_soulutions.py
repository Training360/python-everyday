# 2.
from os import path


def sum_numbers_from_file(file):
    with open(file, 'r') as file:
        numbers = file.readline().strip().split(',')
        return sum(map(int, numbers))


print(sum_numbers_from_file('numbers.txt'))
