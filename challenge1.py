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
    return str(card_number[-4:]).rjust(len(str(card_number)), "*")

print(masking("1234567891234567"))

class TestMaskCardTest(unittest.TestCase):
    def test_mask_card(self):
        self.assertEqual(masking("1234567891234567"), "************4567")


if __name__ == '__main__':
    unittest.main()