# -*-coding:utf-8-*-


class Solution:
    def isPalindrome(self, s):
        s1 = ""
        for ch in s:
            if ch.isalpha():
                s1 += ch.lower()
            if ch.isdecimal():
                s1 += ch
        for i in range(len(s1) // 2):
            if s1[i] != s1[len(s1)-1-i]:
                return False
        return True


s = Solution()
a = s.isPalindrome("0P,00")
print(a)