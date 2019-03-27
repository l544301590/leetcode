# -*-coding:utf-8-*-
from urllib3 import request
import urllib3

class Solution:
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a

urllib3.__version__