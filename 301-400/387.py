# -*-coding:utf-8-*-


class Solution:
    def firstUniqChar(self, s):
        alphabet = {chr(asc): 0 for asc in range(ord("a"), ord("z")+1)}
        for ch in s:
            alphabet[ch] += 1
        for i in range(len(s)):
            if alphabet[s[i]] == 1:
                return i
        return -1


s = Solution()
a = s.firstUniqChar("loveleetcode")
print(a)