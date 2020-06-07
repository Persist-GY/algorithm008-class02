# https://leetcode-cn.com/problems/sudoku-solver/

from typing import List
class Solution():


    # 时间复杂度比较高
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidSudoku(board, row, col, c):
            
            for i in range(9):
                if board[row][i] != '.' and board[row][i] == c: return False
                if board[i][col] != '.' and board[i][col] == c: return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] != '.' and board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                    return False
            return True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if isValidSudoku(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.solveSudoku(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True


    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1,10)) for _ in range(9)] # 行可用数字
        col = [set(range(1,10)) for _ in range(9)]# 列可用数字
        block = [set(range(1,10)) for _ in range(9)]# 块可用数字
        empty = [] # 保存空格位置
        # 先去除不可用的数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row[i].remove(num)
                    col[j].remove(num)
                    block[3*(i//3)+j//3].remove(num)
                else:
                    empty.append((i, j))

        def backtrack(level=0):
            if level == len(empty):
                return True
            i, j = empty[level]
            for num in row[i] & col[j] & block[(i//3)*3+j//3]:
                board[i][j] = str(num)
                row[i].remove(num)
                col[j].remove(num)
                block[(i//3)*3+j//3].remove(num)
                if backtrack(level+1):
                    return True
                row[i].add(num)
                col[j].add(num)
                block[(i//3)*3+j//3].add(num)
            return False
        backtrack()