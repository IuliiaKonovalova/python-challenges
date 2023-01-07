#  Card Mask code challenge

str = "1234567891234567"
# First solution
string_length = len(str)
print(string_length)
mask = string_length - 4
print(mask)
showstr = str[mask:]
print(showstr)

print("Original String: " + str)
print("Masked String: " + "*" * mask + showstr)


# second solution
def masking(card_number):
    return str(card_number)[-4:].rjust(len(card_number), '*')

print(masking("1234567891234567"))



