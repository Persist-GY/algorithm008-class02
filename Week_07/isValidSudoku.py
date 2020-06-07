# https://leetcode-cn.com/problems/valid-sudoku/

class Solution():

    def isValidSudoku(self, board):
        # 所在行
        row = [set() for _ in range(9)]
        # 所在列
        col = [set() for _ in range(9)]
        # 所在块
        block = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    if num in row[i] or num in col[j] or num in block[(i//3)*3+j//3]:
                        return False
                    row[i].add(num)
                    col[j].add(num)
                    block[(i//3)*3+j//3].add(num)
        return True


        