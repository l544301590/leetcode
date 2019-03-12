# -*-coding:utf-8-*-


class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if d.get(num):
                return True
            d[num] = True
        return False


s = Solution()
a = s.containsDuplicate([1, 2, 3, 1])
print(a)