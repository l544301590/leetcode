# -*-coding:utf-8-*-
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        cur, i, j = nums[0], 0, 0
        while i < len(nums):
            nums[j] = cur
            j += 1
            while i < len(nums) and nums[i] == cur:
                i += 1
            if i != len(nums):
                cur = nums[i]
        return j


s = Solution()
a = s.removeDuplicates([1, 1,2, 3])
print(a)