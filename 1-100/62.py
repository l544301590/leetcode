# -*-coding:utf-8-*-

class Solution:
    def uniquePaths(self, m, n):
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = 1 if i == 0 or j == 0 else dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


s = Solution()
a = s.uniquePaths(10, 10)
print(a)