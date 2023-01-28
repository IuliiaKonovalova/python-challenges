import unittest

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_simbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0


        altered_s = ''
        if "CM" in s:
            s = s.replace("CM", "")
            result += 900
            print(s)
        if "M" in s:
            for i in s:
                if i == "M":
                    s = s.replace("M", "")
                    result += 1000
                    print(s)
        if "CD" in s:
            s = s.replace("CD", "")
            result += 400
            print(s)
        if "D" in s:
            for i in s:
                if i == "D":
                    s = s.replace("D", "")
                    result += 500
        if "XC" in s:
            s = s.replace("XC", "")
            result += 90
        if "C" in s:
            for i in s:
                if i == "C":
                    s = s.replace("C", "")
                    result += 100
        if "IX" in s:
            s = s.replace("IX", "")
            result += 9
        if "XL" in s:
            s = s.replace("XL", "")
            result += 40
        if "L" in s:
            for i in s:
                if i == "L":
                    s = s.replace("L", "")
                    result += 50
        if "X" in s:
            for i in s:
                if i == "X":
                    s = s.replace("X", "")
                    result += 10
        if "IV" in s:
            s = s.replace("IV", "")
            result += 4
        if "V" in s:
            for i in s:
                if i == "V":
                    s = s.replace("V", "")
                    result += 5
        if "I" in s:
            for i in s:
                if i == "I":
                    s = s.replace("I", "")
                    result += 1
        
        return result


class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("III"), 3)
        self.assertEqual(solution.romanToInt("IV"), 4)
        self.assertEqual(solution.romanToInt("IX"), 9)
        self.assertEqual(solution.romanToInt("LVIII"), 58)
        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(solution.romanToInt("MMXIII"), 2013)
        self.assertEqual(solution.romanToInt("MCMXCVI"), 1996)
        self.assertEqual(solution.romanToInt("MCMXCVII"), 1997)
        self.assertEqual(solution.romanToInt("MCMXCVIII"), 1998)
        self.assertEqual(solution.romanToInt("MCMXCIX"), 1999)
        self.assertEqual(solution.romanToInt("MM"), 2000)

if __name__ == '__main__':
  unittest.main()