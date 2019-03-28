# -*-coding:utf-8-*-


class Solution:
    def isAnagram(self, s, t):
        ds, dt = {}, {}
        for ch in s:
            if ds.get(ch):
                ds[ch] += 1
            else:
                ds[ch] = 1
        for ch in t:
            if dt.get(ch):
                dt[ch] += 1
            else:
                dt[ch] = 1
        if ds == dt:
            return True
        return False


s = Solution()
a = s.isAnagram("abbcd", "babcdc")
print(a)