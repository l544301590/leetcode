# -*-coding:utf-8-*-
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        n = len(s)
        s += "#"
        p = [[False for j in range(n)] for i in range(n)]
        max_ = 1
        x, y = 0, 0
        for i in range(n):
            p[i][i] = True
            if s[i] == s[i+1]:
                p[i][i+1] = True
                if 2 > max_:
                    max_ = 2
                    x, y = i, i+1
            o = 1
            # 由一个字母(s[i])或两个字母(s[i], s[i+1])向两边扩展遍历
            while True:
                if i-o < 0 or i+1+o > n:
                    break
                if p[i-o+1][i+o-1] == True and s[i-o] == s[i+o]:
                    p[i-o][i+o] = True
                    if 2*o+1 > max_:
                        max_ = 2*o+1
                        x, y = i-o, i+o
                if p[i-o+1][i+1+o-1] == True and s[i-o] == s[i+1+o]:
                    p[i-o][i+1+o] = True
                    if 2*o+2 > max_:
                        max_ = 2*o+2
                        x, y = i-o, i+1+o
                o += 1

        # 错误遍历方式（已省略初始化）
        # for i in range(n):
        #     for j in range(i+2, n):
        #         if p[i+1][j-1] == True and s[i] == s[j]:
        #             p[i][j] = True
        #             if j - i + 1 > max_:
        #                 max_ = j - i + 1
        return s[x:y+1]


if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("caacdcdc")
    print(res)