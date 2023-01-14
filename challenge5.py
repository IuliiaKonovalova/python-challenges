import random
import unittest


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
amount_of_numbers = 6

def lottery_winner(num_list, amount):
    winner_numbers = random.sample(num_list, amount)
    return winner_numbers


print(lottery_winner(numbers, amount_of_numbers))

class TestLotteryWinner(unittest.TestCase):

    param_list = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6,),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5,),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4,),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3,),
    ]

    def test_return_type(self):
        for par1, par2 in self.param_list:
            with self.subTest():
                self.assertIsInstance(lottery_winner(par1, par2), list)
                self.assertEqual(len(lottery_winner(par1, par2)), par2)


if __name__ == '__main__':
    unittest.main()