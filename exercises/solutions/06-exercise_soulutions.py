# 6.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
