class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(31):
            b = n & 1
            res = res | b
            res = res << 1
            n = n >> 1
        res = res | (n & 1)
        return res