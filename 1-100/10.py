# -*-coding:utf-8-*-

# TODO UNSOLVED

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p))] for i in range(len(s))]
        if len(p) == 0:
            return True
        if len(s) == 0:
            if p == ".*":
                return True
            return False
        if p[0] == '.' or s[0] == p[0]:
            dp[0][0] = True
        for i in range(0, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
                else:
                    return False
        return dp[len(s) - 1][len(p) - 1]


a = "aab"
b = "c*a*b"
s = Solution()
c = s.isMatch(a, b)
print(c)
