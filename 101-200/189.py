# -*-coding:utf-8-*-

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        tmp = nums[-k:].copy()
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = tmp[i]


s = Solution()
l = [1, 2, 3, 4, 5, 6]
s.rotate(l, 6)
print(l)