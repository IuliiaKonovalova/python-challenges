import unittest


word1 = "python"
word2 = "typhon"
word3 = "pythonn"
word4 = "typhom"

def is_anagram(word1, word2):
    if len(word1) == len(word2) and word1 == word2:
        return sorted(word1) == sorted(word2)


print(is_anagram(word1, word2))

class TestAnagram(unittest.TestCase):

    param_list = [
        (word1, word2),
        (word1, word3),
    ]

    def test_return(self):
        for par1, par2 in self.param_list:
            self.assertTrue(is_anagram(word1, word1))
            self.assertFalse(is_anagram(word1, word2))
            self.assertFalse(is_anagram(word1, word3))
            self.assertFalse(is_anagram(word1, word4))


if __name__ == '__main__':
    unittest.main()