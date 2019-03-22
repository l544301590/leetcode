# -*-coding:utf-8-*-


class Solution:
    def intersect(self, nums1, nums2):
        d, res = {}, []
        for num in nums1:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        for num in nums2:
            if d.get(num):
                if d[num] > 0:
                    d[num] -= 1
                    res.append(num)
                else:
                    d.pop(num)
        return res


s = Solution()
a = s.intersect([1, 2, 2, 3, 4], [2, 2, 3, 4, 5])
print(a)