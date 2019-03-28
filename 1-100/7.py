# -*-coding:utf-8-*-


class Solution:
    def reverse(self, x):
        x = str(x)
        flag = 1
        if x[0] == '-':
            x = x[1:]
            flag = -1
        x = x[::-1]

        i = 0
        for i in range(len(x)):
            if x[i] != '0':
                break

        x = x[i:]
        x = int(x) * flag

        if x > 2**31-1 or x < -2**31:
            return 0

        return x


s = Solution()
a = s.reverse(-12344444444444)
print(a)