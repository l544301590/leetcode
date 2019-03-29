# -*-coding:utf-8-*-


class Solution:
    def myAtoi(self, str):
        s, i, flag = str.strip(), 0, 1
        if len(s) == 0:
            return 0
        if s[0] != '-' and not s[0].isdecimal():
            return 0
        if s[0] == '-':
            flag = -1
            s = s[1:]
        if len(s) == 0:
            return 0
        while i < len(s) and s[i].isdecimal():
            i += 1
        res = int(s[:i]) * flag
        res = res if res <= 2**31-1 else 2**31-2
        res = res if res >= -2**31 else -2**31
        return res


s = Solution()
a = s.myAtoi('-+1')
print(a)