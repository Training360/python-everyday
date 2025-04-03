# importing the csv module
import csv


def write_dict_list_to_csv(file, dict_list):
    fileds = dict_list[0].keys()
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fileds)
        writer.writeheader()
        writer.writerows(dict_list)


data = [
    {'name': 'John', 'age': 25, 'city': 'New York'},
    {'name': 'Jane', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Bob', 'age': 35, 'city': 'Seattle'}
]

write_dict_list_to_csv('users.csv', data)
