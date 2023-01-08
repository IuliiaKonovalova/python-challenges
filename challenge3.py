import unittest

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]

def flatten_list(nested_list):
    flatted_list = []
    [flatted_list.extend(i) for i in nested_list]
    return flatted_list

print(flatten_list(nested_list))

