# 7.
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)


def calculate_class_average(students):
    grades = []
    for student in students:
        grades.append(student[1])
    return calculate_average(grades)


students = [
    ('John', 85),
    ('Jane', 92),
    ('Mark', 77),
    ('Sarah', 90)
]
print(calculate_class_average(students))
