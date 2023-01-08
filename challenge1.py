import unittest
#  Card Mask code challenge

str1 = "1234567891234567"
# First solution
string_length = len(str1)
print(string_length)
mask = string_length - 4
print(mask)
showstr = str1[mask:]
print(showstr)

print("Original String: " + str1)
print("Masked String: " + "*" * mask + showstr)


# second solution
def masking(card_number):
    return str(card_number)[-4:].rjust(len(str(card_number)), "*")

print(masking(1234567891234567))

class TestMaskCardTest(unittest.TestCase):
    def test_mask_card(self):
        self.assertEqual(masking("1234567891234567"), "************4567")


class TestMaskCardTest2(unittest.TestCase):

    param_list = [
        ("1234567891234567", "************4567"),
        (1234567891234567, "************4567"),
    ]

    def test_return_type(self):
        for par1, par2 in self.param_list:
            print(par1, par2)
            with self.subTest():
                self.assertEqual(masking(par1), par2)

if __name__ == '__main__':
    unittest.main()