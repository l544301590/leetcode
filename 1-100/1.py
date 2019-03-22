# -*-coding:utf-8-*-


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum2(self, nums, target):  # Hashmap(Dict)
        d = {}
        for i in range(len(nums)):
            j = d.get(target - nums[i])
            if j is not None:
                return [j, i]
            d[nums[i]] = i
        return None


s = Solution()
a = s.twoSum2([2,7,11,15], 9)
print(a)