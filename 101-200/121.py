# -*-coding:utf-8-*-

class Solution:
    def maxProfit(self, prices):
        mi, ma = 65535, 0
        for i in range(len(prices)):
            if ma < prices[i] - mi:
                ma = prices[i] - mi
            if mi > prices[i]:
                mi = prices[i]
        return ma


s = Solution()
a = s.maxProfit([])
print(a)