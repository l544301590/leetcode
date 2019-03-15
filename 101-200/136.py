# -*-coding:utf-8-*-

class Solution:
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a