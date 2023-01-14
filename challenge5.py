import random
import unittest


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
amount_of_numbers = 6

def lottery_winner(num_list, amount):
    winner_numbers = random.sample(num_list, amount)
    return winner_numbers


print(lottery_winner(numbers, amount_of_numbers))




if __name__ == '__main__':
    unittest.main()