# -*-coding:utf-8-*-

class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            row = {k: 0 for k in range(1, 10)}
            col = {k: 0 for k in range(1, 10)}
            for j in range(9):
                if board[i][j] != '.':
                    a = int(board[i][j])
                    if row[a] != 0:
                        return False
                    else:
                        row[a] += 1
                if board[j][i] != '.':
                    a = int(board[j][i])
                    if col[a] != 0:
                        return False
                    else:
                        col[a] += 1
        for i in range(3):
            for j in range(3):

