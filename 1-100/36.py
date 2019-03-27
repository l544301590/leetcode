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
                sec = {k: 0 for k in range(1, 10)}
                for k in range(9):
                    if board[i*3+k//3][j*3+k%3] != '.':
                        a = int(board[i*3+k//3][j*3+k%3])
                        if sec[a] != 0:
                            return False
                        else:
                            sec[a] += 1

        return True


s = Solution()
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))