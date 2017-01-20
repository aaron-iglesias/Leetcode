# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = tmp_res = 0
        for n in nums:
            if n == 1:
                tmp_res += 1
            else:
                res = max(res, tmp_res)
                tmp_res = 0
        return max(res, tmp_res)