# https://leetcode-cn.com/problems/minesweeper/description/

class Solution():

    def updateBoard(self, board, click):
        row, col = click
        if board[row][col] == "M":
            board[row][col] = 'X'
        else:
            count = 0 # 周围地雷数量
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if row + i < 0 or j  + col < 0 or row + i >= len(board) or col + j >= len(board[0]): continue
                    if board[row + i][col + j] == 'M':
                        count += 1
            if count > 0:
                board[row][col] = str(count)
            else:
                board[row][col] = 'B'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if row + i < 0 or j  + col < 0 or row + i >= len(board) or col + j >= len(board[0]): continue
                        if board[row + i][col + j] == 'E': self.updateBoard(board, [row + i, col + j])
        return board