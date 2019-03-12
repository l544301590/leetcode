# -*-coding:utf-8-*-

class Solution:
    def romanToInt(self, s):
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return d[s[0]]

        sum_, i = 0, 0
        while i < len(s) - 1:
            if d[s[i+1]] > d[s[i]]:  # 如果下一个比较大
                sum_ += d[s[i+1]] - d[s[i]]  # 则这两个字符表示一个值
                i += 1   # 跳过下一个字符
            else:
                sum_ += d[s[i]]  # 当前这个字符单独表示一个值
            i += 1  # 计数器加一
        sum_ += d[s[-1]] if d[s[-1]] <= d[s[-2]] else 0  # 最后一个字符单独计算
        return sum_


s = Solution()
a = s.romanToInt("MCMXCIV")
print(a)