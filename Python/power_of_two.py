# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0