# -*-coding:utf-8-*-


class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        n_row, n_col, res = len(matrix), len(matrix[0]), 0
        dp = [[0 for j in range(n_col+1)] for i in range(n_row+1)]
        for i in range(1, n_row+1):
            for j in range(1, n_col+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                if dp[i][j] > res:
                    res = dp[i][j]
        return res**2


s = Solution()
a = s.maximalSquare([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])
print(a)