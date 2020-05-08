# https://leetcode-cn.com/problems/minesweeper/
from typing import List


class Solution():

    # DFS
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        row, col = click[0], click[1]
        # 判断是否是地雷
        if board[row][col] == "M":
            board[row][col] = 'X'
        else:
            # 不是地雷判断周围有没有地雷显示数字
            # 周围 8个 左，右 上，下 左上，右上  左下，右下
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # 当前点击位置过滤
                    if i == 0 and j == 0: continue
                    r, c = row + i, col + j
                    # 超出面板 过滤
                    if c < 0 or r < 0 or r >= m or c >= n: continue
                    if board[r][c] == "M" or board[r][c] == "X": count +=1
            if count > 0:
                # 表示周围有地雷
                board[row][col] = str(count)
            else:
                # 周围没有地雷 查找出其他B
                board[row][col] = "B"
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # 当前点击位置过滤
                        if i == 0 and j == 0: continue
                        r, c = row + i, col + j
                        # 超出面板 过滤
                        if c < 0 or r < 0 or r >= m or c >= n: continue
                        if board[r][c] == "E": self.updateBoard(board, [r, c])
        return board

    # BFS
    def updateBoard2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        queue = [click]
        m, n = len(board), len(board[0])
        while queue:
            cell = queue.pop()
            row, col = cell[0], cell[1]
            # 是否是地雷
            if board[row][col] == "M":
                # 地雷
                board[row][col] = "X"
            else:
                # 不是地雷
                # 判断是否周围有地雷
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # 当前过滤掉
                        if i == 0 and j == 0: continue
                        r, c = row + i, col + j
                        # 超出边界过滤掉
                        if r < 0 or c < 0 or r >= m or c >= n: continue
                        # 判断是否是地雷
                        if board[r][c] == 'M' or board[r][c] == "X": count +=1
                if count >0:
                    # 周围有地雷
                    board[row][col] = str(count)
                else:
                    # 周围没有地雷，继续查看其它空块
                    board[row][col] = 'B'
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            # 当前过滤掉
                            if i == 0 and j == 0: continue
                            r, c = row + i, col + j
                            # 超出边界过滤掉
                            if r < 0 or c < 0 or r >= m or c >= n: continue
                            if board[r][c] == "E": 
                                queue.insert(0, [r, c])
                                board[r][c] = 'B'; # Avoid to be added again.
        return board