# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i