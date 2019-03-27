# -*-coding:utf-8-*-


class Solution:
    def plusOne(self, digits):
        c = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += c
            if digits[i] > 9:
                digits[i], c = 0, 1
            else:
                c = 0
        if c == 1:
            digits = [1] + digits
        return digits


s = Solution()
a = s.plusOne([9, 9, 9, 9])
print(a)