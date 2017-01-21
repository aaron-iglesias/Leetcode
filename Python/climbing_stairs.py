# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        sqrt5 = pow(5, 0.5)
        return int(pow((1 + sqrt5) / 2, n + 1) / sqrt5 + 0.5)