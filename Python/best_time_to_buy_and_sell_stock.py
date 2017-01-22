# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        res = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            res = max(res, p - min_price)
        return res