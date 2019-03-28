# -*-coding:utf-8-*-


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return []
        n = len(matrix)
        for i in range(n):
            tmp = matrix[i]

