# https://leetcode-cn.com/problems/number-of-islands/

class Solution():

    def numIslands(self, grid):
        num = 0
        if not grid: return num
        def DFS(row, col):
            grid[row][col] = '0'
            if row - 1 >= 0 and grid[row - 1][col] == '1': DFS(row - 1, col)
            if row + 1 <len(grid) and grid[row + 1][col] == '1': DFS(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == '1': DFS(row, col - 1)
            if col + 1 < len(grid[0]) and grid[row][col + 1] == '1': DFS(row, col + 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    DFS(row, col)
                    num += 1
        return num