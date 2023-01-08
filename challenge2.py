import os
import sys
import unittest

file_path = "just_text.txt"
file_path2 = "just_text2.txt"


try:
    size = os.path.getsize(file_path)

except FileNotFoundError:
    print("File not found")
    sys.exit()

print("File size is", size, "bytes")

# solution2

def get_file_size(file_path_ex):
    try:
        size = os.path.getsize(file_path_ex)
        return print("File size: ", size, "bytes.")
    except FileNotFoundError:
        return "File not found"


get_file_size(file_path)
get_file_size(file_path2)

class TestGetFileSize(unittest.TestCase):

    param_list = [
        # ("just_text.txt", "File size: is 38 bytes."),
        (file_path2, "File not found"),
    ]

    def test_return(self):
        for par1, par2 in self.param_list:
            print(par1, par2)
            with self.subTest():
                self.assertEqual(get_file_size(par1), par2)


if __name__ == '__main__':
    unittest.main()