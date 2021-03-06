# -*-coding:utf-8-*-


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - i * 2 - 1):
                tmp = matrix[n - i - j - 1][i]
                matrix[n - i - j - 1][i] = matrix[n - i - 1][n - i - j - 1]
                matrix[n - i - 1][n - i - j - 1] = matrix[i + j][n - i - 1]
                matrix[i + j][n - i - 1] = matrix[i][i + j]
                matrix[i][i + j] = tmp


s = Solution()
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
s.rotate(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
