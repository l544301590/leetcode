# -*-coding:utf-8-*-


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


s = Solution()
a = ["a", "b", "c", "d", "e"]
s.reverseString(a)
print(a)