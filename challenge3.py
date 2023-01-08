import unittest
import itertools

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]

def flatten_list(nested_list):
    flatted_list = []
    [flatted_list.extend(i) for i in nested_list]
    return flatted_list

print(flatten_list(nested_list))

def flatted_list_with_itertools(nested_list):
    return list(itertools.chain(*nested_list))

class TestFlattenList(unittest.TestCase):

    param_list = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
        ),
        (
            [[1, 2, 3], [4,[1, 2, 3], 5, 6], [7, 8, 9], ['a', 'b', 'c'], ],
            [1, 2, 3, 4, [1, 2, 3], 5, 6, 7, 8, 9, 'a', 'b', 'c']
        ),
    ]

    def test_return(self):
        for par1, par2 in self.param_list:
            with self.subTest():
                self.assertEqual(flatten_list(par1), par2)

class TestFlatten_listWithItertools(unittest.TestCase):

    param_list = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
        ),
        (
            [[1, 2, 3], [4,[1, 2, 3], 5, 6], [7, 8, 9], ['a', 'b', 'c'], ],
            [1, 2, 3, 4, [1, 2, 3], 5, 6, 7, 8, 9, 'a', 'b', 'c']
        ),
    ]

    def test_return(self):
        for par1, par2 in self.param_list:
            with self.subTest():
                self.assertEqual(flatted_list_with_itertools(par1), par2)

if __name__ == '__main__':
    unittest.main()