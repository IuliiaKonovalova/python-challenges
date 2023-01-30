import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked_value_index = {}
        for i in range(len(nums)):
            diff_with_target = target - nums[i]
            if diff_with_target in checked_value_index:
                return [checked_value_index[diff_with_target], i]
            else:
                checked_value_index[nums[i]] = i


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 3], 6), [0, 2])


if __name__ == '__main__':
  unittest.main()