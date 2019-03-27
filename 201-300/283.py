# -*-coding:utf-8-*-

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0


s = Solution()
a = [0, 1, 0, 2, 3]
s.moveZeroes(a)
print(a)